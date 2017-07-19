import cv2
import sys
import numpy as np
from time import time
from time import clock
#abrir la webcam
#cap=cv2.VideoCapture(0)
centroPantalla = (315, 80)
centroPantallaMensaje = (150, 300)
salirPantalla=(675, 470)

rojof = (10, 300)
azulf = (275, 370)
amarillof = (275, 470)

numeroRojo = 1
numeroAzul = 2
numeroAmarrillo = 3
variable = 0
suma = 0
num = 0
rep = 1
tb = 0
tiempo_pantalla=0
varfinal = 0 


#Create a imagen with the size of the video
def img(img1,img2,xpos,ypos):
    rows2,cols2,channels2 = img2.shape
    rows1,cols1,channels1 = img1.shape
    print (str(rows2)+'x'+str(rows1))
    aux = np.zeros((rows2, cols2, 3), dtype = "uint8")
    for i in range(rows1):
        for j in range(cols1):
            aux[xpos+i,ypos+j]=img1[i,j]
    return aux
#Start the game
#game = Game()
#Select camera
captura = cv2.VideoCapture(0)
#Load all images
arriba=cv2.imread("images/marco-arriba_opt.png") 
abajo=cv2.imread("images/marco-abajo_opt.png")
izquierda=cv2.imread("images/marco-izquierda_opt.png")
derecha=cv2.imread("images/marco-derecha_opt.png")

rojof=cv2.imread("images/rojof.png")
azulf=cv2.imread("images/azulf.png")
amarillof=cv2.imread("images/amarillof.png")

num1=cv2.imread("images/num1.jpg")
num2=cv2.imread("images/num2.jpg")
num3=cv2.imread("images/num3.jpg")	

#reini=cv2.imread("images/Reiniciar2.png")

#all variables  
bdx=15;
bdy=184;
base=150;
altura=150;
radio=20;
c_punt=[0,0,0]
l_p=10;
#capture the video
_, imagen1 = captura.read()
#Ceate a mask with the directions, exit and restar
salir=cv2.imread("images/salir2.jpg")
up=img(arriba,imagen1,bdx-150+base,bdy-50+base)
down=img(abajo,imagen1,bdx+base-8,bdy-50+base)
left=img(izquierda,imagen1,bdx+base-120,bdy-70+altura)
right=img(derecha,imagen1,bdx+base-138,bdy+190+altura)

rojoff=img(rojof,imagen1,bdx+base+18,bdy-320+base)
azulff=img(azulf,imagen1,bdx+base+118,bdy-320+altura)
amarilloff=img(amarillof,imagen1,bdx+base+218,bdy-320+altura)

num1f=img(num1,imagen1,bdx+base+33,bdy-230+base)
num2f=img(num2,imagen1,bdx+base+128,bdy-230+altura)
num3f=img(num3,imagen1,bdx+base+228,bdy-230+altura)

exit=img(salir,imagen1,bdx-320+base,bdy+455+altura-50)
#reiniciar=img(reini,imagen1,bdx+base+200,bdy-300+altura)
dire=cv2.add(up,down)
dire=cv2.add(dire,left)
dire=cv2.add(dire,right)

dire=cv2.add(dire,rojoff)
dire=cv2.add(dire,azulff)
dire=cv2.add(dire,amarilloff)

dire=cv2.add(dire,num1f)
dire=cv2.add(dire,num2f)
dire=cv2.add(dire,num3f)

