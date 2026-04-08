import urllib.request
import os

def download(url, filename):
    try:
        print(f"Downloading {filename}...")
        urllib.request.urlretrieve(url, filename)
        print(f"{filename} downloaded successfully ✅")
    except Exception as e:
        print(f"Error downloading {filename}: {e}")

# Model files
files = {
    "MobileNetSSD_deploy.caffemodel":
    "https://github.com/chuanqi305/MobileNet-SSD/raw/master/mobilenet_iter_73000.caffemodel",

    "MobileNetSSD_deploy.prototxt":
    "https://raw.githubusercontent.com/chuanqi305/MobileNet-SSD/master/deploy.prototxt"
}

for file, url in files.items():
    if not os.path.exists(file):
        download(url, file)
    else:
        print(f"{file} already exists 👍")
