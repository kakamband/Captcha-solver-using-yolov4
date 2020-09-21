import os

YOLO_DATA_DIR = 'yolo-data'
TEST_DATA_DIR = 'test-treated-4'
filenames = os.listdir(TEST_DATA_DIR)
CONFIDENCE  = 0.5
NON_MAXIMA_THRESHOLD = 0.3 

for name in filenames:
	command = 'python3 yolov4_detection.py -i ' + os.path.join(TEST_DATA_DIR, name) + ' -y ' + YOLO_DATA_DIR + ' -c ' + str(CONFIDENCE) + ' -t ' + str(NON_MAXIMA_THRESHOLD)
	os.system(command)
