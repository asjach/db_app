# PROPERTY
- box model



# SUB CONTROL
::indicator   checkable QMenu Item
::icon
::item
::right-arrow
::scroller
::separator
::tearoff


# PSEUDO-STATE
::item
  :selected
  :default
  :exclusive
  :non-exclusive
  




QMenu {
  border:
  color: 
  margin: 
  background-color: 
  selection-background-color: 
}

QMenu::separator {
  height: 1px;
  background-color: #60798B;
  color: #DFE1E2;
}

QMenu::item {
  background-color: #37414F;
  padding: 4px 24px 4px 28px;
  /* Reserve space for selection border */
  border: 1px transparent #455364;
}

QMenu::item:selected {
  color: #DFE1E2;
  background-color: #1A72BB;
}

QMenu::item:pressed {
  background-color: #1A72BB;
}

QMenu::icon {
  padding-left: 10px;
  width: 14px;
  height: 14px;
}

QMenu::indicator {
  padding-left: 8px;
  width: 12px;
  height: 12px;
  /* non-exclusive indicator = check box style indicator (see QActionGroup::setExclusive) */
  /* exclusive indicator = radio button style indicator (see QActionGroup::setExclusive) */
}

QMenu::indicator:non-exclusive:unchecked {
  image: url(":/qss_icons/dark/rc/checkbox_unchecked.png");
}

QMenu::indicator:non-exclusive:unchecked:hover, QMenu::indicator:non-exclusive:unchecked:focus, QMenu::indicator:non-exclusive:unchecked:pressed {
  border: none;
  image: url(":/qss_icons/dark/rc/checkbox_unchecked_focus.png");
}

QMenu::indicator:non-exclusive:unchecked:disabled {
  image: url(":/qss_icons/dark/rc/checkbox_unchecked_disabled.png");
}

QMenu::indicator:non-exclusive:checked {
  image: url(":/qss_icons/dark/rc/checkbox_checked.png");
}

QMenu::indicator:non-exclusive:checked:hover, QMenu::indicator:non-exclusive:checked:focus, QMenu::indicator:non-exclusive:checked:pressed {
  border: none;
  image: url(":/qss_icons/dark/rc/checkbox_checked_focus.png");
}

QMenu::indicator:non-exclusive:checked:disabled {
  image: url(":/qss_icons/dark/rc/checkbox_checked_disabled.png");
}

QMenu::indicator:non-exclusive:indeterminate {
  image: url(":/qss_icons/dark/rc/checkbox_indeterminate.png");
}

QMenu::indicator:non-exclusive:indeterminate:disabled {
  image: url(":/qss_icons/dark/rc/checkbox_indeterminate_disabled.png");
}

QMenu::indicator:non-exclusive:indeterminate:focus, QMenu::indicator:non-exclusive:indeterminate:hover, QMenu::indicator:non-exclusive:indeterminate:pressed {
  image: url(":/qss_icons/dark/rc/checkbox_indeterminate_focus.png");
}

QMenu::indicator:exclusive:unchecked {
  image: url(":/qss_icons/dark/rc/radio_unchecked.png");
}

QMenu::indicator:exclusive:unchecked:hover, QMenu::indicator:exclusive:unchecked:focus, QMenu::indicator:exclusive:unchecked:pressed {
  border: none;
  outline: none;
  image: url(":/qss_icons/dark/rc/radio_unchecked_focus.png");
}

QMenu::indicator:exclusive:unchecked:disabled {
  image: url(":/qss_icons/dark/rc/radio_unchecked_disabled.png");
}

QMenu::indicator:exclusive:checked {
  border: none;
  outline: none;
  image: url(":/qss_icons/dark/rc/radio_checked.png");
}

QMenu::indicator:exclusive:checked:hover, QMenu::indicator:exclusive:checked:focus, QMenu::indicator:exclusive:checked:pressed {
  border: none;
  outline: none;
  image: url(":/qss_icons/dark/rc/radio_checked_focus.png");
}

QMenu::indicator:exclusive:checked:disabled {
  outline: none;
  image: url(":/qss_icons/dark/rc/radio_checked_disabled.png");
}

QMenu::right-arrow {
  margin: 5px;
  padding-left: 12px;
  image: url(":/qss_icons/dark/rc/arrow_right.png");
  height: 12px;
  width: 12px;
}