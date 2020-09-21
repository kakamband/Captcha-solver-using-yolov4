# Steps for the captcha solver

1. Download whole dataset from https://www.kaggle.com/famadio/captcha-2-text
2. Do perform data preprcessing of images using image-preprocess.ipynb notebook
3. Label treated-4 images using labelImg annotation tool and labelImg can be obtained from https://github.com/tzutalin/labelImg
4. Train yolov4 model on our custom dataset using YOLOv4_Training.ipynb in google colab or gpu-enabled system linux system 
5. Download trained model to local system (can run on CPU)
6. Do predictions on test-treated-4 images using detect_all.py

