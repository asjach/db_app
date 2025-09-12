# PROPERTY
- box model
- spacing



# SUB CONTROL
::indicator






QRadioButton {
  background-color: #19232D;
  color: #DFE1E2;
  spacing: 4px;
  padding-top: 4px;
  padding-bottom: 4px;
  border: none;
  outline: none;
}

QRadioButton:focus {
  border: none;
}

QRadioButton:disabled {
  background-color: #19232D;
  color: #788D9C;
  border: none;
  outline: none;
}

QRadioButton QWidget {
  background-color: #19232D;
  color: #DFE1E2;
  spacing: 0px;
  padding: 0px;
  outline: none;
  border: none;
}

QRadioButton::indicator {
  border: none;
  outline: none;
  margin-left: 2px;
  height: 14px;
  width: 14px;
}

QRadioButton::indicator::unchecked {
  image: url(":/qss_icons/dark/rc/radio_unchecked.png");
}

QRadioButton::indicator:unchecked:hover, 
QRadioButton::indicator:unchecked:focus, 
QRadioButton::indicator:unchecked:pressed {
  border: none;
  outline: none;
  image: url(":/qss_icons/dark/rc/radio_unchecked_focus.png");
}

QRadioButton::indicator:unchecked:disabled {
  image: url(":/qss_icons/dark/rc/radio_unchecked_disabled.png");
}

QRadioButton::indicator::checked {
  border: none;
  outline: none;
  image: url(":/qss_icons/dark/rc/radio_checked.png");
}

QRadioButton::indicator:checked:hover, 
QRadioButton::indicator:checked:focus, 
QRadioButton::indicator:checked:pressed {
  border: none;
  outline: none;
  image: url(":/qss_icons/dark/rc/radio_checked_focus.png");
}

QRadioButton::indicator:checked:disabled {
  outline: none;
  image: url(":/qss_icons/dark/rc/radio_checked_disabled.png");
}


QRadioButton::indicator:!checked{}