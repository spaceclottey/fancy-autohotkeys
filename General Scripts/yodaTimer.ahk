;Activate subtle yoda timer anywhere in the corner of the screen by pressing alt+why

;By TheTrueSquidward


#SingleInstance, Force
SendMode Input
SetWorkingDir, %A_ScriptDir%

!y::
		Progress,X1600 Y900 b w200,, Yoda Timer, My Title
		
		loop 5 { ;starting sound
			soundbeep, 400, 100
		}

		time = 0
		Loop 10 { ;make the amount of loops double the amount of minutes
			Progress, %time%  ; show how far it is
			sleep, 30000 ;every half a minute
			time += 15
		}

		sleep, 5000

		loop 5 { ; ending sound
			soundbeep, 900, 100
		}

		Progress, Off

		return