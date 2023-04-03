@echo off
:begin
cd codeparts
echo Hello, please choose a program to continue
echo.
set /p startpro=

python %startpro%

echo Invalid program try again later.