/* =============================================== */
/* QTableWidget                                    */
/* =============================================== */

QTableWidget, QTableView
{
    gridline-color: #333333;    
    background: #181818;
    alternate-background-color: #DADADA;
    selection-background-color:#264F78;   
    border:1px solid #333333;  
    /*border:none;   
    /*border-radius:5px;*/
    /*padding:10px 10px;*/  
}
QTableView::item, QTabWidget::item{
    background: transparent;
	outline-style: none;
	border: none;
}

QTableView::item:hover {
	background: #264F78;
    border: 1px solid #0078D4;
}

QTableView::item:selected {
	background: #264F78;
	color: #DADADA;
}

QTableView::item:selected:active {
	background: #5599ff;
	color: #DADADA;
}

QTableWidget QComboBox{
    margin: 2px;
    border: none;
}
