from .siswa import *
from .guru import *
from .dokumen import *
from .nilai import *
from .preferensi import *
from .pembayaran import *

__all__ =   siswa.__all__ + \
            guru.__all__ + \
            dokumen.__all__ + \
            nilai.__all__+\
            preferensi.__all__+\
            pembayaran.__all__