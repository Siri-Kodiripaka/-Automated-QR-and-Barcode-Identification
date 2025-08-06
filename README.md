# -Automated-QR-and-Barcode-Identification

---

```markdown
# 📷 QR and Barcode Detection

## 📌 Project Overview
This project is a **QR and Barcode Detection Web Application** built using **Python (Flask)**.  
It allows users to upload or scan QR codes and barcodes, detect them, and retrieve the embedded information.  
The app includes a simple **HTML frontend** and a **Flask backend** for processing.

---

## 🛠 Tech Stack
- **Python** (Flask, OpenCV, pyzbar)
- **HTML / CSS** (Frontend templates)
- **Bootstrap** (for UI styling)
- **Pillow (PIL)** for image handling

---

## 📂 Project Structure
```

project/
│── app.py                 # Main Flask application
│── MyDataFile.text        # Data storage file
│── tempCodeRunnerFile.py  # Temporary test file
│── QRCODES/               # Sample QR/Barcode images
│   ├── Accenture.png
│   ├── Amazon.png
│   ├── Apple.png
│   ├── CapeGemini.png
│   ├── Cognizent.png
│   ├── Google.png
│   ├── IBM.png
│   ├── Microsoft.png
│   └── Tech Mahindra.png
│── templates/
│   ├── index.html         # Home page
│   ├── model.html         # Detection results page
│   └── team.html          # Team info page

````

---

## ⚡ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Siri-Kodiripaka/-Automated-QR-and-Barcode-Identification
cd qr-bar-detection/project
````

### 2️⃣ Install Dependencies

Make sure you have **Python 3.x** installed.
Install required libraries:

```bash
pip install flask opencv-python pyzbar pillow
```

### 3️⃣ Run the Application

```bash
python app.py
```

The app will start locally at:

```
http://127.0.0.1:5000/
```

---

## 🎯 Features

* Detect **QR codes** and **barcodes** from uploaded images.
* Extract and display the embedded text or link.
* Preloaded sample QR codes in `QRCODES/` folder.
* Web-based interface for ease of use.

---

## 📸 Sample QR Codes

The `QRCODES/` folder contains sample QR codes for companies like:

* Amazon
* Google
* IBM
* Microsoft
* Apple
* Tech Mahindra

---

## 👨‍💻 Authors

* **Siri Kodiripaka** – Developer

---

## 📜 License

This project is licensed under the MIT License.

```


