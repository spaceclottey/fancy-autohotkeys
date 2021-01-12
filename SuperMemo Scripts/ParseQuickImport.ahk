#SingleInstance, Force
SendMode Input
SetWorkingDir, %A_ScriptDir%


GroupAdd, SuperMemo, ahk_class TBrowser ;Browser
GroupAdd, SuperMemo, ahk_class TContents ;Content Window (Knowledge Tree)
GroupAdd, SuperMemo, ahk_class TElWind ;Element window
GroupAdd, SuperMemo, ahk_class TSMMain ;Toolbar	
GroupAdd, SuperMemo, ahk_exe PluginHost.exe ; PDF reader

;———————————————————Quick Import———————————————————

			;you need to have articleparser as your first bookmark


			!x::
			url = ; empties url variable
			article = ;empties article variable
			Clipboard = ;


			; Locates and presses 'Parse Article' button (must be your first bookmark)
			Send, {F6}
			Send, {F6}
			Send, {F6}
			Sleep, 100
			Send, {Enter}
			
			
			;Selects and copys the article
			Sleep, 2000
			Send, ^{a}
			sleep, 50
			Send, ^{c}
			ClipWait, 2
				IF ErrorLevel{
					SplashTextOn,,,Error`, try again,
					Sleep,500
					SplashTextOff
					return
				}
			article := ClipboardAll
			Clipboard = 
			sleep, 500



			;copy url
			send, ^l
			sleep, 50
			Send, ^c ;Copies the url as it passes omnibox
			ClipWait, 2
				IF ErrorLevel{
					SplashTextOn,,,Error`, try again,
					Sleep,500
					SplashTextOff
					return
				}
			url = #Link:%Clipboard%
			send, {Esc}


			;Pasting Article
			winactivate ahk_group SuperMemo
			WinWaitActive, ahk_group SuperMemo, , 2
			if ErrorLevel{

				MsgBox, Open SuperMemo.
				return
				}	
			Clipboard := article
			sleep, 500 
			send, ^n


			;Pasting url in SuperMemo
			send, q
			send, {Enter}
			send, %url%
		
            ;Filter
            send, {F6}
            send, ^{a}
            sleep, 50
            send, s
            send, {Enter}
            send, {Enter}
			return