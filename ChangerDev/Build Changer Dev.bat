@echo off
color 0A
:start
cls
if exist %systemdrive%\ProgramData\1.txt del %systemdrive%\ProgramData\1.txt
if defined version endlocal
echo This program allows you to install the needed SmartPTT build.
@echo.
echo -- WARNING --
echo Before using the program for build installing, make sure that you have the needed build in your local repository.
echo In case there is no needed build, copy it using the program downloader and then use the build for further work.
@echo.
echo - To begin to work with SPTT Version 9.1, enter 1
@echo.
echo - To begin to work with SPTT Version 9.2, enter 2
@echo.
echo - To open the local repository folder, enter "RF"
@echo.
set /p version="Enter your answer here: "
@echo.

:: -- Path Variables --

if "%version%"=="1" set var=9.1
if "%version%"=="2" set var=9.2
if "%version%" NEQ "1" (if "%version%" NEQ "2" ( if /i "%version%" NEQ "RF" ( ( echo Please, try again ) & pause & goto start ) ) )


if /i "%version%"=="RF" ( C:\WINDOWS\explorer.exe C:\ProgramData\Builds_SmartPTT ) & pause & goto start

if "%var%"=="9.1" (set repo=%systemdrive%\ProgramData\Builds_SmartPTT\SPTT_9.1)
if "%var%"=="9.2" (set repo=%systemdrive%\ProgramData\Builds_SmartPTT\SPTT_9.2)

set source=\\orpo-tfs-buildbot.elcom.local\Artifact share\Binaries (NOT ENCRYPTED, FAST BUILD)
set target=C:\Program Files (x86)\SmartPTT

:config_choice
cls & (@echo.
	) & ( echo ---- VERSION %var% Action Selection Window ----
	) & ( @echo. ) & ( echo ---- Choose the needed action and enter your answer below ----
	) & ( @echo. ) & ( echo - To install SmartPTT Enterprise build, enter "E".
	) & ( @echo. ) & ( echo - To install SmartPTT Plus build, enter "P".
	) & ( @echo. ) & ( echo - To install SmartPTT Basic build, enter "B".
	) & ( @echo. ) & ( echo - To install SmartPTT Monitoring build, enter "M".
	) & ( @echo. ) & ( echo - To install SmartPTT Radius-IP Enterprise build, enter "RE".
	) & ( @echo. ) & ( echo - To install SmartPTT Developer build, enter "D".
	) & ( @echo. ) & ( echo - To activate Downloader, enter "DD"
	) & ( @echo. ) & ( set /p choice="Enter the character(s) here: " ) 

if /i "%choice%" neq "e" ( if /i "%choice%" neq "p" ( if /i "%choice%" neq "b" ( if /i "%choice%" neq "m" ( if /i "%choice%" neq "d" ( if /i "%choice%" neq "re" (if /i "%choice%" neq "dd" ( echo Please, try again ) & pause & goto config_choice ) ) ) ) ) ) 
if /i "%choice%"=="e" ( set folderName=enterprise_2017)
if /i "%choice%"=="p" ( set folderName=plus_2017) 
if /i "%choice%"=="b" ( set folderName=basic_2017) 
if /i "%choice%"=="m" ( set folderName=monitoring_2017) 
if /i "%choice%"=="d" ( set folderName=dev_2017) 
if /i "%choice%"=="re" ( set folderName=radius_enterprise_2017) 

setlocal
if /i "%choice%"=="dd" ( @echo.
	) & ( set /p d_var="Please enter the needed build name ( or names ) here " )
if defined d_var ( >> %systemdrive%\ProgramData\1.txt echo %d_var%)
if defined d_var goto Deferred_Downloader
:: ----- Main script block -----

::-- Checking the repository folders --
cls
@echo.
if not exist "%repo%" (md "%repo%")

:: -- Checking the local build folders --

for /f "usebackq" %%A in (`dir /a:d /b "%repo%" ^| findstr /i /b "%folderName%"`) do (set NewBuildName=%%A)
setlocal
if "%NewBuildName%"=="" (echo "There is no requested build in the local repository folder. Please download it using the program Downloader") & pause & goto start
cls
if "%NewBuildName%" neq "" echo "%NewBuildName%"
:: -- Local Copy Unit --
@echo.
echo Please wait until the program finishes copying your local files to the SmartPTT folder
@echo.

