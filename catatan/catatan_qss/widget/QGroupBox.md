# PROPERTY
  - box model
  - spacing


# SUB CONTROL
::indicator    ketika checkable
::title




QGroupBox {
  font-weight: bold;
  border: 1px solid #455364;
  border-radius: 4px;
  padding: 2px;
  margin-top: 6px;
  margin-bottom: 4px;
}

QGroupBox::title {
  subcontrol-origin: margin;
  subcontrol-position: top left;
  left: 4px;
  padding-left: 2px;
  padding-right: 4px;
  padding-top: -4px;
}

QGroupBox::indicator {
  margin-left: 2px;
  margin-top: 2px;
  padding: 0;
  height: 14px;
  width: 14px;
}

QGroupBox::indicator:unchecked {
  border: none;
  image: url(":/qss_icons/dark/rc/checkbox_unchecked.png");
}

QGroupBox::indicator:unchecked:hover, QGroupBox::indicator:unchecked:focus, QGroupBox::indicator:unchecked:pressed {
  border: none;
  image: url(":/qss_icons/dark/rc/checkbox_unchecked_focus.png");
}

QGroupBox::indicator:unchecked:disabled {
  image: url(":/qss_icons/dark/rc/checkbox_unchecked_disabled.png");
}

QGroupBox::indicator:checked {
  border: none;
  image: url(":/qss_icons/dark/rc/checkbox_checked.png");
}

QGroupBox::indicator:checked:hover, QGroupBox::indicator:checked:focus, QGroupBox::indicator:checked:pressed {
  border: none;
  image: url(":/qss_icons/dark/rc/checkbox_checked_focus.png");
}

QGroupBox::indicator:checked:disabled {
  image: url(":/qss_icons/dark/rc/checkbox_checked_disabled.png");
}