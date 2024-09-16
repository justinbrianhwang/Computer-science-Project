.686P					; Pentium Pro
.model flat, stdcall	; flat segment model, standard call (window API)
.stack 4096				; 4KB stack

; prototype declaration
ExitProcess proto,dwExitCode:dword ; exit
DumpRegs proto			; print registers
DumpMem proto 			; print memory area
WriteHex PROTO			; write hexadecimal integer to output
WriteString PROTO		; write null-terminated string to output 
Crlf PROTO 				; output carriage-return / linefeed
