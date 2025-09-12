## PROPERTY
- box model
- icon


## SUB CONTROL
::menu-indicator

## PSEUDO-STATE
:default
:flat
:checked
:open
:closed



QPushButton {
    border: 1px solid #333333;
    border-radius: 2px;
    background-color: #455364;
    padding: 1px 1px;
    color: #DFE1E2;
    outline: none;
}

QPushButton:hover{
    background-color: #264F78;
    border-color: #5599ff;
}

QPushButton:pressed
{
    border-width: 1px;      
    background-color: #5599ff;
    border-color: #333333;
}

QPushButton:focus {
    border-color: #0078D4; /* make the default button prominent */
}

QPushButton::default{
	border-style: solid;
	border-top-color: transparent;
	border-right-color: transparent;
	border-left-color: transparent;
	border-bottom-color: #e67e22;
	border-width: 1px;
	color: #a9b7c6;
	padding: 2px;
	background-color: #000000;
}

QPushButton:disabled {
  background-color: #455364;
  color: #788D9C;
  border-radius: 4px;
  padding: 2px;
}

QPushButton:checked {
  background-color: #60798B;
  border-radius: 4px;
  padding: 2px;
  outline: none;
}

QPushButton:checked:disabled {
  background-color: #60798B;
  color: #788D9C;
  border-radius: 4px;
  padding: 2px;
  outline: none;
}

QPushButton:checked:selected {
  background: #60798B;
}


QPushButton:selected {
  background: #60798B;
  color: #DFE1E2;
}

QPushButton::menu-indicator {
  subcontrol-origin: padding;
  subcontrol-position: bottom right;
  bottom: 4px;
}

QDialogButtonBox QPushButton {
  /* Issue #194 #248 - Special case of QPushButton inside dialogs, for better UI */
  min-width: 80px;
}

