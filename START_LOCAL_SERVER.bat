@echo off
cd /d "%~dp0"
where python >nul 2>nul
if errorlevel 1 (echo Python 3 is not installed or not on PATH. Install it first. & pause & exit /b 1)
echo HenJB local offline server on port 8080
echo Keep this window open while using the PS4.
python -m http.server 8080 --bind 0.0.0.0
pause
