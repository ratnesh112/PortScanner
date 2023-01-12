#!/bin/python3

import sys
import socket
from datetime import datetime 

if len(sys.argv)==2:
	target = socket.gethostbyname(sys.argv[1])
else:
	print("argument is invalid,")
	print("Syntax: python3 scanner.py <ip>")
	
print("-" * 50)
print("Scanning Target "+target)
print("Time started; "+str(datetime.now()))
print("-" * 50)


try: 
	for port in range(0,1024):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port))
		if result == 0:
			print(f"Port {port} is open")
		s.close()

except KeyboardInterrupt:
	print("\n Scanning Ended. ")
	sys.exit()

except socket.gaierror:
	print("host not resolve. ")
	sys.exit()

except socket.error:
	print("Sever Not Found.")
	sys.exit()