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
Filename: "{tmp}\python-3.12.1-amd64.exe"; Parameters: "/quiet InstallAllUsers=1 PrependPath=1"; StatusMsg: "Installing Python..."; Flags: waituntilterminated

; Install python requirements
Filename: "{app}\Script\InstallRequirements.bat"; Parameters: ""; StatusMsg: "Installing Python Requirements..."; Flags: runascurrentuser waituntilterminated

; Run your application
Filename: "{app}\Script\Installation.bat"; Parameters: ""; StatusMsg: "Running SpeedLocker Installer..."; Flags: runascurrentuser waituntilterminated