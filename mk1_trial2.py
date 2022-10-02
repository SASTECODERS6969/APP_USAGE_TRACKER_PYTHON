from ctypes.wintypes import HWND
from win32gui import GetWindowText, GetForegroundWindow
import time
# from watchpoints import watch



while True:
    active_window = (GetWindowText(GetForegroundWindow()))
    # print(active_window)

