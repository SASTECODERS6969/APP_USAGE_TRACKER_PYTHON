import psutil
import win32process
import win32gui
import time
import win32process

i = 0

while i <= 1:
    w=win32gui
    w.GetWindowText (w.GetForegroundWindow())
    pid = win32process.GetWindowThreadProcessId(w.GetForegroundWindow())
    time.sleep(0.1)
    print(psutil.Process(pid[-1]).name())