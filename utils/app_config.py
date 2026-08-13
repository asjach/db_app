from pathlib import Path
import os

# =====================
# BASE DIR APLIKASI
# =====================
BASE_DIR = Path(__file__).resolve().parent.parent


# =====================
# ROOT DETECTION
# =====================
def resolve_data_root(base_dir: Path) -> Path:
    """
    Mencari root data secara aman.
    Prioritas:
    1. ENV VAR (paling stabil)
    2. Marker folder project
    3. fallback drive root (Windows)
    """

    # 1. ENV override (REKOMENDASI TERKUAT)
    env_root = os.getenv("APP_DATA_ROOT")
    if env_root:
        return Path(env_root)

    # 2. cari marker project
    for parent in [base_dir] + list(base_dir.parents):
        if (parent / "DATABASE").exists() or (parent / "OneDrive - MI Persis Rahayu").exists():
            return parent

    # 3. fallback Windows/Linux
    return Path(base_dir.anchor)


DATA_ROOT = resolve_data_root(BASE_DIR)


# =====================
# DIREKTORI DATA
# =====================
ONEDRIVE_NAME = "OneDrive - MI Persis Rahayu"

DIREKTORI_ONEDRIVE = DATA_ROOT / ONEDRIVE_NAME
DIREKTORI_DOKUMEN = DIREKTORI_ONEDRIVE / "database" / "dokumen"


# =====================
# FOLDER LOGICAL
# =====================
FOLDER_SISWA = "siswa"
FOLDER_GURU = "guru"
FOLDER_MADRASAH = "madrasah"


# =====================
# FORMAT SETTINGS
# =====================
SEPARATOR_RIBUAN = "."
SEPARATOR_DESIMAL = ","


# =====================
# DEBUG FLAGS
# =====================
DEBUG_GET = False
DEBUG_UPDATE = False
DEBUG_ONE = False
DEBUG_LIST = False