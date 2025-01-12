@echo off
REM Navigate to your Django project directory
cd D:\self\Business\SMM\Billing-System

REM Activate the virtual environment (if needed)
call C:\path\to\your\venv\Scripts\activate

REM Run the Django server
start cmd /k "python manage.py runserver"

REM Wait for the server to start (optional delay)
timeout /t 5 >nul

REM Open the browser with the Django server URL
start chrome http://127.0.0.1:8000
