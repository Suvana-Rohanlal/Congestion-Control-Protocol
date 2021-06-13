def speedUp(packetsNum):
	delay=0
	if(packetsNum>5):
		delay = packetsNum/5 +5
	return delay


packets1 = 20
packets2 = 40
packets3 = 10

  
print("The transmission delay for "+ str(packets1)+ " is "+str(speedUp(packets1)))
print("The transmission delay for "+ str(packets2)+ " is "+str(speedUp(packets2)))
print("The transmission delay for "+ str(packets3)+ " is "+str(speedUp(packets3)))