for /f "usebackq tokens=1" %%A in (`tasklist ^| find /i "RSConfigurator.exe"`) do set config=%%A
if "%config%"=="RSConfigurator.exe" taskkill /t /f /im "RSConfigurator.exe"  

for /f "usebackq tokens=1" %%A in (`tasklist ^| find /i "Client.exe"`) do set client=%%A
if "%client%"=="Client.exe" taskkill /t /f /im "Client.exe"  

for /f "usebackq delims= tokens=*" %%A in (`net start ^| find /i "SmartPTT Radio Service"`) do set service=%%A 
if "%service%"=="   SmartPTT Radio Service " ( net stop "SmartPTT Radio Service" ) 

if exist "%target%\Client" (
rd /s /q "%target%\Client" & ( if exist "%target%\Client" rd /s /q "%target%\Client") ) 

if exist "%target%\Server" (
rd /s /q "%target%\Server" & ( if exist "%target%\Server" rd /s /q "%target%\Server") ) 
@echo.
xcopy /e /i /q "%repo%\%NewBuildName%\*.*" "%target%" && @echo. && echo All files were successfully copied!
	
:: Launch block
@echo.
echo Would you like to run SmartPTT Radioserver Configurator or SmartPTT Dispatcher? 
@echo.
echo To run SmartPTT Radioserver Configurator - Enter "C"
@echo.
echo To run SmartPTT Dispatcher - Enter "D"
@echo.
echo To run Both programs - Enter "B"
@echo.
echo To exit the Build Changer - Enter "Q"
@echo.

set /p enter="Enter your answer here:"
If /i "%enter%"=="C" start /D "%target%\Server\" RSConfigurator.exe & exit 
If /i "%enter%"=="D" start /D "%target%\Client\" Client.exe & exit
If /i "%enter%"=="B" (
(start /D "%target%\Server\" RSConfigurator.exe
) & ( start /D "%target%\Client\" Client.exe ) ) & exit
If /I "%enter%"=="Q" exit

:Deferred_Downloader
cls

for /f "usebackq tokens=1-6" %%a in ("%systemdrive%\ProgramData\1.txt") do (
( set first=%%a
) & ( set second=%%b
) & ( set third=%%c
) & ( set fourth=%%d
) & ( set fifth=%%e
) & ( set sixth=%%f ) )

:: --- The First Variable ---

( set deferred=%first%) 

:loop

if "%deferred%"=="" ( ( echo No builds are queued ) & ( pause ) & ( goto start ) )

if exist "%repo%\%deferred%" ( echo -- %deferred% -- You already have that build ) 

if not exist "%source%\%deferred%" ( cls & echo Please wait for the %deferred% build compiling ) & ( timeout /t 30 /nobreak ) & goto loop

if exist "%source%\%deferred%" ( if not exist "%repo%\%deferred%" ( echo Please wait until the program finishes copying %deferred% from TFS
	) & ( xcopy /i /e /q "%source%\%deferred%" "%repo%" ) && ( echo -- %deferred% -- Build was successfully copied to your local repository ) )

if exist "%repo%\%deferred%" ( if not exist "%repo%\%second%" ( ( set deferred=%second%) & goto loop ) )
if exist "%repo%\%deferred%" ( if not exist "%repo%\%third%" ( ( set deferred=%third%) & goto loop ) )
if exist "%repo%\%deferred%" ( if not exist "%repo%\%fourth%" ( ( set deferred=%fourth%) & goto loop ) )
if exist "%repo%\%deferred%" ( if not exist "%repo%\%fifth%" ( ( set deferred=%fifth%) & goto loop ) )
if exist "%repo%\%deferred%" ( if not exist "%repo%\%sixth%" ( ( set deferred=%sixth%) & goto loop ) )
if exist %systemdrive%\ProgramData\1.txt del %systemdrive%\ProgramData\1.txt
pause
goto start

