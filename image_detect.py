import cv2
import numpy as np

# Load model
net = cv2.dnn.readNetFromCaffe(
    "MobileNetSSD_deploy.prototxt",
    "MobileNetSSD_deploy.caffemodel"
)

# Class labels
classes = ["background","aeroplane","bicycle","bird","boat","bottle","bus",
           "car","cat","chair","cow","diningtable","dog","horse","motorbike",
           "person","pottedplant","sheep","sofa","train","tvmonitor","ball"]

# Load image
image = cv2.imread("test.png")

# Check image
if image is None:
    print("Image not found bro 💀")
    exit()

orig = image.copy()
h, w = image.shape[:2]

# Create blob
blob = cv2.dnn.blobFromImage(image, 0.007843, (300, 300), 127.5)
net.setInput(blob)
detections = net.forward()

# Detection loop
for i in range(detections.shape[2]):
    confidence = detections[0, 0, i, 2]

    if confidence > 0.2:
        idx = int(detections[0, 0, i, 1])
        label = classes[idx]

        box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
        (x1, y1, x2, y2) = box.astype("int")

        cv2.rectangle(orig, (x1, y1), (x2, y2), (0,255,0), 2)
        cv2.putText(orig, f"{label} {confidence:.2f}",
                    (x1, y1-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                    (0,255,0), 2)

# 🔥 AUTO RESIZE (fit to screen)
max_width = 800
h, w = orig.shape[:2]

if w > max_width:
    ratio = max_width / w
    orig = cv2.resize(orig, (int(w * ratio), int(h * ratio)))

# 🔥 RESIZABLE WINDOW
cv2.namedWindow("Result", cv2.WINDOW_NORMAL)
cv2.imshow("Result", orig)

cv2.waitKey(0)
cv2.destroyAllWindows()
