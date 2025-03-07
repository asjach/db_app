from PySide6.QtWidgets import QComboBox


def fill_combobox(ui_combo:QComboBox, values, *parameter):
    ui_combo.clear()
    ui_combo.addItems(values() if callable(values) else values)
    if parameter:
        ui_combo.addItems(values(parameter) if callable(values) else values)


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