from PySide6.QtWidgets import QComboBox, QListWidget
from PySide6.QtGui import QFontMetrics
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QStyledItemDelegate, QStyleOptionViewItem


# def fill_combobox(ui_combo:QComboBox, values, *parameter):
#     ui_combo.clear()
#     ui_combo.addItems(values() if callable(values) else values)
#     if parameter:
#         ui_combo.addItems(values(parameter) if callable(values) else values)

def populate_combobox(cbo_widget: QComboBox | QListWidget, data, text_data=None, user_data=None, separator='|', padding_pixels=20):
    """
    Fungsi untuk mengisi QComboBox atau QListWidget dengan teks yang rata dan padding antar kolom.
    :parameter
        cbo_widget      : nama combobox atau list widget
        data            : list string atau list of dict untuk ditampilkan di combobox
        text_data       : kunci tunggal (string) atau daftar kunci (list of strings) untuk teks
        user_data       : kunci tunggal (string) atau daftar kunci (list of strings) untuk userData
        separator       : pemisah untuk teks jika text_data adalah list (hanya string, misalnya '|')
        padding_pixels  : jumlah piksel untuk padding tambahan per kolom (default: 10)
    """
    cbo_widget.clear() 
    if not data: 
        return
    if not isinstance(data, list):
        raise TypeError(f"Expected a list or list of dict, got {type(data).__name__}")
    if not isinstance(separator, str):
        raise TypeError("separator must be a string")
    font_metrics = QFontMetrics(cbo_widget.font())
    space_width = font_metrics.horizontalAdvance(' ')
    is_list_of_dict = data and all(isinstance(item, dict) for item in data)
    if is_list_of_dict:
        if text_data is None:
            raise ValueError("text_data must be provided when data is a list of dict")
        max_widths_pixels = None
        if isinstance(text_data, list):
            max_widths_pixels = [0] * len(text_data)
            for item in data:
                text_values = [item.get(key, '') for key in text_data]
                text_values = ['' if value is None else str(value) for value in text_values]
                for i, value in enumerate(text_values):
                    text_width = font_metrics.horizontalAdvance(value)
                    max_widths_pixels[i] = max(max_widths_pixels[i], text_width + padding_pixels)
        for item in data:
            if isinstance(text_data, str):
                text_value = item.get(text_data, '')
                text = '' if text_value is None else str(text_value)
            elif isinstance(text_data, list):
                text_values = [item.get(key, '') for key in text_data]
                text_values = ['' if value is None else str(value) for value in text_values]
                formatted_values = []
                for i, value in enumerate(text_values):
                    text_width = font_metrics.horizontalAdvance(value)
                    padding_pixels_total = max_widths_pixels[i] - text_width
                    padding_spaces = max(0, padding_pixels_total // space_width)
                    formatted_values.append(value + ' ' * padding_spaces)
                text = f' {separator} '.join(formatted_values)
            else:
                raise TypeError("text_data must be a string or list of strings")

            if user_data is not None:
                if isinstance(user_data, str):
                    user_value = item.get(user_data, None)
                elif isinstance(user_data, list):
                    user_value = {key: item.get(key, None) for key in user_data}
                else:
                    raise TypeError("user_data must be a string or list of strings")
                cbo_widget.addItem(text, user_value)
            else:
                cbo_widget.addItem(text)
    else:
        cbo_widget.addItems(['' if item is None else str(item) for item in data])


def next_item(combobox):
    current_index = combobox.currentIndex()
    if current_index == combobox.count() - 1:
        combobox.setCurrentIndex(0)
    else:
        combobox.setCurrentIndex(current_index + 1)


def prev_item(combobox):
    current_index = combobox.currentIndex()
    if current_index <= 0:
        combobox.setCurrentIndex(combobox.count() - 1)
    else:
        combobox.setCurrentIndex(current_index - 1)


def fungsi_filter_buttons(combo_box=None, prev_button=None, next_button=None, clear_button=None):
    if prev_button:
        prev_button.clicked.connect(lambda: prev_item(combobox=combo_box))
    if next_button:
        next_button.clicked.connect(lambda: next_item(combobox=combo_box))
    if clear_button:
        combo_box.setEditable(True)
        clear_button.clicked.connect(lambda: combo_box.setCurrentIndex(-1))
        combo_box.lineEdit().setReadOnly(True)
        combo_box.setEditable(False)
    else:
        pass


def centerize_combo(combo):
    # from PySide6.QtWidgets import QStyledItemDelegate, QStyleOptionViewItem
    class CenteredDelegate(QStyledItemDelegate):
        def initStyleOption(self, option: QStyleOptionViewItem, index):
            super().initStyleOption(option, index)
            option.displayAlignment = Qt.AlignCenter

    combo.setItemDelegate(CenteredDelegate(combo))
    combo.setEditable(True)
    combo.lineEdit().setAlignment(Qt.AlignCenter)
    combo.lineEdit().setReadOnly(True)

def left_combo(combo):
    # from PySide6.QtWidgets import QStyledItemDelegate, QStyleOptionViewItem
    class CenteredDelegate(QStyledItemDelegate):
        def initStyleOption(self, option: QStyleOptionViewItem, index):
            super().initStyleOption(option, index)
            option.displayAlignment = Qt.AlignLeft | Qt.AlignVCenter
            

    combo.setItemDelegate(CenteredDelegate(combo))
    combo.setEditable(True)
    combo.lineEdit().setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
    combo.lineEdit().setReadOnly(True)