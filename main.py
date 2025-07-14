import cv2
import mediapipe as mp
from scipy.spatial import distance

# EAR: Eye Aspect Ratio
def eye_aspect_ratio(eye_points):
    A = distance.euclidean(eye_points[1], eye_points[5])
    B = distance.euclidean(eye_points[2], eye_points[4])
    C = distance.euclidean(eye_points[0], eye_points[3])
    return (A + B) / (2.0 * C)

# Pontos dos olhos no FaceMesh
LEFT_EYE = [33, 160, 158, 133, 153, 144]
RIGHT_EYE = [362, 385, 387, 263, 373, 380]

# Inicialização
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True)
cap = cv2.VideoCapture(0)  # 0 é a webcam padrão

while True:
    ret, frame = cap.read()
    if not ret:
        break

    h, w, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb_frame)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            left_eye = [(int(face_landmarks.landmark[i].x * w),
                         int(face_landmarks.landmark[i].y * h)) for i in LEFT_EYE]
            right_eye = [(int(face_landmarks.landmark[i].x * w),
                          int(face_landmarks.landmark[i].y * h)) for i in RIGHT_EYE]

            # Desenha pontos nos olhos
            for x, y in left_eye + right_eye:
                cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)

            # Calcula EAR
            left_ear = eye_aspect_ratio(left_eye)
            right_ear = eye_aspect_ratio(right_eye)
            ear_avg = (left_ear + right_ear) / 2.0

            status = "OLHOS ABERTOS" if ear_avg >= 0.2 else "OLHOS FECHADOS"
            cor = (0, 255, 0) if status == "OLHOS ABERTOS" else (0, 0, 255)

            cv2.putText(frame, f"{status} (EAR: {ear_avg:.2f})",
                        (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, cor, 2)

    cv2.imshow("Detecção de Olhos com MediaPipe", frame)
    if cv2.waitKey(1) & 0xFF == 27:  # Tecla ESC para sair
        break

cap.release()
cv2.destroyAllWindows()
