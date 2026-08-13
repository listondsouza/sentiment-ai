@echo off
title Sentiment AI

echo.
echo ============================================
echo          STARTING SENTIMENT AI
echo ============================================
echo.

if not exist ".venv\Scripts\python.exe" (
    echo ERROR: Python environment not found.
    echo.
    echo Please run setup.bat first.
    pause
    exit /b 1
)

call .venv\Scripts\activate.bat

echo Starting Flask...
echo.
echo Open this address in your browser:
echo.
echo http://127.0.0.1:5000
echo.
echo Press CTRL+C to stop the server.
echo.

python app.py

pause