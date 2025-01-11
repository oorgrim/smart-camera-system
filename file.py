import cv2
import time
import datetime

cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
body_cascade = cv2.CascadeClassifier("haarcascade_fullbody.xml")

detection = True
detection_stopped_time = None
timer_started = False
SECONDS_TO_RECORD_AFTER_DETECTION = 5

frame_size = (int(cap.get(3)), int(cap.get(4)))
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out =  cv2.VideoWriter("video.mp4", fourcc, 20, frame_size)

if face_cascade.empty():
    print("не удалось загрузить 'haarcascade_frontalface_default.xml'")
    exit()

if body_cascade.empty():
    print("не удалось загрузить 'haarcascade_fullbody.xml'")
    exit()

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Не удалось открыть камеру!")
    exit()

while True:
    _, frame = cap.read()
    if not _:
        print("Не удалось получить кадр!")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    bodies = face_cascade.detectMultiScale(gray, 1.3, 5)

    if len(faces) + len(bodies) > 0:
        detection = True
    out.write(frame)

    

    # for (x, y, width, height) in faces:
    #     cv2.rectangle(frame, (x, y), (x + width, y + height), (255, 0, 0), 3)
    
    cv2.imshow("Camera", frame)

    if cv2.waitKey(1) == ord('q'):
        break

out.release()
cap.release()
cv2.destroyAllWindows()
