## SUB CONTROL
::tab



QToolBox {
  padding: 0px;
  border: 0px;
  border: 1px solid #455364;
}

QToolBox:selected {
  padding: 0px;
  border: 2px solid #346792;
}

QToolBox::tab {
  background-color: #19232D;
  border: 1px solid #455364;
  color: #DFE1E2;
  border-top-left-radius: 4px;
  border-top-right-radius: 4px;
}

QToolBox::tab:disabled {
  color: #788D9C;
}

QToolBox::tab:selected {
  background-color: #60798B;
  border-bottom: 2px solid #346792;
}

QToolBox::tab:selected:disabled {
  background-color: #455364;
  border-bottom: 2px solid #26486B;
}

QToolBox::tab:!selected {
  background-color: #455364;
  border-bottom: 2px solid #455364;
}

QToolBox::tab:!selected:disabled {
  background-color: #19232D;
}

QToolBox::tab:hover {
  border-color: #1A72BB;
  border-bottom: 2px solid #1A72BB;
}

QToolBox QScrollArea {
  padding: 0px;
  border: 0px;
  background-color: #19232D;
}