; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!
#define MyAppSourcePath ExtractFilePath(GetEnv("ScriptPath")) + "..\..\cgpt\dist\windows"
#define MyAppName "cgpt"
#define MyAppVersion "0.2"
#define MyAppPublisher "avillenas.com"
#define MyAppURL "https://avillenas.com/"
#define MyAppExeName "cgpt.exe"

[Setup]
; NOTE: The value of AppId uniquely identifies this application. Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{067E57E5-CF7A-41DA-B77C-BF6C0F51C2B9}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={autopf}\{#MyAppName}
DefaultGroupName={#MyAppName}
DisableProgramGroupPage=yes
; Remove the following line to run in administrative install mode (install for all users.)
PrivilegesRequired=admin
OutputBaseFilename=cgpt-installer
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Files]
Source: "{#MyAppSourcePath}\{#MyAppExeName}"; DestDir: "{app}"; Flags: ignoreversion
Source: "{#MyAppSourcePath}\config.ini"; DestDir: "{app}"; Flags: ignoreversion
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Code]
var
  ApiKeyPage: TInputQueryWizardPage;

procedure InitializeWizard;
begin
  ApiKeyPage := CreateInputQueryPage(wpWelcome,
    'OpenAI API Key', 'Please enter your OpenAI API key.',
    'Please enter your API key, then click Next.');
  ApiKeyPage.Add('API Key:', True);
end;

procedure UpdateConfigFile(FileName: string; Placeholder: string; Value: string);
var
  Lines: TStringList;
  i: Integer;
  S: string;
begin
  Lines := TStringList.Create();
  try
    Lines.LoadFromFile(FileName);
    for i := 0 to Lines.Count - 1 do begin
      S := Lines[i];
      if Pos(Placeholder, S) > 0 then begin
        StringChangeEx(S, Placeholder, Value, True);
        Lines[i] := S;
      end;
    end;
    Lines.SaveToFile(FileName);
  finally
    Lines.Free();
  end;
end;



procedure AddToPath();
var
  Path: string;
begin
  Path := ExpandConstant('{app}');
  if not RegQueryStringValue(HKEY_LOCAL_MACHINE, 'SYSTEM\CurrentControlSet\Control\Session Manager\Environment', 'Path', Path) then
    Path := ''
  else
    Path := Path + ';';
  Path := Path + ExpandConstant('{app}');
  RegWriteStringValue(HKEY_LOCAL_MACHINE, 'SYSTEM\CurrentControlSet\Control\Session Manager\Environment', 'Path', Path)
end;

procedure CurStepChanged(CurStep: TSetupStep);
begin
  if CurStep = ssPostInstall then
  begin
    AddToPath();
    UpdateConfigFile(ExpandConstant('{app}\config.ini'), 'Your KEY HERE.', ApiKeyPage.Values[0]);
  end;
end;
