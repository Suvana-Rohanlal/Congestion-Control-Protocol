##############################################################################################
#### router setup code extracted from https://medium.com/swlh/creating-a-simple-router-simulation-using-python-and-sockets-d6017b441c09 
################################################################################################

import socket
import time

router = ("localhost", 8200)

IP_1 = "23.23.10.10"
MAC_1 = "00:1B:44:11:3A:B7"
user1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

time.sleep(1)
user1.connect(router)

while True:
	received = (user1.recv(1024)).decode("utf-8")
	mac_address_source = received[0:17]
	mac_address_dest = received[17:34]
	ip_address_source = received[34:45]
	ip_address_dest = received[45:56]
	message = received[56:]
	
	print("Message: "+message)

