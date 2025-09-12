# PROPERTY
  - box model
  - spacing
  - placeholder-text-color
  

## SUB CONTROL
::drop-down
::down-arrow  



QComboBox {
  border: 1px solid #455364;
  border-radius: 4px;
  selection-background-color: #346792;
  padding-left: 4px;
  padding-right: 4px;
  /* padding-right = 36; 4 + 16*2 See scrollbar size */
  /* changed to 4px to fix #239 */
  /* Fixes #103, #111 */
  min-height: 1.5em;

  /* padding-top: 2px;     removed to fix #132 */
  /* padding-bottom: 2px;  removed to fix #132 */
  /* min-width: 75px;      removed to fix #109 */
  /* Needed to remove indicator - fix #132 */
}

QComboBox QAbstractItemView {
  border:
  background-color:
  selection-background-color:
}

QComboBox QAbstractItemView:hover {
  background-color: #19232D;
  color: #DFE1E2;
}

QComboBox QAbstractItemView:selected {
  background: #346792;
  color: #455364;
}

QComboBox QAbstractItemView:alternate {
  background: #19232D;
}

QComboBox:disabled {
  background-color: #19232D;
  color: #788D9C;
}

QComboBox:hover {
  border: 1px solid #346792;
}

QComboBox:focus {
  border: 1px solid #1A72BB;
}

QComboBox:on {
  selection-background-color: #346792;
}

QComboBox::indicator {
  border: none;
  border-radius: 0;
  background-color: transparent;
  selection-background-color: transparent;
  color: transparent;
  selection-color: transparent;
  /* Needed to remove indicator - fix #132 */
}

QComboBox::indicator:alternate 
  {
    background: #19232D;
  }

QComboBox::item {
    /* Remove to fix #282, #285 and MR #288*/
    /*&:checked {
              font-weight: bold;
          }

          &:selected {
              border: 0px solid transparent;
          }
          */
  }

QComboBox::item:alternate 
  {
    background: #19232D;
  }

QComboBox::drop-down 
  {
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 12px;
    border-left: 1px solid #455364;
  }

QComboBox::down-arrow 
  {
    image: url(":/qss_icons/dark/rc/arrow_down_disabled.png");
    height: 8px;
    width: 8px;
  }

QComboBox::down-arrow:on, 
QComboBox::down-arrow:hover, 
QComboBox::down-arrow:focus 
  {
    image: url(":/qss_icons/dark/rc/arrow_down.png");
  }

QComboBox:editable {
	background:
	color: 
	selection-background-color:
}

QComboBox:!editable:on, 
QComboBox::drop-down:editable:on {
	color: 
	background: 
}