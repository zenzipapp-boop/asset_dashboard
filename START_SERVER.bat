@echo off
echo.
echo ====================================================
echo   ASSET AUDIT SYSTEM - SERVER STARTUP
echo ====================================================
echo.

echo Installing dependencies...
pip install -q -r requirements.txt

echo.
echo [OK] Starting FastAPI server on http://localhost:8000
echo.
echo Open your browser to:
echo   http://localhost:8000
echo.
echo Press Ctrl+C to stop the server
echo.

python app.py
