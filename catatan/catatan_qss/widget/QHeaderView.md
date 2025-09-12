## PROPERTY
- box model


## SUB CONTROL
::down-arrow  indikator sort/urutan
::up-arrow
::section

## PSEUDO-STATE ::section
:middle
:first
:last
:only-one
:next-selected
:previous-selected
:selected
:checked


QHeaderView {
  background-color: #455364;
  border: 0px transparent #455364;
  padding: 0;
  margin: 0;
  border-radius: 0;
}

QHeaderView:disabled {
  background-color: #455364;
  border: 1px transparent #455364;
}

QHeaderView::section {
  background-color: #455364;
  color: #DFE1E2;
  border-radius: 0;
  text-align: left;
  font-size: 13px;
}

QHeaderView::section::horizontal {
  padding-top: 0;
  padding-bottom: 0;
  padding-left: 4px;
  padding-right: 4px;
  border-left: 1px solid #19232D;
}

QHeaderView::section::horizontal::first, QHeaderView::section::horizontal::only-one {
  border-left: 1px solid #455364;
}

QHeaderView::section::horizontal:disabled {
  color: #788D9C;
}

QHeaderView::section::vertical {
  padding-top: 0;
  padding-bottom: 0;
  padding-left: 4px;
  padding-right: 4px;
  border-top: 1px solid #19232D;
}

QHeaderView::section::vertical::first, QHeaderView::section::vertical::only-one {
  border-top: 1px solid #455364;
}

QHeaderView::section::vertical:disabled {
  color: #788D9C;
}

QHeaderView::down-arrow {
  /* Those settings (border/width/height/background-color) solve bug */
  /* transparent arrow background and size */
  background-color: #455364;
  border: none;
  height: 12px;
  width: 12px;
  padding-left: 2px;
  padding-right: 2px;
  image: url(":/qss_icons/dark/rc/arrow_down.png");
}

QHeaderView::up-arrow {
  background-color: #455364;
  border: none;
  height: 12px;
  width: 12px;
  padding-left: 2px;
  padding-right: 2px;
  image: url(":/qss_icons/dark/rc/arrow_up.png");
}
