#SingleInstance, Force
SendMode Input
SetWorkingDir, %A_ScriptDir%

;Change the paths to the files in the comments



Loop, Read, C:\Users\space\OneDrive\AutoHotkey\Text_References\importqueue.txt
{
run, %A_LoopReadLine%
if ErrorLevel{
	Continue
}
sleep, 700
}

SplashTextOn, , , , Starting Landing Bay Import Soon...
; sleep, 10000

MsgBox, 4, , Ready to Import to root SuperMemo folder?, 20  ; 5-second timeout.
IfMsgBox, No
    Return  ; User pressed the "No" button.
IfMsgBox, Timeout
    Return ; i.e. Assume "No" if it timed out.
;run, C:\Users\space\OneDrive\AutoHotkey\SuperMemo\landingBayImport.ahk ;Add the path to the file


MsgBox, 4, , Successful import? (Would you like to delete the links in queue?), 10
IfMsgBox, No
    Return  ; User pressed the "No" button.
IfMsgBox, Timeout
    Return ; i.e. Assume "No" if it timed out.;
msgbox, deleting links (terminate ahk to cancel)
FileRecycle, C:\Users\space\OneDrive\AutoHotkey\importqueue.txt



Flash:
SplashTextOn, , , , Running
sleep, 500
SplashTextOff
return


#IfWinActive ahk_class Chrome_WidgetWin_1

; Add to Queue

^j::
send, ^l
sleep, 50
send, ^c
MsgBox,, Added to queue, Added to queue, 0.5
sleep, 500
FileAppend, "C:\Program Files\Internet Explorer\iexplore.exe" %Clipboard% `n, C:\Users\space\OneDrive\AutoHotkey\Text References\importqueue.txt ; Add the path to your file
return