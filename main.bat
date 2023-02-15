@echo off
:begin
echo Hello, please choose a program to continue
echo.
echo getpy: Python program to run get requests with many parameters
echo postpy: Python program to run post requests with many parameters
echo signuppy: Python program to run different types of requests with many lines of request headers (In development)
set /p startpro=

if "%startpro%" == "getpy" (
    echo starting get.py...
    start codeparts\get.py
    goto begin
)

if "%startpro%" == "postpy" (
    echo starting post.py...
    start codeparts\post.py
    goto begin
)

if "%startpro%" == "signuppy" (
    echo starting signup.py...
    start codeparts\signup.py
    goto begin
)
