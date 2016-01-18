import numpy as np
import cv2

## Definiujemy obiekt z indeksem urządzenia - w moim przypadku domyslne urzadzenie
cap = cv2.VideoCapture(0)

while(True):
    # Przechwytywanie klatek
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

## Wyswietlamy wynik

    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):   ## ustawienie uczekiwania i przerwania na klawisz "q"
        break

# Zwalniamy przechwytywanie i zabijamy okno
cap.release()
cv2.destroyAllWindows()