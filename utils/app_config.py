# import os

# BASE_DIR = "E:/APP/DB App"
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# DIREKTORI_ONEDRIVE = "E:/OneDrive - MI Persis Rahayu"
# DIREKTORI_DOKUMEN = os.path.join(DIREKTORI_ONEDRIVE, "Database/dokumen")



from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

def resolve_data_root(base_dir: Path):
    """
    Menemukan root data (misalnya E:\ atau /Madrasah)
    berdasarkan lokasi APP.
    """
    for parent in base_dir.parents:
        if parent.name.lower() in ("madrasah",):  # mount point Linux
            return parent
    # fallback Windows (drive letter)
    return Path(base_dir.anchor)

DATA_ROOT = resolve_data_root(BASE_DIR)

DIREKTORI_ONEDRIVE = DATA_ROOT / "OneDrive - MI Persis Rahayu"
DIREKTORI_DOKUMEN = DIREKTORI_ONEDRIVE / "DATABASE" / "dokumen"

FOLDER_SISWA = "siswa"
FOLDER_GURU = "guru"
FOLDER_MADRASAH = "madrasah"
SEPARATOR_RIBUAN = "."
SEPARATOR_DESIMAL  = ","
DEBUG_GET = False
DEBUG_UPDATE = False
DEBUG_ONE = False
DEBUG_LIST = False