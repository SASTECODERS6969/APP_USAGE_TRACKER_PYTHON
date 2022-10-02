import win32gui
import psutil
import win32process

windowTile = ""; 


while ( True ) :
    w=win32gui

    w.GetWindowText (w.GetForegroundWindow())
    pid = win32process.GetWindowThreadProcessId(w.GetForegroundWindow())

    newWindowTile = psutil.Process(pid[-1]).name()
    # newWindowTile = w.GetWindowText (w.GetForegroundWindow());        
    if( newWindowTile != windowTile ):
        windowTile = newWindowTile ; 
        # print(psutil.Process(pid[-1]).name())
        print( windowTile );              

