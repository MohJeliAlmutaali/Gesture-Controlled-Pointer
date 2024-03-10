import cv2
import mediapipe as mp
import pyautogui

# Inisialisasi MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Inisialisasi OpenCV
cap = cv2.VideoCapture(0)

# Inisialisasi status klik (klik pertama adalah False)
click = False

# Inisialisasi posisi kursor sebelumnya
prevX, prevY = 0, 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Balikkan gambar secara horizontal
    frame = cv2.flip(frame, 1)

    # Ubah warna dari BGR ke RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Deteksi tangan
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            for id, lm in enumerate(hand_landmarks.landmark):
                h, w, c = frame.shape
                cx, cy = int(lm.x * w), int(lm.y * h)

                # Tampilkan lingkaran di ujung jari telunjuk
                if id == 8:  # ID 8 adalah ujung jari telunjuk
                    cv2.circle(frame, (cx, cy), 10, (255, 0, 255), cv2.FILLED)

                # Ubah posisi kursor sesuai dengan posisi ujung jari telunjuk
                if id == 8:  # ID 8 adalah ujung jari telunjuk
                    screenWidth, screenHeight = pyautogui.size()
                    newX = cx * screenWidth / w
                    newY = cy * screenHeight / h

                    # Memfilter gerakan yang terlalu kecil
                    if abs(newX - prevX) > 15 or abs(newY - prevY) > 15:
                        pyautogui.moveTo(newX, newY)
                        prevX, prevY = newX, newY

                # Deteksi gerakan klik (angkat jari tengah)
                if id == 12:  # ID 12 adalah jari tengah
                    if lm.y * h < hand_landmarks.landmark[8].y * h:
                        if not click:
                            pyautogui.click()
                            click = True
                    else:
                        click = False

                    # Tampilkan lingkaran di jari tengah jika klik terjadi
                    if click:
                        cv2.circle(frame, (cx, cy), 10, (0, 255, 0), cv2.FILLED)

    cv2.imshow('Hand Tracking', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
