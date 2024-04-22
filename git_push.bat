@echo off
cls

call conda activate base

call rmdir /s /q .git
call rmdir /s /q .quarto
call rmdir /s /q docs

echo init
call git init
echo git remote add origin
call git remote add origin https://github.com/sergeyyurkov1/sergeyyurkov1.github.io.git
@REM echo quarto render
@REM call quarto render
echo git add
call git add *

echo git commit
call git commit --all --message="commit"

echo git push
call git push --force origin main

pause
