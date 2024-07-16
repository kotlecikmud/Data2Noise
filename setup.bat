@echo off

REM check python version
python --version

REM Check for updates
git pull

REM Install/upgarde pip
python.exe -m pip install --upgrade pip

REM Install required libraries
pip install -r requirements.txt

pause
