@echo off
cls

call rmdir /s /q .git
call rmdir /s /q .quarto
call rmdir /s /q docs

call git init
call git remote add origin https://github.com/sergeyyurkov1/sergeyyurkov1.github.io.git

@REM call quarto render

call git add *

call git commit --all --message="commit"

call git push --force origin main

pause
