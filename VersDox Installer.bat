@echo off

title VersDox Installer

:: Detecta si tiene conexion a internet

echo.
echo [#] Detecting for a internet or wi-fi conection, please wait..
timeout 2 >nul
echo.

ping www.google.com -n 2 >nul

if %errorlevel% == 0 goto pip

cls
echo.
echo [X] You need an internet or wi-fi connection to install VersDox Dependencies
echo.
pause>nul
exit

:pip
echo [#] Detecting if pip is installed to install VersDox Dependencies...
timeout 2 >nul
pip >nul
if %errorlevel% == 0 goto dependencias

echo.
echo [X] You need to have pip installed to install VersDox Dependencies.
echo.
pause>nul
exit

:dependencias
pip install colorama && pip install requests_futures && pip install torrequest
echo.
echo [#] Correctly installed VersDox dependencies
pause >nul
exit
