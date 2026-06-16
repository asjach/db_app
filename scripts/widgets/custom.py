from PySide6.QtWidgets import QPlainTextEdit
from PySide6.QtCore import QDataStream, Qt, QByteArray

class DropPlainTextEdit(QPlainTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasFormat("application/x-qabstractitemmodeldatalist"):
            event.acceptProposedAction()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasFormat("application/x-qabstractitemmodeldatalist"):
            event.acceptProposedAction()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasFormat("application/x-qabstractitemmodeldatalist"):
            data = event.mimeData().data("application/x-qabstractitemmodeldatalist")
            stream = QDataStream(data, QDataStream.ReadOnly)

            while not stream.atEnd():
                row = stream.readInt32()
                column = stream.readInt32()
                map_items = stream.readInt32()
                for _ in range(map_items):
                    role = stream.readInt32()
                    value = stream.readQVariant()
                    if role == Qt.DisplayRole:
                        cursor = self.textCursor()
                        cursor.insertText(", " + str(value))   # sisipkan di posisi kursor
            event.acceptProposedAction()
        else:
            event.ignore()
