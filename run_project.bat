@echo off
echo Smart Agriculture Crop Yield Prediction - Project Runner
echo =====================================================

REM Check if virtual environment exists
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
    if errorlevel 1 (
        echo Error: Could not create virtual environment.
        echo Please make sure Python is installed and accessible.
        pause
        exit /b 1
    )
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat
if errorlevel 1 (
    echo Error: Could not activate virtual environment.
    pause
    exit /b 1
)

REM Install requirements
echo Installing required packages...
pip install -r requirements.txt
if errorlevel 1 (
    echo Error: Could not install required packages.
    echo Please check your internet connection and Python installation.
    pause
    exit /b 1
)

REM Run the main program
echo.
echo Starting Crop Yield Prediction System...
echo =====================================================
python main.py

REM Keep window open after execution
echo.
echo =====================================================
echo Program finished. Press any key to exit...
pause >nul
