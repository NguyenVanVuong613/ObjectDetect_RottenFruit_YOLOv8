from flask import Flask, render_template, request
import numpy as np
import base64
import cv2
import os

from ultralytics import YOLO

model = YOLO('YOLO_pretrained_model.pt')

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def predict_on_image(image_stream):
    try:
        image = cv2.imdecode(np.asarray(bytearray(image_stream.read()), dtype=np.uint8), cv2.IMREAD_COLOR)
        if image is None:
            print("Failed to decode image")
            return None

        results = model.predict(image, conf=0.5)
        im_bgr = None

        if results:
            for i, r in enumerate(results):
                im_bgr = r.plot(conf=False)

        if im_bgr is None:
            print("Failed to plot detection results or no detections found")
            return None

        return im_bgr

    except Exception as e:
        print(f"Error during image processing: {e}")
        return None


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('index.html', error='No file part')

        file = request.files['file']

        if file.filename == '':
            return render_template('index.html', error='No selected file')

        if file and allowed_file(file.filename):
            predicted_image = predict_on_image(file.stream)

            if predicted_image is None:
                return render_template('index.html', error='Failed to process image')

            retval, buffer = cv2.imencode('.png', predicted_image)
            if not retval:
                return render_template('index.html', error='Failed to encode image')

            detection_img_base64 = base64.b64encode(buffer).decode('utf-8')

            file.stream.seek(0)
            original_img_base64 = base64.b64encode(file.stream.read()).decode('utf-8')

            return render_template('result.html', original_img_data=original_img_base64,
                                   detection_img_data=detection_img_base64)

    return render_template('index.html')


if __name__ == '__main__':
    os.environ.setdefault('FLASK_ENV', 'development')
    app.run(debug=False, port=5000, host='0.0.0.0')
