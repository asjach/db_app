import sys
from PySide6.QtWidgets import QApplication, QStyledItemDelegate, QProxyStyle, QComboBox
from PySide6.QtCore import Qt
from scripts.main import MainWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    QApplication.setStyle("Fusion")
    # centered_style = CenterTextProxyStyle(app.style())
    # app.setStyle(centered_style)
    window = MainWindow()
    # ThemeManager.apply_theme(app, "dark", "resources/style.qss")
    sys.exit(app.exec())
