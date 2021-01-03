#SingleInstance, Force
SendMode Input
SetWorkingDir, %A_ScriptDir%

; Stops SuperMemo Plan from constantly asking you if you want to save

; Save Plan When Starting Plan
	#IfWinActive ahk_class TPlanDlg

	~!b::
	send, ^s
	return

	$Esc::
	send, ^s
	send, {Esc}
	return
