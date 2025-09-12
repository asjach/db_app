# PROPERTY
  - lihat QSpinBox



QDateEdit, QDateTimeEdit {
  selection-background-color: #346792;
  border-style: solid;
  border: 1px solid #455364;
  border-radius: 4px;
  /* This fixes 103, 111 */
  padding-top: 2px;
  /* This fixes 103, 111 */
  padding-bottom: 2px;
  padding-left: 4px;
  padding-right: 4px;
  min-width: 10px;
}

QDateEdit:on, 
QDateTimeEdit:on {
  selection-background-color: #346792;
}

QDateEdit::drop-down, 
QDateTimeEdit::drop-down {
  subcontrol-origin: padding;
  subcontrol-position: top right;
  width: 12px;
  border-left: 1px solid #455364;
}

QDateEdit::down-arrow, 
QDateTimeEdit::down-arrow {
  image: url(":/qss_icons/dark/rc/arrow_down_disabled.png");
  height: 8px;
  width: 8px;
}

QDateEdit::down-arrow:on, 
QDateEdit::down-arrow:hover, 
QDateEdit::down-arrow:focus, 
QDateTimeEdit::down-arrow:on, 
QDateTimeEdit::down-arrow:hover, 
QDateTimeEdit::down-arrow:focus {
  image: url(":/qss_icons/dark/rc/arrow_down.png");
}

QDateEdit QAbstractItemView, 
QDateTimeEdit QAbstractItemView {
  background-color: #19232D;
  border-radius: 4px;
  border: 1px solid #455364;
  selection-background-color: #346792;
}