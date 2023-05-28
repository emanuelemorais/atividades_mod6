from ultralytics import YOLO
import cv2 as cv

#Abre a câmera do computador
video_capture = cv.VideoCapture(0)

#Importa modelo treinado
model = YOLO("ponderada3/best.pt")

while True:
    #Passa video frame por frame
    _, frame = video_capture.read()
    #Passa frames pelo modelo
    result = model.predict(frame, conf=0.5)
    annotated_frame = result[0].plot()
    #Resultador são exibidos 
    cv.imshow("results", annotated_frame)
    
    #Pressione 'q' para sair
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv.destroyAllWindows()