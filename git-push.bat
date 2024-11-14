@echo off
cls

call rmdir /s /q .quarto
call rmdir /s /q docs

call git add *

call git commit --all --message="commit"

call git push origin main

pause