dire=cv2.add(dire,exit)
#dire=cv2.add(dire,reiniciar)
while varfinal <= 1:
	b = clock()
	#cv2.rectangle(imagen1,(550,150),(280,30),(0,0,0),2)
	
	_, imagen1 = captura.read()
	imagen1 = cv2.flip(imagen1,1)
	imagen = cv2.add(imagen1,dire)    
	salirmami=cv2.imread("images/imagenResultado1.jpg")


	#arriba[y_offset:y_offset+img1.shape[0], x_offset:x_offset+img1.shape[1]] = img1

	
	#cv2.rectangle(imagen, (bdy+100+altura,bdx-150+base), (bdy-50+altura,bdx+base),(255,0,0), 2) #up  150x150 pxls
	#cv2.rectangle(imagen, (bdy+100+altura,bdx+150+base ), (bdy-50+altura,bdx+300+base),(255,0,0), 2) #dowm 150x150 pxls
	#cv2.rectangle(imagen, (bdy-50+altura,bdx+base), (bdy-200+altura,bdx+150+base),(255,0,0), 2) #left 150x150 pxls
	#cv2.rectangle(imagen, (bdy+250+altura,bdx+base), (bdy+100+altura,bdx+150+base),(255,0,0), 2) #rigth 150x150 pxls
	cv2.rectangle(imagen, (bdy+505+altura,bdx+260+base), (bdy+405+altura,bdx+160+base),(0,0,255), 2) #exit 100x100 pxls
	#cv2.rectangle(imagen, (bdy-300+altura,bdx+base+200 ), (bdy-200+altura,bdx+base+300),(255,0,0), 2) #Restar  100x100 pxls
	hsv = cv2.cvtColor(imagen1, cv2.COLOR_BGR2HSV)

    #Show the video
	#cv2.rectangle(imagen,(550,150),(280,30),(0,0,0),2)
	#cv2.imshow('Camara', imagen)

	#convertir a bgr de HSV
	hsv=cv2.cvtColor(imagen1,cv2.COLOR_BGR2HSV)

	#rango de rojo
	red_lower=np.array([136,87,111],np.uint8)
	red_upper=np.array([180,255,255],np.uint8)

	#rango de azul
	blue_lower=np.array([99,115,150],np.uint8)
	blue_upper=np.array([110,255,255],np.uint8)

	#rango de amarillo
	yellow_lower=np.array([22,60,200],np.uint8)
	yellow_upper=np.array([60,255,255],np.uint8)

	#buscando el rango en la imagen
	red=cv2.inRange(hsv, red_lower, red_upper)
	blue=cv2.inRange(hsv,blue_lower,blue_upper)
	yellow=cv2.inRange(hsv,yellow_lower,yellow_upper)


	kernal = np.ones((5 ,5), "uint8")
	red=cv2.dilate(red, kernal)
	res=cv2.bitwise_and(imagen, imagen, mask = red)

	blue=cv2.dilate(blue,kernal)
	res1=cv2.bitwise_and(imagen, imagen, mask = blue)

	yellow=cv2.dilate(yellow,kernal)
	res2=cv2.bitwise_and(imagen, imagen, mask = yellow)


	#en caso de que sea rojo
	(_,contours,hierarchy)=cv2.findContours(red,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

	center = None

	cv2.putText(imagen, "Presiona q para salir", salirPantalla, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

	cv2.putText(imagen, "1 punto", salirPantalla, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 3)
	cv2.putText(imagen, "2 puntos", salirPantalla, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 3)
	cv2.putText(imagen, "3 puntos", salirPantalla, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 3)

	if len(contours)>0:
    	# Busca el contorno mas grande
		c = max(contours, key=cv2.contourArea)
		((x, y), radius) = cv2.minEnclosingCircle(c)
		M = cv2.moments(c)
		center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

		if radius > 10:
            # Dibuja el circulo 
			cv2.circle(imagen, (int(x), int(y)), int(radius), (0,0,255), 2)
			cv2.circle(imagen, center, 5, (0,0,255), -1)
			cv2.putText(imagen, "Rojo", (int(x - radius), int(y - (radius + 10))), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
			
            	# Ubica el objeto en el cuadro
			if x > 750 and x < 800 and y > 350 and y < 400:
				#print('tuculito')
				exit()



			if x < 550 and y < 150:
				#cv2.putText(img1, "Amarillo. Tienes 3 puntos.", centroPantallaMensaje, cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 4)
				print('inicia el tiempo')
				#tiempo_inicial = time() 
				#tiempo_final = time()  
				#tiempo_ejecucion = (tiempo_final - tiempo_inicial)* 1000
				#print(tiempo_ejecucion)
				#if int(tiempo_ejecucion) > 5:
				print(int(b))
				if b - tb > 3:
					print('cada 3 segundos rojo')
					print('se acabo el tiempo rojo')
					variable = 1
					#variable = 1
					if variable == 0:
						suma = 1
					elif variable == 1:
						suma = suma + numeroRojo
					elif variable == 2:
						suma = suma + numeroAzul
					elif variable == 3:
						suma = suma + numeroAmarrillo
					tiempo_inicial = time() 
					tiempo_final = time()  
					tb = b
				cv2.putText(imagen, "La suma es: "+str(suma), centroPantallaMensaje, cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 4)
			
				
	i=0

	#en caso de que sea azul
	(_,contours,hierarchy)=cv2.findContours(blue,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

	if len(contours)>0:
    	# Busca el contorno mas grande
		c = max(contours, key=cv2.contourArea)
		((x, y), radius) = cv2.minEnclosingCircle(c)
		M = cv2.moments(c)
		center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

		if radius > 10:
            # Dibuja el circulo 
			cv2.circle(imagen, (int(x), int(y)), int(radius), (255,0,0), 2)
			cv2.circle(imagen, center, 5, (255,0,0), -1)
			cv2.putText(imagen, "Azul", (int(x - radius), int(y - (radius + 10))), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)

            	# Ubica el objeto en el cuadro
			if x < 550 and y < 150:
				#cv2.putText(imagen1, "Azul. Tienes 3 puntos.", centroPantallaMensaje, cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 4)
				print('inicia el tiempo')
				#tiempo_inicial = time() 
				#tiempo_final = time()  
				#tiempo_ejecucion = (tiempo_final - tiempo_inicial)* 1000
				#print(tiempo_ejecucion)
				#if int(tiempo_ejecucion) > 5:
				print(int(b))
				if b - tb > 3:
					print('cada 3 segundos azul')
					print('se acabo el tiempo azul')
					variable = 2
					#variable = 1
					if variable == 0:
						suma = 1
					elif variable == 1:
						suma = suma + numeroRojo
					elif variable == 2:
						suma = suma + numeroAzul
					elif variable == 3:
						suma = suma + numeroAmarrillo
					tiempo_inicial = time() 
					tiempo_final = time()  
					tb = b
				cv2.putText(imagen, "La suma es: "+str(suma), centroPantallaMensaje, cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 4)
	
	#en caso de que sea amarillo
	(_,contours,hierarchy)=cv2.findContours(yellow,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	
	if len(contours)>0:
    	# Busca el contorno mas grande
		c = max(contours, key=cv2.contourArea)
		((x, y), radius) = cv2.minEnclosingCircle(c)
		M = cv2.moments(c)
		center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

		if radius > 10:
            # Dibuja el circulo 
			cv2.circle(imagen, (int(x), int(y)), int(radius), (0,255,0), 2)
			cv2.circle(imagen, center, 5, (0,255,0), -1)
			cv2.putText(imagen, "Amarillo", (int(x - radius), int(y - (radius + 10))), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

            	# Ubica el objeto en el cuadro
			if x < 550 and y < 150:
				#cv2.putText(imagen1, "Amarillo. Tienes 3 puntos.", centroPantallaMensaje, cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 4)
				print('inicia el tiempo')
				#tiempo_inicial = time() 
				#tiempo_final = time()  
				#tiempo_ejecucion = (tiempo_final - tiempo_inicial)* 1000
				#print(tiempo_ejecucion)
				#if int(tiempo_ejecucion) > 5:
				print(int(b))
				if b - tb > 3:
					print('cada 3 segundos amarillo')
					print('se acabo el tiempo amarillo')
					variable = 3
					#variable = 1
					if variable == 0:
						suma = 1
					elif variable == 1:
						suma = suma + numeroRojo
					elif variable == 2:
						suma = suma + numeroAzul
					elif variable == 3:
						suma = suma + numeroAmarrillo
					tiempo_inicial = time() 
					tiempo_final = time()  
					tb = b
				cv2.putText(imagen, "La suma es: "+str(suma), centroPantallaMensaje, cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 4)

    #Prueba de colores.
	cv2.putText(salirmami, "NIVEL 1", (150, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
	cv2.putText(salirmami, "LLega al numero 5", (150, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
	cv2.putText(salirmami, "     La suma es: "+str(suma), (150, 300), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
	#cv2.putText(salirmami, "15", (150, 400), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
	cv2.imshow('Camara', imagen)
	cv2.imshow('Imagen', salirmami)

	if suma==5:
		varfinal=2

		salirmam=cv2.imread("images/resultado2.jpg")
		cv2.putText(salirmam, "Felicidades", (150, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
		cv2.imshow('Imagen', salirmam)
		if b - tb > 3:
			cv2.putText(salirmam, "Preparate segundo nivel!!", (150, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
			cv2.imshow('Imagen', salirmam)
			
	
	#cv2.imshow("Color azul",blue)

	#cv2.imshow("Juego",imagen1)
	#cv2.imshow("red",res)
	if cv2.waitKey(10) & 0xFF == ord('q'):
    		#cap.release()
    		cv2.destroyAllWindows()
    		break

  ##********nivel 1 terminado**********

  ##********nivel 2**********

suma = 0
while varfinal <= 2:
	b = clock()
	#cv2.rectangle(imagen1,(550,150),(280,30),(0,0,0),2)
	
	_, imagen1 = captura.read()
	imagen1 = cv2.flip(imagen1,1)
	imagen = cv2.add(imagen1,dire)    
	salirmami=cv2.imread("images/nivel3.jpg")


	#arriba[y_offset:y_offset+img1.shape[0], x_offset:x_offset+img1.shape[1]] = img1

	
	#cv2.rectangle(imagen, (bdy+100+altura,bdx-150+base), (bdy-50+altura,bdx+base),(255,0,0), 2) #up  150x150 pxls
	#cv2.rectangle(imagen, (bdy+100+altura,bdx+150+base ), (bdy-50+altura,bdx+300+base),(255,0,0), 2) #dowm 150x150 pxls
	#cv2.rectangle(imagen, (bdy-50+altura,bdx+base), (bdy-200+altura,bdx+150+base),(255,0,0), 2) #left 150x150 pxls
	#cv2.rectangle(imagen, (bdy+250+altura,bdx+base), (bdy+100+altura,bdx+150+base),(255,0,0), 2) #rigth 150x150 pxls
	cv2.rectangle(imagen, (bdy+505+altura,bdx+260+base), (bdy+405+altura,bdx+160+base),(0,0,255), 2) #exit 100x100 pxls
	#cv2.rectangle(imagen, (bdy-300+altura,bdx+base+200 ), (bdy-200+altura,bdx+base+300),(255,0,0), 2) #Restar  100x100 pxls
	hsv = cv2.cvtColor(imagen1, cv2.COLOR_BGR2HSV)

    #Show the video
	#cv2.rectangle(imagen,(550,150),(280,30),(0,0,0),2)
	#cv2.imshow('Camara', imagen)

	#convertir a bgr de HSV
	hsv=cv2.cvtColor(imagen1,cv2.COLOR_BGR2HSV)

	#rango de rojo
	red_lower=np.array([136,87,111],np.uint8)
	red_upper=np.array([180,255,255],np.uint8)

	#rango de azul
	blue_lower=np.array([99,115,150],np.uint8)
	blue_upper=np.array([110,255,255],np.uint8)

	#rango de amarillo
	yellow_lower=np.array([22,60,200],np.uint8)
	yellow_upper=np.array([60,255,255],np.uint8)

	#buscando el rango en la imagen
	red=cv2.inRange(hsv, red_lower, red_upper)
	blue=cv2.inRange(hsv,blue_lower,blue_upper)
	yellow=cv2.inRange(hsv,yellow_lower,yellow_upper)


	kernal = np.ones((5 ,5), "uint8")
	red=cv2.dilate(red, kernal)
	res=cv2.bitwise_and(imagen, imagen, mask = red)

	blue=cv2.dilate(blue,kernal)
	res1=cv2.bitwise_and(imagen, imagen, mask = blue)

	yellow=cv2.dilate(yellow,kernal)
	res2=cv2.bitwise_and(imagen, imagen, mask = yellow)


	#en caso de que sea rojo
	(_,contours,hierarchy)=cv2.findContours(red,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

	center = None

	cv2.putText(imagen, "Presiona q para salir", salirPantalla, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
	if len(contours)>0:
    	# Busca el contorno mas grande
		c = max(contours, key=cv2.contourArea)
		((x, y), radius) = cv2.minEnclosingCircle(c)
		M = cv2.moments(c)
		center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

		if radius > 10:
            # Dibuja el circulo 
			cv2.circle(imagen, (int(x), int(y)), int(radius), (0,0,255), 2)
			cv2.circle(imagen, center, 5, (0,0,255), -1)
			cv2.putText(imagen, "Rojo", (int(x - radius), int(y - (radius + 10))), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
			
            	# Ubica el objeto en el cuadro
			if x > 750 and x < 800 and y > 350 and y < 400:
				#print('tuculito')
				exit()



			if x < 550 and y < 150:
				#cv2.putText(img1, "Amarillo. Tienes 3 puntos.", centroPantallaMensaje, cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 4)
				print('inicia el tiempo')
				#tiempo_inicial = time() 
				#tiempo_final = time()  
				#tiempo_ejecucion = (tiempo_final - tiempo_inicial)* 1000
				#print(tiempo_ejecucion)
				#if int(tiempo_ejecucion) > 5:
				print(int(b))
				if b - tb > 3:
					print('cada 3 segundos amarillo')
					print('se acabo el tiempo amarillo')
					variable = 1
					#variable = 1
					if variable == 0:
						suma = 1
					elif variable == 1:
						suma = suma + numeroRojo
					elif variable == 2:
						suma = suma + numeroAzul
					elif variable == 3:
						suma = suma + numeroAmarrillo
					tiempo_inicial = time() 
					tiempo_final = time()  
					tb = b
				cv2.putText(imagen, "La suma es: "+str(suma), centroPantallaMensaje, cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 4)
			
				
	i=0

	#en caso de que sea azul
	(_,contours,hierarchy)=cv2.findContours(blue,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

	if len(contours)>0:
    	# Busca el contorno mas grande
		c = max(contours, key=cv2.contourArea)
		((x, y), radius) = cv2.minEnclosingCircle(c)
		M = cv2.moments(c)
		center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

		if radius > 10:
            # Dibuja el circulo 
			cv2.circle(imagen, (int(x), int(y)), int(radius), (255,0,0), 2)
			cv2.circle(imagen, center, 5, (255,0,0), -1)
			cv2.putText(imagen, "Azul", (int(x - radius), int(y - (radius + 10))), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)

            	# Ubica el objeto en el cuadro
			if x < 550 and y < 150:
				#cv2.putText(imagen1, "Azul. Tienes 3 puntos.", centroPantallaMensaje, cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 4)
				print('inicia el tiempo')
				#tiempo_inicial = time() 
				#tiempo_final = time()  
				#tiempo_ejecucion = (tiempo_final - tiempo_inicial)* 1000
				#print(tiempo_ejecucion)
				#if int(tiempo_ejecucion) > 5:
				print(int(b))
				if b - tb > 3:
					print('cada 3 segundos azul')
					print('se acabo el tiempo azul')
					variable = 2
					#variable = 1
					if variable == 0:
						suma = 1
					elif variable == 1:
						suma = suma + numeroRojo
					elif variable == 2:
						suma = suma + numeroAzul
					elif variable == 3:
						suma = suma + numeroAmarrillo
					tiempo_inicial = time() 
					tiempo_final = time()  
					tb = b
				cv2.putText(imagen, "La suma es: "+str(suma), centroPantallaMensaje, cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 4)
	
	#en caso de que sea amarillo
	(_,contours,hierarchy)=cv2.findContours(yellow,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	
	if len(contours)>0:
    	# Busca el contorno mas grande
		c = max(contours, key=cv2.contourArea)
		((x, y), radius) = cv2.minEnclosingCircle(c)
		M = cv2.moments(c)
		center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

		if radius > 10:
            # Dibuja el circulo 
			cv2.circle(imagen, (int(x), int(y)), int(radius), (0,255,0), 2)
			cv2.circle(imagen, center, 5, (0,255,0), -1)
			cv2.putText(imagen, "Amarillo", (int(x - radius), int(y - (radius + 10))), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

            	# Ubica el objeto en el cuadro
			if x < 550 and y < 150:
				#cv2.putText(imagen1, "Amarillo. Tienes 3 puntos.", centroPantallaMensaje, cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 4)
				print('inicia el tiempo')
				#tiempo_inicial = time() 
				#tiempo_final = time()  
				#tiempo_ejecucion = (tiempo_final - tiempo_inicial)* 1000
				#print(tiempo_ejecucion)
				#if int(tiempo_ejecucion) > 5:
				print(int(b))
				if b - tb > 3:
					print('cada 3 segundos amarillo')
					print('se acabo el tiempo amarillo')
					variable = 3
					#variable = 1
					if variable == 0:
						suma = 1
					elif variable == 1:
						suma = suma + numeroRojo
					elif variable == 2:
						suma = suma + numeroAzul
					elif variable == 3:
						suma = suma + numeroAmarrillo
					tiempo_inicial = time() 
					tiempo_final = time()  
					tb = b
				cv2.putText(imagen, "La suma es: "+str(suma), centroPantallaMensaje, cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 4)

    #Prueba de colores.
	cv2.putText(salirmami, "NIVEL 2", (150, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
	cv2.putText(salirmami, "LLega al numero 9", (150, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
	cv2.putText(salirmami, "     La suma es: "+str(suma), (100, 300), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
	#cv2.putText(salirmami, "15", (150, 400), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
	cv2.imshow('Camara', imagen)
	cv2.imshow('Imagen', salirmami)

	if suma==9:
		varfinal=3
	
	#cv2.imshow("Color azul",blue)

	#cv2.imshow("Juego",imagen1)
	#cv2.imshow("red",res)
	if cv2.waitKey(10) & 0xFF == ord('q'):
    		#cap.release()
    		cv2.destroyAllWindows()
    		break


  ##********nivel 2 terminado**********

  ##********nivel 3**********

suma = 0
while varfinal <= 3:
	b = clock()
	#cv2.rectangle(imagen1,(550,150),(280,30),(0,0,0),2)
	
	_, imagen1 = captura.read()
	imagen1 = cv2.flip(imagen1,1)
	imagen = cv2.add(imagen1,dire)    
	salirmami=cv2.imread("images/nivel2.jpg")
	salirfinal=cv2.imread("images/final.jpg")


	#arriba[y_offset:y_offset+img1.shape[0], x_offset:x_offset+img1.shape[1]] = img1

	
	#cv2.rectangle(imagen, (bdy+100+altura,bdx-150+base), (bdy-50+altura,bdx+base),(255,0,0), 2) #up  150x150 pxls
	#cv2.rectangle(imagen, (bdy+100+altura,bdx+150+base ), (bdy-50+altura,bdx+300+base),(255,0,0), 2) #dowm 150x150 pxls
	#cv2.rectangle(imagen, (bdy-50+altura,bdx+base), (bdy-200+altura,bdx+150+base),(255,0,0), 2) #left 150x150 pxls
	#cv2.rectangle(imagen, (bdy+250+altura,bdx+base), (bdy+100+altura,bdx+150+base),(255,0,0), 2) #rigth 150x150 pxls
	cv2.rectangle(imagen, (bdy+505+altura,bdx+260+base), (bdy+405+altura,bdx+160+base),(0,0,255), 2) #exit 100x100 pxls
	#cv2.rectangle(imagen, (bdy-300+altura,bdx+base+200 ), (bdy-200+altura,bdx+base+300),(255,0,0), 2) #Restar  100x100 pxls
	hsv = cv2.cvtColor(imagen1, cv2.COLOR_BGR2HSV)

    #Show the video
	#cv2.rectangle(imagen,(550,150),(280,30),(0,0,0),2)
	#cv2.imshow('Camara', imagen)

	#convertir a bgr de HSV
	hsv=cv2.cvtColor(imagen1,cv2.COLOR_BGR2HSV)

	#rango de rojo
	red_lower=np.array([136,87,111],np.uint8)
	red_upper=np.array([180,255,255],np.uint8)

	#rango de azul
	blue_lower=np.array([99,115,150],np.uint8)
	blue_upper=np.array([110,255,255],np.uint8)

	#rango de amarillo
	yellow_lower=np.array([22,60,200],np.uint8)
	yellow_upper=np.array([60,255,255],np.uint8)

	#buscando el rango en la imagen
	red=cv2.inRange(hsv, red_lower, red_upper)
	blue=cv2.inRange(hsv,blue_lower,blue_upper)
	yellow=cv2.inRange(hsv,yellow_lower,yellow_upper)


	kernal = np.ones((5 ,5), "uint8")
	red=cv2.dilate(red, kernal)
	res=cv2.bitwise_and(imagen, imagen, mask = red)

	blue=cv2.dilate(blue,kernal)
	res1=cv2.bitwise_and(imagen, imagen, mask = blue)

	yellow=cv2.dilate(yellow,kernal)
	res2=cv2.bitwise_and(imagen, imagen, mask = yellow)


	#en caso de que sea rojo
	(_,contours,hierarchy)=cv2.findContours(red,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

	center = None

	cv2.putText(imagen, "Presiona q para salir", salirPantalla, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
	if len(contours)>0:
    	# Busca el contorno mas grande
		c = max(contours, key=cv2.contourArea)
		((x, y), radius) = cv2.minEnclosingCircle(c)
		M = cv2.moments(c)
		center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

		if radius > 10:
            # Dibuja el circulo 
			cv2.circle(imagen, (int(x), int(y)), int(radius), (0,0,255), 2)
			cv2.circle(imagen, center, 5, (0,0,255), -1)
			cv2.putText(imagen, "Rojo", (int(x - radius), int(y - (radius + 10))), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
			
            	# Ubica el objeto en el cuadro
			if x > 750 and x < 800 and y > 350 and y < 400:
				#print('tuculito')
				exit()



			if x < 550 and y < 150:
				#cv2.putText(img1, "Amarillo. Tienes 3 puntos.", centroPantallaMensaje, cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 4)
				print('inicia el tiempo')
				#tiempo_inicial = time() 
				#tiempo_final = time()  
				#tiempo_ejecucion = (tiempo_final - tiempo_inicial)* 1000
				#print(tiempo_ejecucion)
				#if int(tiempo_ejecucion) > 5:
				print(int(b))
				if b - tb > 3:
					print('cada 3 segundos amarillo')
					print('se acabo el tiempo amarillo')
					variable = 1
					#variable = 1
					if variable == 0:
						suma = 1
					elif variable == 1:
						suma = suma + numeroRojo
					elif variable == 2:
						suma = suma + numeroAzul
					elif variable == 3:
						suma = suma + numeroAmarrillo
					tiempo_inicial = time() 
					tiempo_final = time()  
					tb = b
				cv2.putText(imagen, "La suma es: "+str(suma), centroPantallaMensaje, cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 4)
			
				
	i=0

	#en caso de que sea azul
	(_,contours,hierarchy)=cv2.findContours(blue,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

	if len(contours)>0:
    	# Busca el contorno mas grande
		c = max(contours, key=cv2.contourArea)
		((x, y), radius) = cv2.minEnclosingCircle(c)
		M = cv2.moments(c)
		center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

		if radius > 10:
            # Dibuja el circulo 
			cv2.circle(imagen, (int(x), int(y)), int(radius), (255,0,0), 2)
			cv2.circle(imagen, center, 5, (255,0,0), -1)
			cv2.putText(imagen, "Azul", (int(x - radius), int(y - (radius + 10))), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)

            	# Ubica el objeto en el cuadro
			if x < 550 and y < 150:
				#cv2.putText(imagen1, "Azul. Tienes 3 puntos.", centroPantallaMensaje, cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 4)
				print('inicia el tiempo')
				#tiempo_inicial = time() 
				#tiempo_final = time()  
				#tiempo_ejecucion = (tiempo_final - tiempo_inicial)* 1000
				#print(tiempo_ejecucion)
				#if int(tiempo_ejecucion) > 5:
				print(int(b))
				if b - tb > 3:
					print('cada 3 segundos azul')
					print('se acabo el tiempo azul')
					variable = 2
					#variable = 1
					if variable == 0:
						suma = 1
					elif variable == 1:
						suma = suma + numeroRojo
					elif variable == 2:
						suma = suma + numeroAzul
					elif variable == 3:
						suma = suma + numeroAmarrillo
					tiempo_inicial = time() 
					tiempo_final = time()  
					tb = b
				cv2.putText(imagen, "La suma es: "+str(suma), centroPantallaMensaje, cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 4)
	
	#en caso de que sea amarillo
	(_,contours,hierarchy)=cv2.findContours(yellow,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	
	if len(contours)>0:
    	# Busca el contorno mas grande
		c = max(contours, key=cv2.contourArea)
		((x, y), radius) = cv2.minEnclosingCircle(c)
		M = cv2.moments(c)
		center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

		if radius > 10:
            # Dibuja el circulo 
			cv2.circle(imagen, (int(x), int(y)), int(radius), (0,255,0), 2)
			cv2.circle(imagen, center, 5, (0,255,0), -1)
			cv2.putText(imagen, "Amarillo", (int(x - radius), int(y - (radius + 10))), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

            	# Ubica el objeto en el cuadro
			if x < 550 and y < 150:
				#cv2.putText(imagen1, "Amarillo. Tienes 3 puntos.", centroPantallaMensaje, cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 4)
				print('inicia el tiempo')
				#tiempo_inicial = time() 
				#tiempo_final = time()  
				#tiempo_ejecucion = (tiempo_final - tiempo_inicial)* 1000
				#print(tiempo_ejecucion)
				#if int(tiempo_ejecucion) > 5:
				print(int(b))
				if b - tb > 3:
					print('cada 3 segundos amarillo')
					print('se acabo el tiempo amarillo')
					variable = 3
					#variable = 1
					if variable == 0:
						suma = 1
					elif variable == 1:
						suma = suma + numeroRojo
					elif variable == 2:
						suma = suma + numeroAzul
					elif variable == 3:
						suma = suma + numeroAmarrillo
					tiempo_inicial = time() 
					tiempo_final = time()  
					tb = b
				cv2.putText(imagen, "La suma es: "+str(suma), centroPantallaMensaje, cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 4)

    #Prueba de colores.
	cv2.putText(salirmami, "NIVEL 3", (150, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
	cv2.putText(salirmami, "LLega al numero 15", (150, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
	cv2.putText(salirmami, "     La suma es: "+str(suma), (100, 300), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
	#cv2.putText(salirmami, "15", (150, 400), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
	cv2.imshow('Camara', imagen)
	cv2.imshow('Imagen', salirmami)

	if suma==15:
		varfinal=3
		if b - tb > 3:
			print('cada 3 segundos final')
			cv2.imshow('Imagen', salirfinal)
	#cv2.imshow("Color azul",blue)

	#cv2.imshow("Juego",imagen1)
	#cv2.imshow("red",res)
	if cv2.waitKey(10) & 0xFF == ord('q'):
    		#cap.release()
    		cv2.destroyAllWindows()
    		break