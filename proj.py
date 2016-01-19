import numpy as np
import cv2

## Definiujemy obiekt z indeksem urzadzeienia - w moim przypadku domyslne urzadzenie
cap = cv2.VideoCapture(0)

while(True):
    # Przechwytywanie klatek
	ret, frame = cap.read()

# Konwertujemy RGB TO HSV

	new = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

## Definiujemy zakres koloru w HSV

	min = np.array([40, 100, 50], dtype=np.uint8)
	max = np.array([80, 255, 255], dtype=np.uint8)

## Ograniczenie do pokazania tylko zielonego koloru

	mask = cv2.inRange(new, min, max)

## Obiekt - iloczyn maski i oryginalnego brazu

	res = cv2.bitwise_and(frame,frame, mask= mask)


	cv2.imshow('frame',frame)
   	cv2.imshow('mask',mask)
    	cv2.imshow('res',res)
    	exit = cv2.waitKey(5) & 0xFF
    	if exit == 27:    ## kod przycisku wyjscia
        	break

cv2.destroyAllWindows()
