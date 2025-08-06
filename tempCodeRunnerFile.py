from flask import Flask, render_template, Response
import cv2
import numpy as np
from pyzbar.pyzbar import decode

app = Flask(__name__)


camera = cv2.VideoCapture(0)
camera.set(3, 640)  
camera.set(4, 480)  

AUTHORIZED_COMPANIES = {
    'https://www.hcltech.com/': 'HCL Technologies',
    'https://www.infosys.com/': 'Infosys',
    'https://www.tcs.com/': 'Tata Consultancy Services',
    'https://www.microsoft.com': 'Microsoft',
    'https://www.google.com': 'Google',
    'https://www.apple.com': 'Apple',
    'https://www.amazon.com': 'Amazon',
    'https://www.ibm.com': 'IBM',
    'https://www.accenture.com': 'Accenture',
    'https://www.wipro.com': 'Wipro'
}

def generate_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            for barcode in decode(frame):
                url = barcode.data.decode('utf-8')
                company_name = AUTHORIZED_COMPANIES.get(url, 'Unknown Company')
                
                if url in AUTHORIZED_COMPANIES:
                    status = "Authorized"
                    color = (0, 255, 0) 
                else:
                    status = "Unauthorized"
                    color = (0, 0, 255)  
                
                
                pts = np.array([barcode.polygon], np.int32)
                pts = pts.reshape((-1, 1, 2))
                cv2.polylines(frame, [pts], True, color, 5)
                
               
                rect = barcode.rect
                cv2.putText(frame, f"{company_name}: {status}", 
                           (rect[0], rect[1] - 10), cv2.FONT_HERSHEY_SIMPLEX,
                           0.7, color, 2)

            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/model')
def model():
    return render_template('model.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(),
                   mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)