@echo off
SETLOCAL ENABLEEXTENSIONS

:: Set the registry path
set KEY_PATH="HKEY_CLASSES_ROOT\*\shell\SpeedLocker"

:: Delete the registry key
reg delete %KEY_PATH% /f

if %ERRORLEVEL% == 0 (
    echo Registry key deleted successfully!
) else (
    echo Failed to delete registry key. Please ensure you have administrative rights.
)

exit
