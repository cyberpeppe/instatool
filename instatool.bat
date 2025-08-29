@echo off
REM Batch wrapper to run instatool on Windows
cd /d "%~dp0"

REM Prefer py launcher if available
where py >nul 2>&1
if %ERRORLEVEL%==0 (
    py unfollow.py
) else (
    python unfollow.py
)

echo.
pause
