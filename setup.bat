@echo off
title Sentiment AI Setup

echo.
echo ============================================
echo          SENTIMENT AI SETUP
echo ============================================
echo.

echo Checking Python...
python --version

if errorlevel 1 (
    echo.
    echo ERROR: Python was not found.
    echo Please install Python and try again.
    pause
    exit /b 1
)

echo.
echo Checking Git...
git --version

if errorlevel 1 (
    echo.
    echo ERROR: Git was not found.
    echo Please install Git and try again.
    pause
    exit /b 1
)

echo.
echo Checking Git LFS...
git lfs version

if errorlevel 1 (
    echo.
    echo ERROR: Git LFS was not found.
    echo Please install Git LFS and try again.
    pause
    exit /b 1
)

echo.
echo ============================================
echo Downloading large model files...
echo ============================================
echo.

git lfs install
git lfs pull

if errorlevel 1 (
    echo.
    echo ERROR: Git LFS could not download the model.
    pause
    exit /b 1
)

echo.
echo ============================================
echo Creating Python environment...
echo ============================================
echo.

if not exist ".venv" (
    python -m venv .venv
) else (
    echo Python environment already exists.
)

echo.
echo ============================================
echo Installing Python packages...
echo ============================================
echo.

call .venv\Scripts\activate.bat

python -m pip install --upgrade pip

pip install -r requirements.txt

if errorlevel 1 (
    echo.
    echo ERROR: Python packages could not be installed.
    pause
    exit /b 1
)

echo.
echo ============================================
echo Installing NLTK resources...
echo ============================================
echo.

python -c "import nltk; nltk.download('wordnet'); nltk.download('omw-1.4')"

if errorlevel 1 (
    echo.
    echo ERROR: NLTK resources could not be downloaded.
    pause
    exit /b 1
)

echo.
echo ============================================
echo             SETUP COMPLETE
echo ============================================
echo.
echo You can now start Sentiment AI.
echo.
echo Run:
echo.
echo     run.bat
echo.
echo Or manually run:
echo.
echo     .venv\Scripts\activate
echo     python app.py
echo.
pause