QAbstractSpinBox {
  background-color: #19232D;
  border: 1px solid #455364;
  color: #DFE1E2;
  /* This fixes 103, 111 */
  padding-top: 2px;
  /* This fixes 103, 111 */
  padding-bottom: 2px;
  padding-left: 4px;
  padding-right: 4px;
  border-radius: 4px;
  /* min-width: 5px; removed to fix 109 */
}

QAbstractSpinBox:up-button {
  background-color: transparent #19232D;
  subcontrol-origin: border;
  subcontrol-position: top right;
  border-left: 1px solid #455364;
  border-bottom: 1px solid #455364;
  border-top-left-radius: 0;
  border-bottom-left-radius: 0;
  margin: 1px;
  width: 12px;
  margin-bottom: -1px;
}

QAbstractSpinBox::up-arrow, QAbstractSpinBox::up-arrow:disabled, QAbstractSpinBox::up-arrow:off {
  image: url(":/qss_icons/dark/rc/arrow_up_disabled.png");
  height: 8px;
  width: 8px;
}

QAbstractSpinBox::up-arrow:hover {
  image: url(":/qss_icons/dark/rc/arrow_up.png");
}

QAbstractSpinBox:down-button {
  background-color: transparent #19232D;
  subcontrol-origin: border;
  subcontrol-position: bottom right;
  border-left: 1px solid #455364;
  border-top: 1px solid #455364;
  border-top-left-radius: 0;
  border-bottom-left-radius: 0;
  margin: 1px;
  width: 12px;
  margin-top: -1px;
}

QAbstractSpinBox::down-arrow, QAbstractSpinBox::down-arrow:disabled, QAbstractSpinBox::down-arrow:off {
  image: url(":/qss_icons/dark/rc/arrow_down_disabled.png");
  height: 8px;
  width: 8px;
}

QAbstractSpinBox::down-arrow:hover {
  image: url(":/qss_icons/dark/rc/arrow_down.png");
}

QAbstractSpinBox:hover {
  border: 1px solid #346792;
  color: #DFE1E2;
}

QAbstractSpinBox:focus {
  border: 1px solid #1A72BB;
}

QAbstractSpinBox:selected {
  background: #346792;
  color: #455364;
}