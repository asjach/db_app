# CATATAN
- jika satu property di sub-control di style, maka seluruh property atau sub-control harus di customisasi juga

## SUB-CONTROL
::add-line (tombol untuk menambah line biasanya tombol panah ke bawah)
::add-page (daerah antara handle (slider) dan add-line)
::down-arrow
::down-button
::handle
::left-arrow
::right-arrow
::sub-line
::sub-page
::up-arrow
























QScrollBar:horizontal {
  height: 16px;
  max-height: 20px;
  margin:
  border: 

  background-color:
}

QScrollBar:vertical {
  background-color: 
  margin:
  border:
  width:
  max-width: 20px;
}



### HANDLE
QScrollBar::handle:horizontal {
  background-color: 
  border: 1px solid 
  border-radius: 
  min-width: 
}

QScrollBar::handle:horizontal:hover {
  background-color: 
  border: 
  border-radius: 
  min-width: 
}

QScrollBar::handle:horizontal:focus {
  border: 
}

QScrollBar::handle:vertical {
  background-color: 
  border: 
  min-height: 
  border-radius: 
}

QScrollBar::handle:vertical:hover {
  background-color: 
  border: 
  border-radius: 
  min-height: 
}

QScrollBar::handle:vertical:focus {
  border:
}



### ADD-LINE
QScrollBar::add-line:horizontal {
  margin: 
  border-image: url(":/qss_icons/dark/rc/arrow_right_disabled.png");
  height: 
  width: 
  subcontrol-position: right;
  subcontrol-origin: margin;
}

QScrollBar::add-line:horizontal:hover, QScrollBar::add-line:horizontal:on {
  border-image: url(":/qss_icons/dark/rc/arrow_right.png");
  height: 12px;
  width: 12px;
  subcontrol-position: right;
  subcontrol-origin: margin;
}

QScrollBar:: add-line:horizontal:pressed{

}

QScrollBar::add-line:vertical {
  margin: 3px 0px 3px 0px;
  border-image: url(":/qss_icons/dark/rc/arrow_down_disabled.png");
  height: 12px;
  width: 12px;
  subcontrol-position: bottom;
  subcontrol-origin: margin;
}

QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on {
  border-image: url(":/qss_icons/dark/rc/arrow_down.png");
  height: 12px;
  width: 12px;
  subcontrol-position: bottom;
  subcontrol-origin: margin;
}
QScrollBar::add-line:vertical:pressed{
  
}


### SUB-LINE
QScrollBar::sub-line:horizontal {
  margin: 0px 3px 0px 3px;
  border-image: url(":/qss_icons/dark/rc/arrow_left_disabled.png");
  height: 12px;
  width: 12px;
  subcontrol-position: left;
  subcontrol-origin: margin;
}

QScrollBar::sub-line:horizontal:hover, QScrollBar::sub-line:horizontal:on {
  border-image: url(":/qss_icons/dark/rc/arrow_left.png");
  height: 12px;
  width: 12px;
  subcontrol-position: left;
  subcontrol-origin: margin;
}

QScrollBar::sub-line:vertical {
  margin: 3px 0px 3px 0px;
  border-image: url(":/qss_icons/dark/rc/arrow_up_disabled.png");
  height: 12px;
  width: 12px;
  subcontrol-position: top;
  subcontrol-origin: margin;
}

QScrollBar::sub-line:vertical:hover, QScrollBar::sub-line:vertical:on {
  border-image: url(":/qss_icons/dark/rc/arrow_up.png");
  height: 12px;
  width: 12px;
  subcontrol-position: top;
  subcontrol-origin: margin;
}



### UP-ARROW
QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal {
  background: none;
}

QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
  background: none;
}



### ADD-PAGE  ### SUB-PAGE
QScrollBar::add-page:horizontal, 
QScrollBar::sub-page:horizontal {
  background: none;
}

QScrollBar::add-page:vertical, 
QScrollBar::sub-page:vertical {
  background: none;
}






### LEFT-ARROW
QScrollBar::left-arrow:horizontal {
  	border: 1px transparent grey;
  	border-radius: 3px;
  	width: 6px;
  	height: 6px;
 	background: rgb(0,0,0);
}

### RIGHT-ARROW
QScrollBar::right-arrow:horizontal {
	border: 1px transparent grey;
	border-radius: 3px;
  	width: 6px;
  	height: 6px;
 	background: rgb(0,0,0);
}