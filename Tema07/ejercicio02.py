import time
hora = time.strftime('%H') 
minutos = time.strftime('%M') 
if int(hora) >= 19:
	print ("a descansar") 
else:
	print ("faltan {} horas y {} minutos para descansar".format(18- int(hora), 59-int(minutos)))