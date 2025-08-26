import cv2
from cvzone.HandTrackingModule import HandDetector

# Inicia câmera
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

detector = HandDetector(detectionCon=0.8, maxHands=1)

# Constante aproximada para cálculo de distância (ajuste conforme sua câmera)
KNOWN_WIDTH = 8.0  # largura média da mão em cm (aprox.)
FOCAL_LENGTH = 650  # focal da câmera (aprox., teste e ajuste)

while True:
    success, img = cap.read()
    if not success:
        print("❌ Não foi possível capturar a câmera")
        break

    hands, img = detector.findHands(img)  # detecta mão

    if hands:
        hand = hands[0]
        bbox = hand['bbox']  # retorna [x, y, w, h]
        x, y, w, h = bbox

        # Desenha bounding box
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Estima distância aproximada usando a largura da mão
        distance = (KNOWN_WIDTH * FOCAL_LENGTH) / w

        # Mostra distância
        cv2.putText(img, f'Distancia: {int(distance)} cm', (x, y - 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

    cv2.imshow("Mão e Distancia da Camera", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()