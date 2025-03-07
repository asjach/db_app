import sys
from PySide6.QtWidgets import QApplication, QStyledItemDelegate, QProxyStyle, QComboBox
from PySide6.QtCore import Qt
from scripts.main import MainWindow


class CenteredItemDelegate(QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super().initStyleOption(option, index)
        option.displayAlignment = Qt.AlignLeft

    def sizeHint(self, option, index):
        size = super().sizeHint(option, index)
        size.setHeight(24)  # Set the desired height for each item
        return size
    
class CenterTextProxyStyle(QProxyStyle):
    def drawItemText(self, painter, rect, flags, pal, enabled, text, textRole):
        flags |= Qt.AlignCenter
        super().drawItemText(painter, rect, flags, pal, enabled, text, textRole)
    def polish(self, widget):
        super().polish(widget)
        if isinstance(widget, QComboBox):
            delegate = CenteredItemDelegate(widget)
            widget.setItemDelegate(delegate)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    QApplication.setStyle("Fusion")
    # centered_style = CenterTextProxyStyle(app.style())
    # app.setStyle(centered_style)
    window = MainWindow()
    sys.exit(app.exec())
