@echo off
title ✦ AryaCart Go Live ✦
color 0A
cls
echo ===================================================
echo             ✦ AryaCart Go Live Redirector ✦
echo ===================================================
echo.

:: Check if Django server is already running on port 8000
netstat -ano | findstr :8000 > nul
if %errorlevel% equ 0 goto :server_running

echo [START] Django server is not active. Starting server...

rem Look for virtual environment in parent directories
if exist "%~dp0..\venv\Scripts\python.exe" goto :use_venv
if exist "%~dp0..\env\Scripts\python.exe" goto :use_env

rem Check py launcher
py --version >nul 2>&1
if %errorlevel% equ 0 goto :use_py

rem Check python command
python --version >nul 2>&1
if %errorlevel% equ 0 goto :use_python

echo [ERROR] Python is not installed or not in system PATH!
echo Please install Python and make sure it is in PATH.
pause
exit

:use_venv
echo [VENV] Found venv virtual environment. Using it...
start "AryaCart Server" "%~dp0..\venv\Scripts\python.exe" "%~dp0..\manage.py" runserver
goto :after_start

:use_env
echo [VENV] Found env virtual environment. Using it...
start "AryaCart Server" "%~dp0..\env\Scripts\python.exe" "%~dp0..\manage.py" runserver
goto :after_start

:use_py
echo [PY] Using Python launcher py...
start "AryaCart Server" py "%~dp0..\manage.py" runserver
goto :after_start

:use_python
echo [SYSTEM] Using system python...
start "AryaCart Server" python "%~dp0..\manage.py" runserver
goto :after_start

:after_start
echo [WAIT] Waiting for server to initialize (4 seconds)...
timeout /t 4 /nobreak > nul
goto :open_browser

:server_running
echo [OK] Django server is already active on port 8000!
echo.

:open_browser
echo [REDIRECT] Opening AryaCart Homepage in your default browser...
start http://127.0.0.1:8000/
echo.
echo ===================================================
echo Redirected successfully! Happy Shopping! ❤️
echo ===================================================
timeout /t 3 > nul
exit
