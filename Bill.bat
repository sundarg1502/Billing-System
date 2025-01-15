@echo off
REM Navigate to the Django project directory relative to the script location
cd "%~dp0Billing-System"

REM Run the Django server
start cmd /k "python manage.py runserver"

REM Wait for the server to start (optional delay)
timeout /t 5 >nul

REM Open the browser with the Django server URL
start chrome http://127.0.0.1:8000
