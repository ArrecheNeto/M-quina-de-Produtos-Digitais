@echo off
cd /d "%~dp0"
python painel-server.py 2>nul || py painel-server.py
pause
