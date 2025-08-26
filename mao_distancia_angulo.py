import cv2
from cvzone.HandTrackingModule import HandDetector
import math

# Inicia câmera
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

detector = HandDetector(detectionCon=0.8, maxHands=1)

# Constantes para cálculo de distância real
KNOWN_WIDTH = 8.0    # largura média da mão em cm
FOCAL_LENGTH = 650    # focal da câmera (ajuste conforme teste)

# Variável para armazenar posição inicial
initial_point = None

while True:
    success, img = cap.read()
    if not success or img is None:
        print("❌ Não foi possível capturar a câmera")
        break

    hands, img = detector.findHands(img, draw=True)

    if hands:
        hand = hands[0]
        x, y, w, h = hand['bbox']

        # Centro da mão
        cx = x + w // 2
        cy = y + h // 2

        # Desenha centro da mão
        cv2.circle(img, (cx, cy), 10, (255, 0, 0), cv2.FILLED)

        # Converte largura da mão em pixels para distância aproximada em cm
        distance_cm = (KNOWN_WIDTH * FOCAL_LENGTH) / w

        if initial_point is not None:
            ix, iy = initial_point

            # Distância em pixels
            dx = cx - ix
            dy = cy - iy

            # Distância em cm aproximada da posição inicial
            distance_to_initial_cm = distance_cm  # já aproximada pela largura

            # Calcula ângulo em graus (0° horizontal, positivo sentido anti-horário)
            angle = math.degrees(math.atan2(dy, dx))

            # Desenha linha do ponto inicial à mão
            cv2.line(img, (cx, cy), (ix, iy), (0, 255, 0), 3)
            cv2.circle(img, (ix, iy), 8, (0, 0, 255), cv2.FILLED)  # ponto inicial

            # Mostra distância e ângulo
            cv2.putText(img, f'Distancia: {int(distance_to_initial_cm)} cm', (50, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            cv2.putText(img, f'Angulo: {int(angle)} deg', (50, 90),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Instrução para definir ponto inicial
    cv2.putText(img, "Pressione 's' para definir ponto inicial", (10, 450),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)

    cv2.imshow("Mao - Distancia e Angulo", img)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('s') and hands:
        # Define ponto inicial no centro da mão
        hand = hands[0]
        x, y, w, h = hand['bbox']
        initial_point = (x + w // 2, y + h // 2)
        print(f"Ponto inicial definido: {initial_point}")

cap.release()
cv2.destroyAllWindows()
