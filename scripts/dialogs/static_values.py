from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog
from ui.ui_dialog_static_values import Ui_Form
from PySide6.QtGui import QFont
import json
import os

class Dialog_Static_Values(QDialog, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(Qt.Window | Qt.WindowMinMaxButtonsHint | Qt.WindowCloseButtonHint)
        self.setWindowState(Qt.WindowMaximized)
        # self.setSizeGripEnabled(True)
        # self.plain_static_values.setFont(QFont("Courier New", 10))  # Font monospace untuk tampilan rapi
        self.open_json_file()
        self.btn_simpan.clicked.connect(self.save_json_file)
        self.btn_batal.clicked.connect(self.close)

    def open_json_file(self):
        BASE_DIR = "D:/APP/DB App"
        json_path = os.path.join(BASE_DIR, "utils", "static_values.json")
        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            formatted_text = self.format_json(data)
            self.plain_static_values.setPlainText(formatted_text)
        except FileNotFoundError:
            error_msg = f"File {json_path} tidak ditemukan. Membuat file baru..."
            default_data = {
                "AGAMA": ["", "Islam", "Katolik", "Protestan", "Hindu", "Budha", "Konghuchu"],
                "RIGHT_COLUMN": ["harga"],
                "KETERANGAN": {
                    "Formulir": ["", "Pendaftaran"],
                    "Kartu Keluarga": [""]
                }
            }
            os.makedirs(os.path.dirname(json_path), exist_ok=True)
            with open(json_path, 'w', encoding='utf-8') as f:
                json.dump(default_data, f, indent=2, ensure_ascii=False)
            formatted_text = self.format_json(default_data)
            self.plain_static_values.setPlainText(formatted_text)
            print(error_msg)
        except json.JSONDecodeError as e:
            error_msg = f"JSON tidak valid: {str(e)}"
            self.plain_static_values.setPlainText(error_msg)
            print(error_msg)
        except Exception as e:
            error_msg = f"Error membaca JSON: {str(e)}"
            self.plain_static_values.setPlainText(error_msg)
            print(error_msg)

    def format_json(self, data, indent=0):
        """Format JSON dengan indentasi 5 spasi per level, persis seperti JSON asli."""
        def custom_dumps(obj, indent_level):
            indent_str = " " * 5 * indent_level
            if isinstance(obj, dict):
                if not obj:
                    return "{}"
                items = []
                for key, value in obj.items():
                    formatted_value = custom_dumps(value, indent_level + 1)
                    items.append(f'{indent_str}     "{key}": {formatted_value}')
                return "{\n" + ",\n".join(items) + f"\n{indent_str}}}"
            elif isinstance(obj, list):
                if not obj:
                    return "[]"
                return json.dumps(obj, ensure_ascii=False)
            else:
                return json.dumps(obj, ensure_ascii=False)
        return custom_dumps(data, indent)

    def save_json_file(self):
        json_path = os.path.join("D:/APP/DB App", "utils", "static_values.json")
        try:
            text = self.plain_static_values.toPlainText()
            data = json.loads(text)  # Validasi teks sebagai JSON
            with open(json_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            print("JSON berhasil disimpan")
            self.accept()
        except json.JSONDecodeError as e:
            error_msg = f"Error: Teks bukan JSON yang valid: {str(e)}\nTeks: {text}"
            self.plain_static_values.setPlainText(error_msg)
            print(error_msg)
        except Exception as e:
            error_msg = f"Error menyimpan JSON: {str(e)}"
            self.plain_static_values.setPlainText(error_msg)
            print(error_msg)