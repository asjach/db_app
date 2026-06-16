# DB App

## Overview
A PySide6 desktop application for managing students, teachers, grades, and documents.

## Quick start
1. Activate the virtual environment:
   - `venv\Scripts\Activate.ps1`
2. Install dependencies:
   - `pip install -r requirements.txt`
3. Run the application:
   - `python app.py`

## Environment
The database connection is loaded from `.env`.
Do not commit real credentials into source control.

Create a `.env` file from `.env.example` with these variables:
- `DATABASE_HOST`
- `DATABASE_USER`
- `DATABASE_PASSWORD`
- `DATABASE_PORT`
- `DATABASE_NAME`

## UI workflow
- UI definitions live in `ui/sources/*.ui`
- Generated Python UI modules are in `ui/ui_*.py`
- Do not edit `ui/ui_*.py` directly unless you also update the source `.ui` file.

## Key files
- `app.py`: application startup
- `scripts/main.py`: main window and page/tab wiring
- `scripts/tab_config.py`: page routing and shared configuration
- `models/*`: business logic and SQL access
- `utils/database.py`: shared MySQL wrapper
- `utils/fungsi/*`: shared helpers for UI, SQL, and PDF
