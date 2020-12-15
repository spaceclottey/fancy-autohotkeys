; Press alt + z to start spamming the parse article button and going to the next tab. To cancel, press alt+ x For when you need to parse dozens of articles in IE and don't wanna do it manually. 


#SingleInstance, Force
SendMode Input
SetWorkingDir, %A_ScriptDir%

#ifwinactive ahk_class IEFrame

		!z::
		loop {
			if stopit = 1
				{
				stopit = 0
				break
				}
		
		MouseClick, L, 111, 105
		send, ^{Tab}
		sleep, 500
		}
		return


		!x::
			MsgBox, 0, ,stopit !, .6
			stopit = 1
		return