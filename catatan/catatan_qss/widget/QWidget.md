/* QWidget ----------------------------------------------------------------

--------------------------------------------------------------------------- */
QWidget {
  background-color: #19232D;
  border: 0px solid #455364;
  padding: 0px;
  color: #DFE1E2;
  selection-background-color: #346792;
  selection-color: #DFE1E2;
}

QWidget:disabled {
  background-color: #19232D;
  color: #788D9C;
  selection-background-color: #26486B;
  selection-color: #788D9C;
}

QWidget::item:selected {
  background-color: #346792;
}

QWidget::item:hover:!selected {
  background-color: #1A72BB;
}
