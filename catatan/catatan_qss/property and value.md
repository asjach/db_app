## Stylable Widget
QAbstractScrollArea     Box Model
                        

QCheckBox               Box Model


## PROPERTY


## PROPERTY VALUE
### LEVEL 1     SHORT HAND
Attachment      {scroll | fixed}
Background      {Brush | Url | Repeat | Alignment}
Border          {Border Sytle | Length | Brush}
Font            (Font Style | Font Weight){0,2} Font Size String
Origin          margin | border | padding | content
Radius          Length{1, 2}
                1 nilai = bentuk radiusnya seperempat lingkaran
                2 nilai = horizontal_radius vertical_radius

Box Colors      Brush{1,4}
                1 nilai = semua sisi
                2 nilai = top-bottom right-left
                3 nilai = top left-right bottom
                4 nilai = top right bottom left
                                              top   right   bottom  left
                1 => red                    = red   red     red     red
                2 => red blue               = red   blue    red     blue
                3 => red blue green         = red   blue    green   blue
                4 => red blue green pink    = red   blue    green   pink

Box Length      Length{1, 4} top right bottom left
                sama seperti box color yakni:
                1 nilai = semua sisi
                2 nilai = top-bottom right-left
                3 nilai = top left-right bottom
                4 nilai = top right bottom left

Font Size       Length
Font Style      normal | italic | oblique
Font Weight     normal | bold | 100 sampai 900


### LEVEL 2     MENGARAH KE LEVEL DI BAWAHNYA
Brush           Color | Gradient | PaletteRole



### LEVEL 3
Length          Number (px|pt|em|ex)
                px  = pixel
                pt  = point (contoh 1/72 inch) tergantung dpi
                em  = ukuran relative terhadap font size
                ex  = tinggi huruf x font
Color           rgb(r, g, b)        nilai variabel 0-255 atau persentase 100% = 1
                rgba(r, g, b, a)
                hsv (h, s, v)
                hsva (h, s, v, a)
                hsl (h, s, l)
                hsla (h, s, l, a)
                #rrggbb
                Color Name
                transparent

### LEVEL 4

Boolean         0 | 1
Number          integer atau double/float atau angka real 
                contoh: 0, 18, +127, -255, 12.34, -.5, 0009.
Border Style    dashed | dot-dash | dot-dot-dash | dotted | double | groove 
                | inset | outset | ridge | solid | none
Border Image    none
                | Url
Alignment       top | bottom | left | right | center
Url             url(filename)
Repeat          repeat-x 
                | repeat-y 
                | repeat 
                | no-repeat