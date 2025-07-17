from flask import Flask, render_template, request, send_file, redirect
import qrcode
from PIL import Image
from pyzbar.pyzbar import decode
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html', result=None)

@app.route('/generate', methods=['POST'])
def generate_qr():
    data = request.form.get('qr-data')
    img = qrcode.make(data)
    file_path = os.path.join(UPLOAD_FOLDER, 'qr.png')
    img.save(file_path)
    return render_template('index.html', result='generated', qr_image=file_path)

@app.route('/scan', methods=['POST'])
def scan_qr():
    file = request.files['qr-image']
    path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(path)

    img = Image.open(path)
    decoded_objects = decode(img)
    text = decoded_objects[0].data.decode('utf-8') if decoded_objects else "No QR code detected."

    return render_template('index.html', result='scanned', qr_text=text)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

