import tkinter as tk
from tkinter import filedialog, messagebox
import cv2
import numpy as np
from datetime import datetime

# Load model once
net = cv2.dnn.readNetFromCaffe(
    "MobileNetSSD_deploy.prototxt",
    "MobileNetSSD_deploy.caffemodel"
)

classes = ["background","aeroplane","bicycle","bird","boat","bottle","bus",
           "car","cat","chair","cow","diningtable","dog","horse","motorbike",
           "person","pottedplant","sheep","sofa","train","tvmonitor"]

save_folder = ""

# 📁 Folder select
def choose_folder():
    global save_folder
    folder = filedialog.askdirectory()
    if folder:
        save_folder = folder
        messagebox.showinfo("Selected", f"Folder: {folder}")

# 🖼️ Image Detection
def image_detection():
    file_path = filedialog.askopenfilename()
    if not file_path:
        return

    image = cv2.imread(file_path)
    h, w = image.shape[:2]

    blob = cv2.dnn.blobFromImage(image, 0.007843, (300, 300), 127.5)
    net.setInput(blob)
    detections = net.forward()

    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]

        if confidence > 0.5:
            idx = int(detections[0, 0, i, 1])
            label = classes[idx]

            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (x1, y1, x2, y2) = box.astype("int")

            cv2.rectangle(image, (x1, y1), (x2, y2), (0,255,0), 2)
            cv2.putText(image, label, (x1, y1-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)

    # 🔥 Resize properly
    max_width = 800
    if w > max_width:
        ratio = max_width / w
        image = cv2.resize(image, (int(w * ratio), int(h * ratio)))

    cv2.namedWindow("Image Detection", cv2.WINDOW_NORMAL)
    cv2.imshow("Image Detection", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 📹 CCTV Mode
def cctv_mode():
    global save_folder

    if not save_folder:
        messagebox.showerror("Error", "Select folder first!")
        return

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

        if person_detected and datetime.now().second % 5 == 0:
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filename = f"{save_folder}/person_{timestamp}.jpg"
            cv2.imwrite(filename, frame)

        cv2.imshow("CCTV", frame)

        if cv2.waitKey(1) == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

# 🎨 GUI
root = tk.Tk()
root.title("AI Detection App")
root.geometry("400x350")
root.resizable(True, True)
root.minsize(400, 300)

title = tk.Label(root, text="AI Detection System", font=("Arial", 16))
title.pack(pady=20)

btn_folder = tk.Button(root, text="Select Save Folder", command=choose_folder, width=25, height=2)
btn_folder.pack(pady=10)

btn_img = tk.Button(root, text="Image Detection", command=image_detection, width=25, height=2)
btn_img.pack(pady=10)

btn_cctv = tk.Button(root, text="Start CCTV", command=cctv_mode, width=25, height=2)
btn_cctv.pack(pady=10)

root.mainloop()
