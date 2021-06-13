import binascii

def CalculateChecksum(message):
	
	length = len(message)
	sum_1 = message[0:length/2]
	sum_2 = message[length/2:]
	
	sum_1 = sum_1.encode('ascii')
	sum_2 = sum_2.encode('ascii')
	
	binary = ''.join(map(bin, bytearray(sum_1))) + ''.join(map(bin, bytearray(sum_2))) 

	checksum = ''
	for i in binary:
		if(i=='1'):
			checksum +='0'
		else:
			checksum += '1'
	
	file1 = open("checksum.txt", "w")
	file1.write(checksum)
	file1.close()
	return checksum


def check(message):
	length = len(message)
	sum_1 = message[0:length/2]
	sum_2 = message[length/2:]
	
	sum_1 = sum_1.encode('ascii')
	sum_2 = sum_2.encode('ascii')
	
	binary = ''.join(map(bin, bytearray(sum_1))) + ''.join(map(bin, bytearray(sum_2))) 

	checksum = ''
	for i in binary:
		if(i=='1'):
			checksum +='0'
		else:
			checksum += '1'
	
	file1 = open("checksum.txt","r+")
	a = file1.read()
	if(checksum == a):
		return True
	else:
		return False

