#Port Scanner Script

#The target will be IP address, user provides the input
#The user selects a specific target or a range of target IP addresses (For example either Port 80 or Ports 21-25)


import socket #sockets are needed to connect to ports
import threading
import queue

Target_IP = input("Enter your target IP address")
Select_Port = input ("Enter your target port (e.g. 80) or a range of ports to scan (eg. 21-25)")

