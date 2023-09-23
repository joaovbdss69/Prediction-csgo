import os
import sys

from pathlib import Path

found_root = False
cur_path = Path(__file__).parent

for depth in range(10):
    list_files = os.listdir(cur_path)

    if '.proj_root' not in list_files:
        cur_path /= '..'
        continue

    PROJ_DIR = cur_path.resolve()
    found_root = True
    break

if not found_root:
    raise RuntimeError("Project root folder not found. Please check if "
                       "the file ** .proj_root ** exists."
    )


DATA_FLD    = PROJ_DIR / 'data'
DATA_RAW_FLD    = DATA_FLD / 'raw'
DATA_INTERIM_FLD    = DATA_FLD / 'interim'
DATA_PROCESSED_FLD    = DATA_FLD / 'processed'
DATA_EXTERNAL_FLD    = DATA_FLD / 'external'
MODELS_FLD    = PROJ_DIR / 'models'
NOTEBOOKS_FLD    = PROJ_DIR / 'notebooks'
SRC_FLD    = PROJ_DIR / 'src'
SQL_FLD    = SRC_FLD / 'sql'
DATA_CLEAN_FLD = SRC_FLD / 'data'
FEATURES_FLD = SRC_FLD / 'features'
MODELS_SRC_FLD = SRC_FLD / 'models'
VISUALIZATION_FLD = SRC_FLD / 'visualization'
REFERENCES_FLD    = PROJ_DIR / 'references'
REPORTS_FLD    = PROJ_DIR / 'reports'
FIGURES_FLD    = REPORTS_FLD / 'figures'