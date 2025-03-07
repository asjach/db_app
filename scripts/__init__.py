from .pages import *
from .dialogs import *
from .widgets import *


__all__ = pages.__all__ + dialogs.__all__ + widgets.__all__


# NAMA_PROJECT
#     model
#         siswa.py
#             ClassSiswa
#         guru.py
#             ClassGuru
#         main.py
#             ClassMain
#         ...
#     script
#         pages
#             daftar_kelas.py
#             rekap.py
#             mutasi_keluar.py
#             ...
#         dialogs
#             detail_siswa.py
#                 ClassDetailSiswa
#                 ClassRiwayatBelajar
#                 ...
#             ...
#     utils
#         db.py
#         functions.py
#         tab_config.py
#         ...

# bagaimana mengatur __init__.py di tiap foldernya sehingga saya tidak perlu mengimport di tiap file