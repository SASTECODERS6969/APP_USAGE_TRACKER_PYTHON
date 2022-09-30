import wmi

f = wmi.WMI()

# for process in f.Win32_Process():
    # print(f"{process.ProcessId:<10} {process.Name}")
    
flag = 0
  
# Iterating through all the running processes
for process in f.Win32_Process():
    if "firefox.exe" == process.Name:
        # print("firefox is Running")
        flag = 1
        break
  
# if flag == 0:
    # print("firefox is not Running")


for process in f.Win32_Process():
    if "vlc.exe" == process.Name:
        # print("vlc is Running")
        flag = 2
        break
  
# if flag == 0:
    # print("vlc is not Running")


for process in f.Win32_Process():
    if "Spotify.exe" == process.Name:
        # print("vlc is Running")
        flag = 3
        break
  
# if flag == 0:
    # print("spotify is not Running")


for process in f.Win32_Process():
    if "DroidCamApp.exe" == process.Name:
        # print("droidcam is Running")
        flag = 4
        break
  
if flag == 0:
    # print("droidcam is not Running")


for process in f.Win32_Process():
    if "chrome.exe" == process.Name:
        # print("chrome is Running")
        flag = 5
        break
  
if flag == 0:
    # print("chrome is not Running")

while True():
    if 