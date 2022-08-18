# building a basic port scanner.
import sys
from datetime import datetime
import socket

print("Enter ip address: ")
if len(sys.argv) == 2:
    # fetch the target address from passed arguments
    target = socket.gethostbyname(sys.argv[1])

# if the passed arguments is invalid, inform the user of proper syntax
else:
    print("invalid number of arguments passed.")
    print("Please find valid syntax below")
    print("python3 <file_name>.py <ip_address>")

# adding a banner for display.

print("*"*10)
print("scanning the target: {}".format(target))
print("Time started :" + str(datetime.now()))
print("*"*10)

# Scanning ports

try:
    for port in range(1, 86):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print("Port {} is open".format(port))
        s.close()

except KeyboardInterrupt:
    print("\n Exiting scanner")
    sys.exit()
except socket.gaierror:
    print("\n Hostname could not be resolved.")
    sys.exit()
except socket.error:
    print("\n Couldn't connect to server.")
    sys.exit()

