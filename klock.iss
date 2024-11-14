; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppName "pyKlock"
#define MyAppVersion "2024.32"
#define MyAppPublisher "keleven"
#define MyAppURL "www.keleven.co.uk"
#define MyAppExeName "pyklock.exe"

[Setup]
; NOTE: The value of AppId uniquely identifies this application.
; Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{9DD174AE-9044-436B-BAA1-585AC5521A11}}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}

;  all source files here
SourceDir=D:\My\shed\Projects\python\pyKlock1\output\Klock

DefaultDirName={pf}\keleven\{#MyAppName}
DefaultGroupName={#MyAppName}
LicenseFile=LICENSE.txt
InfoAfterFile=README.md
OutputDir=D:\My\shed\Projects\python\pyKlock1\output\Klock
OutputBaseFilename={#MyAppName}_{#MyAppVersion}
SetupIconFile=resources\tea.ico
Compression=lzma
SolidCompression=yes
DisableStartupPrompt=False
UsePreviousAppDir=False
SetupLogging=True

; "ArchitecturesInstallIn64BitMode=x64" requests that the install be done in "64-bit mode" 
; on x64, meaning it should use the native 64-bit Program Files directory and the 64-bit 
; view of the registry. On all other architectures it will install in "32-bit mode".
ArchitecturesInstallIn64BitMode=x64
; Note: We don't set ProcessorsAllowed because we want this installation to run on 
; all architectures (including Itanium,since it's capable of running 32-bit code too)

[Messages]
SetupLdrStartupMessage=This will install [%1 {#MyAppVersion}] on your computer.

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"    ; Description: "{cm:CreateDesktopIcon}"    ; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked
Name: "quicklaunchicon"; Description: "{cm:CreateQuickLaunchIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked; OnlyBelowVersion: 0,6.1


; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Files]
Source: "Klock.exe"    ; DestDir: "{app}"           ; Flags: ignoreversion; Check: Is64BitInstallMode    ; DestName: {#MyAppExeName}
Source: "LICENSE.txt"  ; DestDir: "{app}"           ; Flags: ignoreversion
Source: "history.txt"  ; DestDir: "{app}"           ; Flags: ignoreversion
Source: "README.md"    ; DestDir: "{app}"           ; Flags: isreadme
Source: "version.toml" ; DestDir: "{app}"           ; Flags: ignoreversion
Source: "_internal\*"  ; DestDir: "{app}\_internal" ; Flags: recursesubdirs
Source: "help\*"       ; DestDir: "{app}\help"      ; Flags: ignoreversion
Source: "resources\*"  ; DestDir: "{app}\resources" ; Flags: ignoreversion

[Icons]
Name: "{group}\{#MyAppName}"                                               ; Filename: "{app}\{#MyAppExeName}"
Name: "{group}\{cm:UninstallProgram,{#MyAppName}}"                         ; Filename: "{uninstallexe}"
Name: "{commondesktop}\{#MyAppName}"                                       ; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon
Name: "{userappdata}\Microsoft\Internet Explorer\Quick Launch\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: quicklaunchicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, "&", "&&")}}"; Flags: nowait postinstall skipifsilent

