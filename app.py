from flask import Flask, request, Response
import os
from yolov4_detection import detect
import numpy as np
import cv2
from img_treatments import treatment1, treatment4

UPLOADED_IMGS_DIR = 'uploaded images/'
UPLOADED_TREATED_DIR = 'uploaded treated/'
YOLO_DATA_DIR = 'yolo-data'
MIN_CONFIDENCE = 0.5
NON_MAXIMA_THRESHOLD = 0.3


app = Flask(__name__)


def predict():
    images = request.files.getlist("images")

    img_names = []
    for img in images:
        img_names.append(img.filename)
        img.save(UPLOADED_IMGS_DIR + img.filename)

    # img = img_preprocessing()
    for name in img_names:
        img_path = os.path.join(UPLOADED_IMGS_DIR, name)
        treated1_img = treatment1(img_path)
        treated4 = treatment4(treated1_img)
        cv2.imwrite(os.path.join(UPLOADED_TREATED_DIR, name), treated4)

    detections = {}
    detected_imgs = []
    for name in img_names:
        treated_img_path = os.path.join(UPLOADED_TREATED_DIR, name)
        result, detected_img = detect(treated_img_path, YOLO_DATA_DIR, MIN_CONFIDENCE, NON_MAXIMA_THRESHOLD)
        result = [value[0] for value in result]
        result = "".join(result)
        detections[name] = result

        _, encoded_img = cv2.imencode('.png', detected_img)
        detected_img = encoded_img.tostring()
        detected_imgs.append(detected_img)

    return detections, detected_imgs


@app.route("/CAPTCHA/text", methods=["POST"])
def captcha_to_text():
    detections, _ = predict()
    return detections


@app.route("/CAPTCHA/image", methods=["POST"])
def captcha_img_detection():
    _, detected_img = predict()
    return Response(response=detected_img, mimetype='image/png')


if __name__ == "__main__":
    app.run(debug=True)
