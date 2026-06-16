import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

path = r"G:\Surat Undangan Rapat Evaluasi TPA Al-Kautsar 2025.pdf"
nomor = "62881022647247"

def kirim_file_wa(nomor, path_file):
    url = f"https://web.whatsapp.com/send?phone={nomor}&text=&app_absent=0"

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.get(url)
    time.sleep(15)  # tunggu scan QR

    # klik tombol attachment (clip)
    attach = driver.find_element(By.XPATH, "//span[@data-icon='plus']")
    attach.click()
    time.sleep(1)

    # input file
    file_input = driver.find_element(By.XPATH, "//input[@type='file']")
    file_input.send_keys(path_file)

    time.sleep(2)

    # klik tombol kirim
    send_btn = driver.find_element(By.XPATH, "//span[@data-icon='send']")
    send_btn.click()

    time.sleep(5)
    driver.quit()
