##############################################################################################
#### router setup code extracted from https://medium.com/swlh/creating-a-simple-router-simulation-using-python-and-sockets-d6017b441c09 
################################################################################################

import socket
import time

router = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
router.bind(("localhost",8100))

send = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
send.bind(("localhost",8200))

MAC_router = "02:A4:F9:16:D8:59"

server = ("localhost", 8000)

IP_1 = "23.23.10.10"
MAC_1 = "00:1B:44:11:3A:B7"
IP_2 = "23.23.10.15"
MAC_2 = "00:1B:44:11:3B:C7"

send.listen(4)

user1 = None
user2 = None

while(user1==None):
	user, address = send.accept()
	
	if(user1==None):
		user1=user
		print("user 1 is online")

arp_table_socket = {IP_1 : user1, IP_2 : user2}
arp_table_mac = {IP_1 : MAC_1, IP_2 : MAC_2}

router.connect(server)

while True:
	received = (router.recv(1024)).decode("utf-8")
	mac_address_source = received[0:17]
	mac_address_dest = received[17:34]
	ip_address_source = received[34:45]
	ip_address_dest = received[45:56]
	message = received[56:]
	
	print("---------------------------------------------")
	print("The destination IP address is ",ip_address_dest)
	print("The message is - ",message)
	print("----------------------------------------------")
	
	e_header = MAC_router + arp_table_mac[ip_address_dest]
	IP_header = ip_address_source + ip_address_dest
	packet = e_header + IP_header + message
	packet = str(packet).encode("utf-8")
	dest_socket = arp_table_socket[ip_address_dest]
	dest_socket.send(packet)
	time.sleep(2)
