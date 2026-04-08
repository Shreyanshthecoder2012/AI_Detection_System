import cv2
import numpy as np
import os
from datetime import datetime

# 🔥 USER SE FOLDER INPUT
save_folder = input("Enter folder path to save images: ")

if not os.path.exists(save_folder):
    os.makedirs(save_folder)

# Load model
net = cv2.dnn.readNetFromCaffe(
    "MobileNetSSD_deploy.prototxt",
    "MobileNetSSD_deploy.caffemodel"
)

classes = ["background","aeroplane","bicycle","bird","boat","bottle","bus",
           "car","cat","chair","cow","diningtable","dog","horse","motorbike",
           "person","pottedplant","sheep","sofa","train","tvmonitor"]

# Webcam start
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    h, w = frame.shape[:2]

    blob = cv2.dnn.blobFromImage(frame, 0.007843, (300, 300), 127.5)
    net.setInput(blob)
    detections = net.forward()

    person_detected = False

    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]

        if confidence > 0.5:
            idx = int(detections[0, 0, i, 1])
            label = classes[idx]

            if label == "person":
                person_detected = True

                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (x1, y1, x2, y2) = box.astype("int")

                cv2.rectangle(frame, (x1, y1), (x2, y2), (0,0,255), 2)
                cv2.putText(frame, "PERSON DETECTED",
                            (x1, y1-10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6,
                            (0,0,255), 2)

    # 🔥 SAVE IMAGE + TIME
    if person_detected and datetime.now().second % 5 == 0 :
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"{save_folder}/person_{timestamp}.jpg"
        cv2.imwrite(filename, frame)
        print(f"Saved: {filename}")

    cv2.imshow("CCTV AI", frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
