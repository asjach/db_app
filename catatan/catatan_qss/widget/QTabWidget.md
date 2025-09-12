## SUB CONTROL
::left-corner
::pane
::right-corner
::tab-bar



QTabWidget{
  margin:
  padding:
  selection-background-color:
  background-color:
  }


  QTabWidget QWidget {}


QTabWidget::pane {
  background:
  border: 
  margin: 
  /* Fixes double border inside pane with pyqt5 */
  padding: 0px;
}

QTabWidget::pane:selected {
  background-color: #455364;
  border: 1px solid #346792;
}


QTabWidget::tab-bar {
    left: 0px;
}

