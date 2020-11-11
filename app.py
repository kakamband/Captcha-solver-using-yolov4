from flask import Flask, request
import os
from yolov4_detection import detect
import numpy as np
import cv2
from img_treatments import treatment1, treatment4

UPLOADED_IMGS_DIR = 'uploaded images/'
UPLOADED_TREATED_DIR = 'uploaded treated/'
YOLO_DATA_DIR = 'yolo-data'
MIN_CONFIDENCE  = 0.5
NON_MAXIMA_THRESHOLD = 0.3


app = Flask(__name__)


@app.route("/CAPTCHA/yolo_detection", methods=["POST"])
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
    for name in img_names:
        treated_img_path = os.path.join(UPLOADED_TREATED_DIR, name)
        result, _ = detect(treated_img_path, YOLO_DATA_DIR, MIN_CONFIDENCE, NON_MAXIMA_THRESHOLD)
        result = [value[0] for value in result]
        result = "".join(result)
        detections[name] = result

    return detections


if __name__ == "__main__":
    app.run(debug=True)
