@echo off
cls

call conda activate base

call quarto preview "d:/My_Projects/blog/index.qmd"

pause
