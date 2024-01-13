[Setup]
AppName=SpeedLocker
AppVersion=1.0
DefaultDirName={pf}\SpeedLocker
PrivilegesRequired=admin

[Files]
; Include the Python installer
Source: "python-3.12.1-amd64.exe"; DestDir: "{tmp}"; Flags: deleteafterinstall

; Include your application files (assuming you've already cloned your repo locally)
Source: "SpeedLocker\*"; DestDir: "{app}"; Flags: recursesubdirs createallsubdirs

[Run]
; Run the Python installer
Filename: "{tmp}\python-3.12.1-amd64.exe"; Parameters: "/quiet InstallAllUsers=0 PrependPath=1"; StatusMsg: "Installing Python..."; Flags: waituntilterminated shellexec runascurrentuser

; Install python requirements
Filename: "{app}\Script\InstallRequirments.bat"; Parameters: ""; StatusMsg: "Installing Python Requirements..."; Flags: runascurrentuser waituntilterminated runhidden

; Run your application
Filename: "{app}\Script\Installation.bat"; Parameters: ""; StatusMsg: "Running SpeedLocker Installer..."; Flags: runascurrentuser waituntilterminated runhidden

[UninstallRun]

; Uninstall your application
Filename: "{app}\Script\Uninstallation.bat"; Parameters: ""; StatusMsg: "Uninstalling SpeedLocker..."; Flags: runascurrentuser waituntilterminated runhidden