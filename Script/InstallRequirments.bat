@echo off
REM Ensure Python and pip are installed and in the system's PATH

REM Change directory to the current script's directory
cd /d "%~dp0"

REM Install packages from requirements.txt
echo Installing Python packages from requirements.txt...
"C:\Users\%username%\AppData\Local\Programs\Python\Python312\python.exe" -m pip install -r requirement.txt

echo Requirements installation finished.

exit
