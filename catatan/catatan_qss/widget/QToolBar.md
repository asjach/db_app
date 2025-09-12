QToolBar {
  background-color: #455364;
  border-bottom: 1px solid #19232D;
  padding: 1px;
  font-weight: bold;
  spacing: 2px;
}

QToolBar:disabled {
  /* Fixes #272 */
  background-color: #455364;
}

QToolBar::handle:horizontal {
  width: 16px;
  image: url(":/qss_icons/dark/rc/toolbar_move_horizontal.png");
}

QToolBar::handle:vertical {
  height: 16px;
  image: url(":/qss_icons/dark/rc/toolbar_move_vertical.png");
}

QToolBar::separator:horizontal {
  width: 16px;
  image: url(":/qss_icons/dark/rc/toolbar_separator_horizontal.png");
}

QToolBar::separator:vertical {
  height: 16px;
  image: url(":/qss_icons/dark/rc/toolbar_separator_vertical.png");
}