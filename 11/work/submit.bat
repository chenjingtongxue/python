@echo off
set WRITE_Y=0
if exist \\TEACHER201\d$\result\STU20116.txt  (@for /f "tokens=2 delims=:" %%i in (\\TEACHER201\d$\result\STU20116.txt) do set STUID=%%i) && echo ***���Ѿ��ύ���ˣ�����ʾ����ԭ�ύ���ݣ�Y���򲻸��ǣ�N����ȫ�����ǣ�A������ctrl+c�˳���***  & set WRITE_Y=1 & goto end
:input
set STUID=
set /p STUID=������ѧ��/����(�磺10111520333�������Իس�������:
echo  ��ȷ������ѧ��/�����Ƿ�Ϊ��[%STUID%]
set Selection=
set /p Selection=ȷ���밴Y��y��ֱ�ӻس����������밴N��n������Իس�������:
if "%Selection%" == "Y" goto next
if "%Selection%" == "y" goto next
if "%Selection%" == "" goto next
goto input
:next
echo ѧ�ţ�������:%STUID%: > \\TEACHER201\d$\result\STU20116.txt
:end
@echo on
xcopy c:\work\*.* \\TEACHER201\d$\result\%STUID%\ /s /e /h 
@echo off
if %WRITE_Y% == 1 goto end2
if not errorlevel 1 goto end2
echo.
echo ***��������ѧ���������䲻���пո��\������/���������ַ��������������롣***
echo.
del \\TEACHER201\d$\result\STU20116.txt
goto input
:end2
exit
