REM --------------------------------------------------------------
REM DEPRECATED from v4.4, use pack-obfuscated-scripts.bat instead.
REM --------------------------------------------------------------

@ECHO OFF
REM
REM Sample script used to distribute obfuscated python scripts with py2exe
REM
REM Before run it, all TODO variables need to set correctly.
REM

SetLocal

REM TODO: zip used to update library.zip
Set ZIP=zip
Set PYTHON=C:\Python34\python.exe

REM TODO: Where to find pyarmor.py
Set PYARMOR_PATH=C:\Python34\Lib\site-packages\pyarmor

REM TODO: Absolute path of source
Set SOURCE=C:\Python34\Lib\site-packages\pyarmor\examples\py2exe

REM TODO: Output path of py2exe
REM       An executable binary file and library.zip generated by py2exe should be here
Set OUTPUT=%SOURCE%\dist

REM TODO: Entry name, no extension
Set ENTRY_NAME=hello

Set ENTRY_SCRIPT=%ENTRY_NAME%.py
Set ENTRY_EXE=%ENTRY_NAME%.exe

REM TODO: PyArmor project path to save project config file
Set PROJECT=C:\Python34\Lib\site-packages\pyarmor\build-for-py2exe

REM TODO: Comment next line if not to test obfuscated scripts
Set TEST_OBFUSCATED_SCRIPTS=1

REM Compressed python library generated by py2exe
Set LIBRARYZIP=%OUTPUT%\library.zip


REM Check Python
%PYTHON% --version
If NOT ERRORLEVEL 0 (
    Echo.
    Echo Python doesn't work, check value of variable PYTHON
    Echo.
    Goto END
)

REM Check Zip
%ZIP% --version > NUL
If NOT ERRORLEVEL 0 (
    Echo.
    Echo Zip doesn't work, check value of variable ZIP
    Echo.
    Goto END
)

REM Check PyArmor
If NOT EXIST "%PYARMOR_PATH%\pyarmor.py" (
    Echo.
    Echo No pyarmor found, check value of variable PYARMOR_PATH
    Echo.
    Goto END
)

REM Check Source
If NOT EXIST "%SOURCE%" (
    Echo.
    Echo No %SOURCE% found, check value of variable SOURCE
    Echo.
    Goto END
)

REM Check entry script
If NOT EXIST "%SOURCE%\%ENTRY_SCRIPT%" (
    Echo.
    Echo No %ENTRY_SCRIPT% found, check value of variable ENTRY_SCRIPT
    Echo.
    Goto END
)

REM Create a project
Echo.
Cd /D %PYARMOR_PATH%
%PYTHON% pyarmor.py init --type=app --entry=%ENTRY_SCRIPT% --src=%SOURCE% %PROJECT%
If NOT ERRORLEVEL 0 Goto END

REM Change to project path, there is a convenient script pyarmor.bat
cd /D %PROJECT%

REM This is the key, change default runtime path, otherwise dynamic library _pytransform could not be found
Echo.
Call pyarmor.bat config --runtime-path="" --manifest "global-include *.py, exclude %ENTRY_SCRIPT% setup.py pytransform.py, prune build, prune dist"

REM Obfuscate scripts without runtime files, only obfuscated scripts are generated
Echo.
Call pyarmor.bat build --no-runtime
If NOT ERRORLEVEL 0 Goto END

REM Copy pytransform.py and modified entry script to source
Echo.
Echo Copy pytransform.py to %SOURCE%
Copy %PYARMOR_PATH%\pytransform.py %SOURCE%

Echo Backup original %ENTRY_SCRIPT%
Copy %SOURCE%\%ENTRY_SCRIPT% %ENTRY_SCRIPT%.bak

Echo Move modified entry script %ENTRY_SCRIPT% to %SOURCE%
Move dist\%ENTRY_SCRIPT% %SOURCE%

REM Run py2exe
SetLocal
    Echo.
    Cd /D %SOURCE%
    %PYTHON% setup.py py2exe
    If NOT ERRORLEVEL 0 Goto END
EndLocal

Echo.
Echo Restore entry script
Move %ENTRY_SCRIPT%.bak %SOURCE%\%ENTRY_SCRIPT%

REM Generate runtime files only
Echo.
Call pyarmor.bat build --only-runtime --output runtime-files
If NOT ERRORLEVEL 0 Goto END

Echo.
Echo Copy runtime files to %OUTPUT%
Copy runtime-files\*.key runtime-files\*.lic runtime-files\_pytransform.dll %OUTPUT%

Echo.
Echo Compile obfuscated script .py to .pyc
%PYTHON% -m compileall dist
If NOT ERRORLEVEL 0 Goto END

REM Replace python scripts with obfuscated ones in zip file
Echo.
SetLocal
    Cd dist
    %ZIP% -r %LIBRARYZIP% *.pyc
    If NOT "%ERRORLEVEL%" == "0" Goto END
EndLocal

Echo.
Echo All the python scripts have been obfuscated in the output path %OUTPUT% successfully.
Echo.

REM Test obfuscated scripts
If "%TEST_OBFUSCATED_SCRIPTS%" == "1" (
    Echo.
    Echo Prepare to run %ENTRY_EXE% with obfuscated scripts
    PAUSE

    Cd /D %OUTPUT%
    %ENTRY_EXE%
)

:END

EndLocal
PAUSE