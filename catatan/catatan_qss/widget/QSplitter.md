## SUB CONTROL
::handle



QSplitter {
  background-color: #455364;
  spacing: 0px;
  padding: 0px;
  margin: 0px;
}

QSplitter::handle {
  background-color: #455364;
  border: 0px solid #19232D;
  spacing: 0px;
  padding: 1px;
  margin: 0px;
}

QSplitter::handle:hover {
  background-color: #9DA9B5;
}

QSplitter::handle:horizontal {
  width: 5px;
  image: url(":/qss_icons/dark/rc/line_vertical.png");
}

QSplitter::handle:vertical {
  height: 5px;
  image: url(":/qss_icons/dark/rc/line_horizontal.png");
}