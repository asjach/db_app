Widget2 yang biasanya bisa discroll

## CHILD WIDGET
QAbstractItemView, 
QGraphicsView, 
QMdiArea, 
QPlainTextEdit, 
QScrollArea, 
QTextEdit, 
QTextBrowser



## SUB CONTROL
::corner	bagian pinggir antara 2 scrollbar


QAbstractScrollArea {
  background-color: #19232D;
  border: 1px solid #455364;
  border-radius: 4px;
  /* fix #115599ff */
  padding: 2px;
  /* remove min-height to fix #244 */
  color: #DFE1E2;
}

QAbstractScrollArea:disabled {
  color: #788D9C;
}