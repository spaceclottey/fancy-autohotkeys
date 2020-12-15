#SingleInstance, Force
SendMode Input
SetWorkingDir, %A_ScriptDir%

; Automatically dismisses the 'script error' box in supermemo whenever it shows up, making it easier to use the in-supermemo browser

Loop {
    WinWaitActive, Script Error
    send, n
}

