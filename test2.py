import psutil

psutil.process_iter(attrs=None, ad_value=None)

# psutil.pid_exists(p.pid)

# for proc in psutil.process_iter(['pid', 'name', 'username']):
#     print(proc.info)

# psutil.pid_exists(21988)


"firefox.exe" in (p.name() for p in psutil.process_iter())