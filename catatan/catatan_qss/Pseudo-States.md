:hover          ketika mouse hover ke item
:pressed        ketika item di tekan
:selected       ketika dipilih/terpilih
:focus          ketika item dalam keadaan input mode
:editable       contoh combobox yang dibuat editable
:default        ketika item memiliki default  
:flat           contoh flat pada button
:active         ketika state window aktif

### widget yang diaktif/non-aktifkan
:disabled
:enabled

### widget yang memiliki orientasi seperti scrollbar
:horizontal
:vertical

### item yang bisa diceklist (ada 3 state)
:checked        ketika statenya 'checked'
:unchecked
:indeterminate

### item yang memiliki posisi contoh TabBar
:first
:middle
:last
:previous-selected
:next-selected
:only-one

### Untuk item yang diposisikan seperti posisi TabBar
:top
:left
:right
:bottom         ketika item ditempatkan di bawah seperti TabBar yang 
                disimpan di bottom

### untuk item yang bisa di Toggle
:on                   ketika item yang bisa ditoggled dalam state off
:off                  ketika item yang bisa ditoggled dalam state off

:maximized
:minimized

:no-frame           ketika item framenya dihilangkan
:window


### untuk item yang di exclusive/non-exclusive, contoh seperti pada checkbox atau button yang checkable
:exclusive
:non-exclusive

:movable
:open
:read-only
:adjoins-item   khusus treeview
:alternate      untuk alternate row pada QAbstractItemView ketika 
                alternatingRowColor() di aktifkan
:edit-focus
:floatable
:has-children
:has-siblings
:closed         
:closable       ketika statenya 'closable' contoh di QDockWidget