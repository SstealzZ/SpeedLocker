@echo off
REM Ensure Python and pip are installed and in the system's PATH

REM Change directory to the current script's directory
cd /d "%~dp0"

REM Install packages from requirements.txt
echo Installing Python packages from requirements.txt...
python -m pip install -r requirement.txt

echo Requirements installation finished.
exit
