##############################################################################################
#### router setup code extracted from https://medium.com/swlh/creating-a-simple-router-simulation-using-python-and-sockets-d6017b441c09 
################################################################################################

import socket
import time
import calculateChecksum

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost",8000))
server.listen(2)

IP_server = "25.15.15.02"
MAC_server = "00:A0:C9:14:C8:29"

MAC_router = "02:A4:F9:16:D8:59"

while True:
	connection, address = server.accept()
	if(connection != None):
		print(connection)
		break

while True:
	e_header=""
	IP_header = ""
	
	print("\n Enter a message: ")
	message = raw_input()
	checksum = calculateChecksum.CalculateChecksum(message)
	print(checksum)
	destination = "23.23.10.10"
	if(destination == "23.23.10.10"):
		s_ip = IP_server
		IP_header = IP_header + s_ip + destination
		
		s_mac = MAC_server
		dest_mac = MAC_router
		
		e_header = e_header + s_mac + dest_mac
		
		packet = e_header + IP_header + message
		packet = str(packet).encode("utf-8")
		connection.send(packet)
	else:
		print("IP does not exist")
