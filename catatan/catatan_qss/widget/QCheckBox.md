# 

# PROPERTY
  - box model
  - spacing



# SUB CONTROL
::indicator



QCheckBox {
  background:;
  color: 
  spacing: 4px;
  outline: none;
  padding:

}

QCheckBox:focus {}
QCheckBox:hover
QCheckBox:disabled {}
QCheckBox QWidget:disabled {}
QCheckBox:disabled
QCheckBox::indicator {
  background:
  border:
  padding:
  margin: 
  height: 
  width: 
}

QCheckBox::indicator:checked {
  image: url(":/qss_icons/dark/rc/checkbox_checked.png");
}

QCheckBox::indicator:checked:hover, 
QCheckBox::indicator:checked:focus, 
QCheckBox::indicator:checked:pressed {
  border: none;
  image: url(":/qss_icons/dark/rc/checkbox_checked_focus.png");
}
QCheckBox::indicator:unchecked {
  image: url(":/qss_icons/dark/rc/checkbox_unchecked.png");
}

QCheckBox::indicator:unchecked:hover, 
QCheckBox::indicator:unchecked:focus, 
QCheckBox::indicator:unchecked:pressed {
  border: none;
  image: url(":/qss_icons/dark/rc/checkbox_unchecked_focus.png");
}

QCheckBox::indicator:unchecked:disabled {
  image: url(":/qss_icons/dark/rc/checkbox_unchecked_disabled.png");
}

QCheckBox::indicator:checked:disabled {
  image: url(":/qss_icons/dark/rc/checkbox_checked_disabled.png");
}

QCheckBox::indicator:indeterminate {
  image: url(":/qss_icons/dark/rc/checkbox_indeterminate.png");
}

QCheckBox::indicator:indeterminate:disabled {
  image: url(":/qss_icons/dark/rc/checkbox_indeterminate_disabled.png");
}

QCheckBox::indicator:indeterminate:focus, 
QCheckBox::indicator:indeterminate:hover, 
QCheckBox::indicator:indeterminate:pressed {
  image: url(":/qss_icons/dark/rc/checkbox_indeterminate_focus.png");
}