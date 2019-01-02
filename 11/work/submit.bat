@echo off
set WRITE_Y=0
if exist \\TEACHER201\d$\result\STU20116.txt  (@for /f "tokens=2 delims=:" %%i in (\\TEACHER201\d$\result\STU20116.txt) do set STUID=%%i) && echo ***您已经提交过了！按提示覆盖原提交内容（Y）或不覆盖（N）或全部覆盖（A），按ctrl+c退出。***  & set WRITE_Y=1 & goto end
:input
set STUID=
set /p STUID=请输入学号/姓名(如：10111520333张敏，以回车结束）:
echo  请确认您的学号/姓名是否为：[%STUID%]
set Selection=
set /p Selection=确认请按Y或y或直接回车，重新输入按N或n（最后以回车结束）:
if "%Selection%" == "Y" goto next
if "%Selection%" == "y" goto next
if "%Selection%" == "" goto next
goto input
:next
echo 学号（姓名）:%STUID%: > \\TEACHER201\d$\result\STU20116.txt
:end
@echo on
xcopy c:\work\*.* \\TEACHER201\d$\result\%STUID%\ /s /e /h 
@echo off
if %WRITE_Y% == 1 goto end2
if not errorlevel 1 goto end2
echo.
echo ***输入有误（学号与姓名间不能有空格或‘\’、‘/’等特殊字符），请重新输入。***
echo.
del \\TEACHER201\d$\result\STU20116.txt
goto input
:end2
exit
