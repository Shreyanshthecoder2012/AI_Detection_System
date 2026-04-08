# 🚀 AI Detection App

A simple yet powerful AI-based desktop application that performs **real-time object detection** and **smart CCTV monitoring** using OpenCV.

---

## ✨ Features

* 🖼️ Image Object Detection
* 📹 Real-time CCTV Monitoring
* 🚨 Auto-detects **person** and saves image
* ⏱️ Timestamp-based image saving
* 📁 User-selected save folder
* 🧠 Lightweight MobileNet SSD model
* 🎨 Simple & user-friendly GUI (Tkinter)
* ⚡ Automatic model download (no manual setup)

---

## 🛠️ Tech Stack

* Python 🐍
* OpenCV
* NumPy
* Tkinter (GUI)

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/AI-Detection-App.git
cd AI-Detection-App
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the App

```bash
python3 full_app.py
```

---

## 🤖 Model Setup (Automatic)

No manual download required.

* The app will automatically download required model files on first run
* Internet connection required only once

---

## 📸 How It Works

### Image Detection

* Select an image
* AI detects objects and shows results

### CCTV Mode

* Select a folder
* Start CCTV
* When a **person is detected**:

  * Image is captured 📸
  * Saved with timestamp ⏱️

---

## 📁 Project Structure

```
AI-Detection-App/
│
├── full_app.py
├── cctv.py
├── image_detect.py
├── download_model.py
├── requirements.txt
└── MobileNetSSD files
```

---

## ⚠️ Notes

* Works best with good lighting conditions
* Detection accuracy depends on model limitations
* Designed for learning and experimentation

---

## 👨‍💻 Author

**Shreyansh** 🚀
Passionate about AI, coding, and building cool stuff

---

## ⭐ Support

If you like this project:

* Star ⭐ the repo
* Share with friends
* Build something even cooler 😏

---
