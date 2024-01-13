@echo off
SETLOCAL ENABLEEXTENSIONS

:: Determine the directory where the script is located
set SCRIPT_DIR=%~dp0
cd /d %SCRIPT_DIR%..

:: Set the registry path
set KEY_PATH="HKEY_CLASSES_ROOT\*\shell\SpeedLocker\command"

:: Set the command to run your Python script - Modify pythonw.exe path if necessary
set COMMAND="\"C:\Users\%username%\AppData\Local\Programs\Python\Python312\pythonw.exe\" \"%CD%\Script\encrypt_gestion.py\" \"%%1\""

:: Add the registry key
reg add %KEY_PATH% /ve /t REG_SZ /d %COMMAND% /f

if %ERRORLEVEL% == 0 (
    echo Registry updated successfully!
) else (
    echo Failed to update registry. Please ensure you have administrative rights.
)

exit
