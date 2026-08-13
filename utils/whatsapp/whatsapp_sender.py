import os
import tempfile
import time
import logging
from pathlib import Path
from typing import Union

from PySide6.QtCore import QByteArray

from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeout


class WhatsAppSender:
    """
    WhatsApp Sender menggunakan Playwright (Lebih Stabil)
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, user_data_dir: str, headless: bool = False, timeout: int = 45):
        if hasattr(self, "_initialized"):
            return

        self._initialized = True
        self.user_data_dir = user_data_dir
        self.headless = headless
        self.timeout = timeout
        self.browser = None
        self.context = None
        self.page = None
        self._logger = logging.getLogger(__name__)

    def start(self):
        """Start browser Playwright"""
        if self.page:
            return

        try:
            playwright = sync_playwright().start()
            self.browser = playwright.chromium.launch_persistent_context(
                user_data_dir=self.user_data_dir,
                headless=self.headless,
                viewport={"width": 1200, "height": 800},
                args=[
                    "--start-maximized",
                    "--disable-blink-features=AutomationControlled",
                    "--no-sandbox",
                ]
            )
            self.page = self.browser.pages[0] if self.browser.pages else self.browser.new_page()
            self._logger.info("✅ Playwright browser started successfully")
        except Exception as e:
            self._logger.error(f"❌ Gagal start Playwright: {e}")
            raise

    def stop(self):
        """Tutup browser"""
        try:
            if self.browser:
                self.browser.close()
        except:
            pass
        self.browser = None
        self.page = None

    def send(self, nomor: str, pdf_file: Union[str, bytes, QByteArray, Path], caption: str = "") -> bool:
        """Kirim PDF via WhatsApp Web dengan Playwright - Versi Stabil"""
        temp_file = None
        try:
            self.start()

            # Persiapan File
            if isinstance(pdf_file, (bytes, QByteArray)):
                fd, temp_file = tempfile.mkstemp(suffix=".pdf")
                os.close(fd)
                with open(temp_file, "wb") as f:
                    f.write(bytes(pdf_file))
                pdf_path = temp_file
            else:
                pdf_path = str(pdf_file)

            # Buka Chat
            clean_number = self._clean_number(nomor)
            self.page.goto(f"https://web.whatsapp.com/send?phone={clean_number}", timeout=60000)

            # Tunggu chat benar-benar terbuka (lebih aman)
            self.page.wait_for_load_state("networkidle", timeout=30000)
            time.sleep(3)  # Beri waktu WhatsApp memuat

            # === Kirim Caption ===
            if caption:
                try:
                    textbox = self.page.wait_for_selector('div[contenteditable="true"][role="textbox"]', timeout=15000)
                    textbox.fill(caption)
                    self.page.keyboard.press("Enter")
                    time.sleep(1.5)
                except:
                    self._logger.warning("Tidak bisa mengirim caption")

            # === Attach Button - Lebih Fleksibel ===
            attach_btn = None
            selectors = [
                'button[title="Attach"]',
                'button[aria-label="Attach"]',
                '//button[contains(@title, "Attach")]',
                'span[data-icon="attach-menu-plus"]',
                'div[role="button"] svg[data-icon="plus"]'  # fallback
            ]

            for selector in selectors:
                try:
                    attach_btn = self.page.wait_for_selector(selector, timeout=8000)
                    if attach_btn:
                        break
                except:
                    continue

            if not attach_btn:
                raise Exception("Tombol Attach tidak ditemukan. Pastikan chat sudah terbuka.")

            attach_btn.click()
            time.sleep(2)

            # Pilih "Document"
            document_option = self.page.wait_for_selector('span:has-text("Document")', timeout=10000)
            document_option.click()
            time.sleep(1.5)

            # Upload PDF
            file_input = self.page.wait_for_selector('input[type="file"]', timeout=10000)
            file_input.set_input_files(pdf_path)

            # Tunggu dan klik tombol Send
            send_btn = self.page.wait_for_selector('span[data-icon="send"]', timeout=20000)
            send_btn.click()

            time.sleep(4)   # Tunggu upload selesai

            self._logger.info(f"✅ PDF berhasil dikirim ke {clean_number}")
            return True

        except Exception as e:
            self._logger.error(f"Error saat kirim PDF: {e}")
            raise Exception(f"Gagal mengirim PDF: {str(e)}")
        finally:
            if temp_file and os.path.exists(temp_file):
                try:
                    os.remove(temp_file)
                except:
                    pass

    def _clean_number(self, nomor: str) -> str:
        nomor = str(nomor).strip().replace("+", "").replace(" ", "").replace("-", "")
        if nomor.startswith("0"):
            nomor = "62" + nomor[1:]
        elif not nomor.startswith("62"):
            nomor = "62" + nomor
        return nomor