#Port Scanner Script

#The target will be IP address, user provides the input
#The user selects a specific target or a range of target IP addresses (For example either Port 80 or Ports 21-25)


import socket #sockets are needed to connect to ports
import threading
import queue

Target_IP = input("Enter your target IP address")
Select_Port = input ("Enter your target port (e.g. 80) or a range of ports to scan (eg. 21-25)")


if "-" in Select_Port:                                        #If a range is ports if given such as "21-25", and hence there is a presence of a dash "-"
    start_port, end_port = map(int, Select_Port.split("-"))   #Then we can split that string into 2 and convert them to integers giving us the start and end of the range. i.e ["21", "25"]
    Port_Range = range(start_port, end_port) + 1              #Port_Range is the range of ports we will use later for scanning 
    
else
    Port_Range = [int(Select_Port)]                           #If only a single port number was provided, then Port_Range contains the value of that single integer.
