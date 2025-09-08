from PySide6.QtWidgets import QListWidget, QListWidgetItem, QStyledItemDelegate, QStyleOptionViewItem
from PySide6.QtCore import Qt

def populate_list_widget(
        list_widget: QListWidget,
        data,
        set_check=True,
        show_check=False,
        display_key=None,
        data_key=None
    ):
    """
    Populate QListWidget with various data formats:
    - List: Simple values (text = value, no user data)
    - Dict: Uses values as text (no user data)
    - List of Dicts: Uses display_key for text and data_key for user data
    
    Args:
        list_widget: Target QListWidget
        data: Input data (list, dict, or list of dicts)
        set_check: Set items checked by default
        show_check: Show checkboxes
        display_key: Key for display text (for list of dicts)
        data_key: Key for user data (for list of dicts)
    """
    list_widget.blockSignals(True)
    list_widget.clear()

    if not data:
        list_widget.blockSignals(False)
        return

    # Handle single dictionary input (values as text, no user data)
    if isinstance(data, dict):
        if display_key or data_key:
            raise ValueError("For dictionary input, display_key and data_key should not be specified")
        
        for value in data.values():
            item = QListWidgetItem(str(value), list_widget)
            _set_check_state(item, show_check, set_check)
        
        list_widget.blockSignals(False)
        return

    # Handle list input
    if isinstance(data, (list, tuple)):
        # Handle list of dictionaries
        if data and all(isinstance(item, dict) for item in data):
            if not display_key:
                raise ValueError("display_key must be specified for list of dictionaries")
            
            for item_data in data:
                text = str(item_data.get(display_key, ''))
                item = QListWidgetItem(text, list_widget)
                
                if data_key:
                    user_data = item_data.get(data_key)
                    if user_data is not None:
                        item.setData(Qt.UserRole, user_data)
                
                _set_check_state(item, show_check, set_check)
        
        # Handle simple list
        else:
            if display_key or data_key:
                raise ValueError("For simple list input, display_key and data_key should not be specified")
            
            for value in data:
                item = QListWidgetItem(str(value), list_widget)
                _set_check_state(item, show_check, set_check)
        
        list_widget.blockSignals(False)
        return

    raise ValueError("Unsupported data type. Expected list, dict, or list of dicts")


def _set_check_state(item, show_check, set_check):
    """Helper function to set checkbox state"""
    if show_check:
        item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
        item.setCheckState(Qt.Checked if set_check else Qt.Unchecked)

def get_list_widget_items(list_widget: QListWidget, opsi: str = 'list') -> list | str:
    """
        opsi (str): Output format option. Can be:
            'list'        : Returns list of items [1, 2, 3, ...]
            'quoted'  : Returns string with quoted items "'1', '2', '3', ..."
            'not_quoted'  : Returns string with items "1, 2, 3, ..."
    """
    items = [list_widget.item(index).text() for index in range(list_widget.count()) if list_widget.item(index)]
    if opsi == 'quoted':
        return ", ".join(f"'{item}'" for item in items)
    elif opsi == 'not_quoted':
        return ", ".join(str(item) for item in items)
    return items

def get_selected_list_widget_items(list_widget: QListWidget, opsi: str = 'list') -> list | str:
    """
        opsi (str): Output format option. Can be:
            'list'        : Returns list of selected items [1, 2, 3, ...]
            'quoted'  : Returns string with quoted selected items "'1', '2', '3', ..."
            'not_quoted'  : Returns string with selected items "1, 2, 3, ..."
    """
    items = [item.text() for item in list_widget.selectedItems()]

    if opsi == 'quoted':
        return ", ".join(f"'{item.strip()}'" for item in items)
    elif opsi == 'not_quoted':
        return ", ".join(str(item.strip()) for item in items)
    return items

def get_selected_list_widget_item(list_widget: QListWidget, opsi: str = 'quoted') -> str:
    item = list_widget.currentItem()
    if item:
        if opsi == 'quoted':
            return f"'{item.text().strip()}'"
        else:
            return item.text().strip()
        
def get_selected_list_widget_data(list_widget: QListWidget, opsi: str = None) -> str:
    item = list_widget.currentItem()
    if item:
        if opsi == 'quoted':
            return f"'{item.data(Qt.UserRole)}'"
        else:
            return item.data(Qt.UserRole)

# def get_list_widget_items(list_widget: QListWidget, checked=None, return_type='text') -> list:
#     if return_type not in ['text', 'data']:
#         raise ValueError("return_type harus 'text' atau 'data'")
    
#     items = []
#     for index in range(list_widget.count()):
#         item = list_widget.item(index)
#         if item:
#             if checked is None:
#                 items.append(item.text() if return_type == 'text' else item.data(Qt.UserRole))
#             elif checked is True and item.checkState() == Qt.Checked:
#                 items.append(item.text() if return_type == 'text' else item.data(Qt.UserRole))
#             elif checked is False and item.checkState() == Qt.Unchecked:
#                 items.append(item.text() if return_type == 'text' else item.data(Qt.UserRole))
#     return items


def toggle_list_widget_state(list_widget: QListWidget, state: bool):
    for index in range(list_widget.count()):
        item = list_widget.item(index)
        if item:  # Pastikan item tidak None
            if state:
                item.setCheckState(Qt.Checked)
            else:
                item.setCheckState(Qt.Unchecked)

    

class CenteredDelegate(QStyledItemDelegate):
    def initStyleOption(self, option: QStyleOptionViewItem, index):
        super().initStyleOption(option, index)
        option.displayAlignment = Qt.AlignCenter