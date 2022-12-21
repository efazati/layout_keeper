^!1::
Run, C:\apps\shortcuts\Browse.cmd
If WinExist ("ahk_exe firefox.exe") {
	WinActivate, ahk_exe firefox.exe
}
return

^!2::
Run, C:\apps\shortcuts\Code.cmd
If WinExist ("ahk_exe firefox.exe") {
	WinActivate, ahk_exe firefox.exe
}
If WinExist ("ahk_exe Code.exe") {
	WinActivate, ahk_exe Code.exe
}
return

^!3::
Run, C:\apps\shortcuts\Chat.cmd
If WinExist ("ahk_exe firefox.exe") {
	WinActivate, ahk_exe firefox.exe
}
return

^!4::
Run, C:\apps\shortcuts\Standup.cmd
return

^!5::
Run, C:\apps\shortcuts\Remote.cmd
return

^!6::
Run, C:\apps\shortcuts\Meet.cmd
If WinExist ("ahk_exe firefox.exe") {
	WinActivate, ahk_exe firefox.exe
}
return