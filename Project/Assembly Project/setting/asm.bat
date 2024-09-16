REM asm.bat - batch file for assemble & link assembly programs

@echo off
ml /coff /c /Zi /Fl %1.asm 
if errorLevel 1 goto terminate
link %1.odj user32.lib kernel32 /subsystem:console /debug
: terminate
