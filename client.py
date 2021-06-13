##############################################################################################
#### router setup code extracted from https://medium.com/swlh/creating-a-simple-router-simulation-using-python-and-sockets-d6017b441c09 
################################################################################################

import socket
import time
import calculateChecksum

router = ("localhost", 8200)

IP_1 = "23.23.10.10"
MAC_1 = "00:1B:44:11:3A:B7"
user1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
MAC_router = "02:A4:F9:16:D8:59"
time.sleep(1)
user1.connect(router)

while True:
	received = (user1.recv(1024)).decode("utf-8")
	mac_address_source = received[0:17]
	mac_address_dest = received[17:34]
	ip_address_source = received[34:45]
	ip_address_dest = received[45:56]
	message = received[56:]
	
	check = calculateChecksum.check(message)
	if check==True:
		print("---------------------------------------------")
		print("The message is sent from ",ip_address_source)
		print("The message is - ",message)
		print("----------------------------------------------")
	else:
		IP_hearder=''
		IP_header = IP_header + IP_1 + ip_address_source
		
		s_mac = MAC_1
		dest_mac = MAC_router
		
		e_header = e_header + s_mac + dest_mac
		
		packet = e_header + IP_header + "Incorrect message received"
		packet = str(packet).encode("utf-8")
		connection.send(packet)
