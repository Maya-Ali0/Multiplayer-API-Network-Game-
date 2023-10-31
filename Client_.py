# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 12:42:28 2023

@author: Maya
"""

import socket
import time
from datetime import datetime
import uuid

#time functions
Date= datetime.now()
Time= Date.strftime("%H:%M:%S")

#Socket intialization
ClientSocket= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#gethostbyname :IP address of the local host
#gethostname:returns the host name of the current system under
#which the Python interpreter is executed.
Name= socket.gethostbyname(socket.gethostname())
Port= 3566
ClientSocket.connect((Name,Port))

#User Inputting the IP address of the desired http webpage
Userinput= input(" Insert IP Address of wanted http page: ")
Request="GET / HTTP/1.1\r\nHost: " + Userinput + "\r\n\r\n"
print(Request)

#start of RTT
RTTBegin= time.time()

#Send Request to Proxy server
ClientSocket.send(Request.encode())
#Message with request Details+ time
print("IP address of the desired http webpage"+ Userinput)
print("Time of access:"+ Time)
print("Accessing...")

#Recieve the request+ time
Response= ClientSocket.revc(4096).decode()
print("Time received: "+ Time)

#End of RTT
RTTEnd= time.time()

#RTT 
RTT= RTTEnd-RTTBegin
print ("Total round-trip time: "+ RTT+ "secs")
print("Physical MAC address: "+ uuid.getnode())

ClientSocket.close()

