@echo off

start cmd /k python main.py
start cmd /k "cd /d bot_core\cogs\music\data\lavalink && java -jar lavalink.jar"

pause
