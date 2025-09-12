Referensi:
https://doc.qt.io/qt-6/stylesheet-syntax.html

## CATATAN UMUM
- QSS case insensensitive kecuali nama class, nama objek, dan Qt Property Names
- selector dapat disambungkan: QPushButton, QLineEdit, QComboBox {color: red}
- 

## STRUKTUR QSS
QPushButton{color:red}
QPushButton => selector
{}          => declaration
color:red   => property


## TIPE SELECTOR

- Universal Selector    = *   => seluruh widget
- Type Selector         = QPushButton   => mencakup seluruh instance dan subclassnya
- Property Selector     = QpushButton[flat="false"] => property di Qt
- Class Selector        = .QPushButton  => mencakup seluruh instance tapi tidak dengan subclassnya equivalen dengan *[class~="QPushButton"]
- ID Selector           = QPushButton#okButton => object name
- Descendant Selector   = QDialog QPushButton => seluruh QPushButton yang menjadi turunan (children, grandchildren, dll) dari QDialog
- Child Selector        = QDialog>QPushButton   => hanya child saja



## SUB-CONTROL
- ditandai dengan ::


## Pseudo-States
- ditandai dengan ":"
- bisa di-'chain'  => QCheckBox:hover:checked (memakai logika AND)
- Bisa di negate   => QCheckBox:!checked
- logika OR        => QCheckBox:hover, QCheckBox:pressed
- Bisa dikombinasikan dengan sub-control  => QComboBox::drop-down:hover
