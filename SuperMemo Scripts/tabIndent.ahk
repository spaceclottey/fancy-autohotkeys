; Press Tab to actually indent. Use Ctrl+T instead to switch components

#SingleInstance, Force
SendMode Input
SetWorkingDir, %A_ScriptDir%

#IfWinActive, ahk_class TElWind

scF::   ; Tab Act like Tab
	Loop, 8{
	send, {space}
	}

    LAlt & scF::AltTab