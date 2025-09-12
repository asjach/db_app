## SUB CONTROL
::menu-arrow
::menu-button


QToolButton {
  background-color: #455364;
  color: #DFE1E2;
  border-radius: 4px;
  padding: 2px;
  outline: none;
  border: none;
  /* The subcontrols below are used only in the DelayedPopup mode */
  /* The subcontrols below are used only in the MenuButtonPopup mode */
  /* The subcontrol below is used only in the InstantPopup or DelayedPopup mode */
}

QToolButton:disabled {
  background-color: #455364;
  color: #788D9C;
  border-radius: 4px;
  padding: 2px;
}

QToolButton:checked {
  background-color: #60798B;
  border-radius: 4px;
  padding: 2px;
  outline: none;
}

QToolButton:checked:disabled {
  background-color: #60798B;
  color: #788D9C;
  border-radius: 4px;
  padding: 2px;
  outline: none;
}

QToolButton:checked:hover {
  background-color: #54687A;
  color: #DFE1E2;
}

QToolButton:checked:pressed {
  background-color: #60798B;
}

QToolButton:checked:selected {
  background: #60798B;
  color: #DFE1E2;
}

QToolButton:hover {
  background-color: #54687A;
  color: #DFE1E2;
}

QToolButton:pressed {
  background-color: #60798B;
}

QToolButton:selected {
  background: #60798B;
  color: #DFE1E2;
}

QToolButton[popupMode="0"] {
  /* Only for DelayedPopup */
  padding-right: 2px;
}

QToolButton[popupMode="1"] {
  /* Only for MenuButtonPopup */
  padding-right: 20px;
}

QToolButton[popupMode="1"]::menu-button {
  border: none;
}

QToolButton[popupMode="1"]::menu-button:hover {
  border: none;
  border-left: 1px solid #455364;
  border-radius: 0;
}

QToolButton[popupMode="2"] {
  /* Only for InstantPopup */
  padding-right: 2px;
}

QToolButton::menu-button {
  padding: 2px;
  border-radius: 4px;
  width: 12px;
  border: none;
  outline: none;
}

QToolButton::menu-button:hover {
  border: 1px solid #346792;
}

QToolButton::menu-button:checked:hover {
  border: 1px solid #346792;
}

QToolButton::menu-indicator {
  image: url(":/qss_icons/dark/rc/arrow_down.png");
  height: 8px;
  width: 8px;
  top: 0;
  /* Exclude a shift for better image */
  left: -2px;
  /* Shift it a bit */
}

QToolButton::menu-arrow {
  image: url(":/qss_icons/dark/rc/arrow_down.png");
  height: 8px;
  width: 8px;
}

QToolButton::menu-arrow:hover {
  image: url(":/qss_icons/dark/rc/arrow_down_focus.png");
}