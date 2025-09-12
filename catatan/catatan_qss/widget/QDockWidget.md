# PROPERTY
  - border



## SUB CONTROL
::close-button
::float-button
::title

## PSEUDO-STATE
:closable
:floatable
:movable




QDockWidget {
  outline: 1px solid #455364;
  background-color: #19232D;
  border: 1px solid #455364;
  border-radius: 4px;
  titlebar-close-icon: url(":/qss_icons/dark/rc/transparent.png");
  titlebar-normal-icon: url(":/qss_icons/dark/rc/transparent.png");
}

QDockWidget::title {
  /* Better size for title bar */
  padding: 3px;
  spacing: 4px;
  border: none;
  background-color: #455364;
}

QDockWidget::close-button {
  icon-size: 12px;
  border: none;
  background: transparent;
  background-image: transparent;
  border: 0;
  margin: 0;
  padding: 0;
  image: url(":/qss_icons/dark/rc/window_close.png");
}

QDockWidget::close-button:hover {
  image: url(":/qss_icons/dark/rc/window_close_focus.png");
}

QDockWidget::close-button:pressed {
  image: url(":/qss_icons/dark/rc/window_close_pressed.png");
}

QDockWidget::float-button {
  icon-size: 12px;
  border: none;
  background: transparent;
  background-image: transparent;
  border: 0;
  margin: 0;
  padding: 0;
  image: url(":/qss_icons/dark/rc/window_undock.png");
}

QDockWidget::float-button:hover {
  image: url(":/qss_icons/dark/rc/window_undock_focus.png");
}

QDockWidget::float-button:pressed {
  image: url(":/qss_icons/dark/rc/window_undock_pressed.png");
}