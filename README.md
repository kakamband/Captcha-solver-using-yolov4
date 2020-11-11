# Steps for the captcha solver

1. Download whole dataset from https://www.kaggle.com/famadio/captcha-2-text
2. Do perform data preprcessing of images using image-preprocess.ipynb notebook
3. Label treated-4 images using labelImg annotation tool and labelImg can be obtained from https://github.com/tzutalin/labelImg
4. Train yolov4 model on our custom dataset using YOLOv4_Training.ipynb in google colab or gpu-enabled system linux system and for more help refer https://www.youtube.com/watch?v=mmj3nxGT2YQ&t=1956s
5. Download trained model from google drive to local system & store in yolo-data folder 
6. Do predictions on test-treated-4 images using test.ipynb & for predictions we don't need GPU it can be done simply using dnn module in opencv
7. Deploying model "app.py" for real-time predictions using simple API created using flask 

