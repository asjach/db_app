## SUB-CONTROL
::branch      indikator cabang pada TreeView




QTreeView:branch:selected, QTreeView:branch:hover {
  background: url(":/qss_icons/dark/rc/transparent.png");
}

QTreeView:branch:has-siblings:!adjoins-item {
  border-image: url(":/qss_icons/dark/rc/branch_line.png") 0;
}

QTreeView:branch:has-siblings:adjoins-item {
  border-image: url(":/qss_icons/dark/rc/branch_more.png") 0;
}

QTreeView:branch:!has-children:!has-siblings:adjoins-item {
  border-image: url(":/qss_icons/dark/rc/branch_end.png") 0;
}

QTreeView:branch:has-children:!has-siblings:closed, QTreeView:branch:closed:has-children:has-siblings {
  border-image: none;
  image: url(":/qss_icons/dark/rc/branch_closed.png");
}

QTreeView:branch:open:has-children:!has-siblings, QTreeView:branch:open:has-children:has-siblings {
  border-image: none;
  image: url(":/qss_icons/dark/rc/branch_open.png");
}

QTreeView:branch:has-children:!has-siblings:closed:hover, QTreeView:branch:closed:has-children:has-siblings:hover {
  image: url(":/qss_icons/dark/rc/branch_closed_focus.png");
}

QTreeView:branch:open:has-children:!has-siblings:hover, QTreeView:branch:open:has-children:has-siblings:hover {
  image: url(":/qss_icons/dark/rc/branch_open_focus.png");
}



QTreeView::indicator:checked,
QListView::indicator:checked,
QTableView::indicator:checked,
QColumnView::indicator:checked {
  image: url(":/qss_icons/dark/rc/checkbox_checked.png");
}

QTreeView::indicator:checked:hover, QTreeView::indicator:checked:focus, QTreeView::indicator:checked:pressed,
QListView::indicator:checked:hover,
QListView::indicator:checked:focus,
QListView::indicator:checked:pressed,
QTableView::indicator:checked:hover,
QTableView::indicator:checked:focus,
QTableView::indicator:checked:pressed,
QColumnView::indicator:checked:hover,
QColumnView::indicator:checked:focus,
QColumnView::indicator:checked:pressed {
  image: url(":/qss_icons/dark/rc/checkbox_checked_focus.png");
}

QTreeView::indicator:unchecked,
QListView::indicator:unchecked,
QTableView::indicator:unchecked,
QColumnView::indicator:unchecked {
  image: url(":/qss_icons/dark/rc/checkbox_unchecked.png");
}

QTreeView::indicator:unchecked:hover, QTreeView::indicator:unchecked:focus, QTreeView::indicator:unchecked:pressed,
QListView::indicator:unchecked:hover,
QListView::indicator:unchecked:focus,
QListView::indicator:unchecked:pressed,
QTableView::indicator:unchecked:hover,
QTableView::indicator:unchecked:focus,
QTableView::indicator:unchecked:pressed,
QColumnView::indicator:unchecked:hover,
QColumnView::indicator:unchecked:focus,
QColumnView::indicator:unchecked:pressed {
  image: url(":/qss_icons/dark/rc/checkbox_unchecked_focus.png");
}

QTreeView::indicator:indeterminate,
QListView::indicator:indeterminate,
QTableView::indicator:indeterminate,
QColumnView::indicator:indeterminate {
  image: url(":/qss_icons/dark/rc/checkbox_indeterminate.png");
}

QTreeView::indicator:indeterminate:hover, QTreeView::indicator:indeterminate:focus, QTreeView::indicator:indeterminate:pressed,
QListView::indicator:indeterminate:hover,
QListView::indicator:indeterminate:focus,
QListView::indicator:indeterminate:pressed,
QTableView::indicator:indeterminate:hover,
QTableView::indicator:indeterminate:focus,
QTableView::indicator:indeterminate:pressed,
QColumnView::indicator:indeterminate:hover,
QColumnView::indicator:indeterminate:focus,
QColumnView::indicator:indeterminate:pressed {
  image: url(":/qss_icons/dark/rc/checkbox_indeterminate_focus.png");
}

QTreeView,
QListView,
QTableView,
QColumnView {
  background-color: #19232D;
  border: 1px solid #455364;
  color: #DFE1E2;
  gridline-color: #455364;
  border-radius: 4px;
}

QTreeView:disabled,
QListView:disabled,
QTableView:disabled,
QColumnView:disabled {
  background-color: #19232D;
  color: #788D9C;
}

QTreeView:selected,
QListView:selected,
QTableView:selected,
QColumnView:selected {
  background-color: #346792;
  color: #455364;
}

QTreeView:focus,
QListView:focus,
QTableView:focus,
QColumnView:focus {
  border: 1px solid #1A72BB;
}

QTreeView::item:pressed,
QListView::item:pressed,
QTableView::item:pressed,
QColumnView::item:pressed {
  background-color: #346792;
}

QTreeView::item:selected:active,
QListView::item:selected:active,
QTableView::item:selected:active,
QColumnView::item:selected:active {
  background-color: #346792;
}

QTreeView::item:selected:!active,
QListView::item:selected:!active,
QTableView::item:selected:!active,
QColumnView::item:selected:!active {
  color: #DFE1E2;
  background-color: #37414F;
}

QTreeView::item:!selected:hover,
QListView::item:!selected:hover,
QTableView::item:!selected:hover,
QColumnView::item:!selected:hover {
  outline: 0;
  color: #DFE1E2;
  background-color: #37414F;
}

QTableCornerButton::section {
  background-color: #19232D;
  border: 1px transparent #455364;
  border-radius: 0px;
}
