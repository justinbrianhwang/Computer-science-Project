REM asm.bat - batch file for assemble & linking assembly programs

@echo off
SET PATH=C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Tools\MSVC\14.29.30133\bin\Hostx86\x86;%PATH%
SET INCLUDE=C:\Program Files (x86)\Windows Kits\10\Include\10.0.22621.0\um;%INCLUDE%
SET LIB=C:\Program Files (x86)\Windows Kits\10\Lib\10.0.22621.0\um\x86;%LIB%

ml /c /coff /Zi /Fl %1.asm 

link %1.obj print.lib kernel32.lib user32.lib /subsystem:console /debug
: terminate ; Link the object file with libraries
