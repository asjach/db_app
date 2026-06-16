# Copilot Instructions

## What this project is
- A PySide6 desktop application for student, teacher, grades, and document management.
- Entry point: `app.py` launches `scripts/main.py` and builds the window from generated UI classes in `ui/`.
- UI is generated from Qt Designer source files in `ui/sources/*.ui` and compiled into `ui/ui_*.py`.

## Architecture & boundaries
- `scripts/main.py` is the main application shell:
  - loads `TAB_CONFIG` from `scripts/tab_config.py`
  - creates page widgets from `scripts/pages/*`
  - maps menu actions to page classes and shared parent state
- `scripts/pages/*` contains page-specific views and controller logic.
- `models/*` contains database-access classes derived from `utils/database.py`.
- `utils/database.py` is the shared MySQL wrapper: `ConnectDB` exposes `get_data`, `get_one_data`, `update_data`, and transaction helpers.
- `utils/fungsi/*` contains shared UI helpers, especially table rendering and filtering utilities.

## Important conventions
- Do not edit generated UI files under `ui/ui_*.py` unless you also update the corresponding source `.ui` file in `ui/sources/`.
- Page widgets generally use a `Model_*` instance for SQL work and `generate_table()` / helper functions for UI updates.
- `TAB_CONFIG` is the central page registry: it binds page titles, action names, and page classes.
- Global filter and selection state is stored on the main window instance (e.g. `str_jenjang`, `quoted_daftar_tingkat`, `str_search_by`).
- SQL uses MySQL connector parameter style `%s`; avoid inline string assembly except where the code already builds safe `IN (...)` fragments.
- `static_values.json` is used for shared UI and formatting defaults.

## Typical workflow
- Activate virtualenv: `venv\Scripts\Activate.ps1`
- Install dependencies: `pip install -r requirements.txt`
- Run app: `python app.py`
- If UI source changes: regenerate generated UI modules from `ui/sources/*.ui` with `pyside6-uic`.

## What to read first
- `app.py` for startup behavior
- `scripts/main.py` for main UI assembly and signal wiring
- `scripts/tab_config.py` for page routing and shared config
- `utils/database.py` for database connection patterns
- `scripts/pages/*` for page-specific UI-controller logic

## What not to do
- Avoid changing generated `ui/ui_*.py` directly for layout logic.
- Avoid creating new page classes outside `scripts/pages/*` unless there is a new menu/tab flow.
- Avoid changing DB connection details in code; they are loaded from `.env`.
- Do not commit `.env`; use `.env.example` for environment templates.

## Key files to reference
- `scripts/main.py`
- `scripts/tab_config.py`
- `utils/database.py`
- `utils/fungsi/table_functions.py`
- `models/model_main.py`, `models/model_nilai.py`
- `ui/sources/*.ui`
