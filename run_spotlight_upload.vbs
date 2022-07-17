Set WshShell = CreateObject("WScript.Shell")
return = WshShell.Run("cmd /C cd C:\Users\Wiktor\Desktop\spotlight && npm start ", 0, true)