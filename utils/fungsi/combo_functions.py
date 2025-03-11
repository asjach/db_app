from PySide6.QtWidgets import QComboBox


def fill_combobox(ui_combo:QComboBox, values, *parameter):
    ui_combo.clear()
    ui_combo.addItems(values() if callable(values) else values)
    if parameter:
        ui_combo.addItems(values(parameter) if callable(values) else values)


def populate_combobox(cbo_widget: QComboBox, data, text_data=None, user_data=None):
    """
    Mengisi QComboBox dengan data berdasarkan parameter yang diberikan.
    
    Args:
        cbo_widget (QComboBox): Widget QComboBox yang akan diisi.
        data: Data yang akan digunakan untuk mengisi QComboBox (list atau list of dict).
        text_data (str, optional): Kunci dalam dictionary untuk teks yang ditampilkan.
        user_data (str, optional): Kunci dalam dictionary untuk userData.
    """
    cbo_widget.clear()  # Bersihkan isi combobox sebelum menambahkan data baru
    if not data:  # Jika data kosong, langsung keluar
        return
    if not isinstance(data, list):
        raise TypeError(f"Expected a list or list of dict, got {type(data).__name__}")

    # Cek apakah data adalah list of dict
    is_list_of_dict = data and all(isinstance(item, dict) for item in data)

    if is_list_of_dict:
        if text_data is None:
            raise ValueError("text_data must be provided when data is a list of dict")
        
        for item in data:
            text = str(item.get(text_data, ''))  # Ambil teks dari kunci text_data, default ke string kosong
            if user_data is not None:
                # Jika user_data diberikan, tambahkan item dengan userData
                user_value = item.get(user_data, None)  # Ambil userData dari kunci user_data
                cbo_widget.addItem(text, user_value)
            else:
                # Jika hanya text_data yang diberikan, tambahkan item tanpa userData
                cbo_widget.addItem(text)
    else:
        # Jika data adalah list biasa, gunakan addItems
        cbo_widget.addItems([str(item) for item in data])


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