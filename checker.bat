ECHO OFF
TITLE GANO HWID CHECKER
ECHO **********************************
Color 3
ECHO **********************************
:start
color 3
cls
wmic diskdrive get model, serialnumber
ECHO CPU 
wmic cpu get serialnumber
ECHO BIOS
wmic bios get serialnumber
ECHO Motherboard
wmic baseboard get serialnumber
ECHO smBIOS UUID
wmic path win32_computersystemproduct get uuid
getmac
timeout /t 3 >nul
exit