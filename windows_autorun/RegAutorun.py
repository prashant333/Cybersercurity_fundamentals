import os, shutil, winreg

filedir = os.path.join(os.getcwd(), "Temp")
filename = "benign.exe"
filepath = os.path.join(filedir, filename)

if os.path.isfile(filepath):
    os.remove(filepath)

os.system("Python BuildExe.py")

shutil.move(filename,filedir)

regkey = 1

if regkey < 2:
    reghive = winreg.HKEY_CURRENT_USER
else:
    reghive = winreg.HKEY_LOCAL_MACHINE
if (reghive % 2) == 0:
    regpath = "SOFTWARE\Microsoft\Windows\CurrentVersion\Run"

else:
    regpath = "SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce"

reg = winreg.ConnectRegistry(None, reghive)
key = winreg.OpenKey(reg, regpath, 0, access=winreg.KEY_WRITE)
winreg.SetValueEx(key, "SecurityScan", 0, winreg.REG_SZ, filepath)
