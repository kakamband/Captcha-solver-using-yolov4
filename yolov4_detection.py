# import the necessary packages
import numpy as np
import argparse
import time
import cv2
import os

# construct the argument parse and parse the arguments
#ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", required=True,
#               help="path to input image")
#ap.add_argument("-y", "--yolo", required=True,
#                help="base path to YOLO directory")
#ap.add_argument("-c", "--confidence", type=float, default=0.5,
#                help="minimum probability to filter weak detections")
#ap.add_argument("-t", "--threshold", type=float, default=0.3,
#                help="threshold when applying non-maxima suppression")
#args = vars(ap.parse_args())


def detect(img_path, yolo_data_path, min_confidence, threshold):
	# load the obj class labels our YOLO model was trained on
	labelsPath = os.path.sep.join([yolo_data_path, "obj.names"])
	LABELS = open(labelsPath).read().strip().split("\n")
	# initialize a list of colors to represent each possible class label
	np.random.seed(42)
	COLORS = np.random.randint(0, 255, size=(len(LABELS), 3), dtype="uint8")

	# derive the paths to the YOLO weights and model configuration
	weightsPath = os.path.sep.join([yolo_data_path, "yolov4-obj_last.weights"])
	configPath = os.path.sep.join([yolo_data_path, "yolov4-obj.cfg"])
	# load our YOLO object detector trained on our custom dataset (36 classes)
	#print("[INFO] loading YOLO from disk...")
	net = cv2.dnn.readNetFromDarknet(configPath, weightsPath)

	# load our input image and grab its spatial dimensions
	image = cv2.imread(img_path)
	(H, W) = image.shape[:2]

	#white = np.full((H//2, W, 3), 255)
	#image = np.append(white, image, axis=0)
	#image = cv2.resize(image.astype('float32'), (W, H))

	# determine only the *output* layer names that we need from YOLO
	ln = net.getLayerNames()
	ln = [ln[i[0] - 1] for i in net.getUnconnectedOutLayers()]
	# construct a blob from the input image and then perform a forward
	# pass of the YOLO object detector, giving us our bounding boxes and
	# associated probabilities
	blob = cv2.dnn.blobFromImage(image, 1 / 255.0, (256, 64),
		                     swapRB=True, crop=False)
	net.setInput(blob)
	start = time.time()
	layerOutputs = net.forward(ln)
	end = time.time()
	# show timing information on YOLO
	print("[INFO] YOLO took {:.6f} seconds".format(end - start))

	# initialize our lists of detected bounding boxes, confidences, and
	# class IDs, respectively
	boxes = []
	confidences = []
	classIDs = []

	# loop over each of the layer outputs
	for output in layerOutputs:
		# loop over each of the detections
		for detection in output:
			# extract the class ID and confidence (i.e., probability) of
			# the current object detection
			scores = detection[5:]
			classID = np.argmax(scores)
			confidence = scores[classID]
			# filter out weak predictions by ensuring the detected
			# probability is greater than the minimum probability
			if confidence >= min_confidence:
			# scale the bounding box coordinates back relative to the
		    # size of the image, keeping in mind that YOLO actually
		    # returns the center (x, y)-coordinates of the bounding
		    # box followed by the boxes' width and height
				box = detection[0:4] * np.array([W, H, W, H])
				(centerX, centerY, width, height) = box.astype("int")
				# use the center (x, y)-coordinates to derive the top and
		    	# and left corner of the bounding box
				x = int(centerX - (width / 2))
				y = int(centerY - (height / 2))
				# update our list of bounding box coordinates, confidences,
		    	# and class IDs
				boxes.append([x, y, int(width), int(height)])
				confidences.append(float(confidence))
				classIDs.append(classID)

	# apply non-maxima suppression to suppress weak, overlapping bounding
	# boxes
	idxs = cv2.dnn.NMSBoxes(boxes, confidences, min_confidence, threshold)

	#print(H//2, W)
	#white = np.full((H//2, W, 3), 255)
	#image = np.append(white, image, axis=0)
	#print(image.shape)


	name = img_path
	if '/' in name:
		name = name.split("/")[-1]
	print(name)

	class_data = []
	# ensure at least one detection exists
	if len(idxs) > 0:
		# loop over the indexes we are keeping
		for i in idxs.flatten():
		# extract the bounding box coordinates
			(x, y) = (boxes[i][0], boxes[i][1])
			(w, h) = (boxes[i][2], boxes[i][3])
			# draw a bounding box rectangle and label on the image
			color = [int(c) for c in COLORS[classIDs[i]]]
			if x < 0:
				x=0
			if y < 0:
				y=0
			cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
			#image[y:y + h, x:x + w] = cv2.blur(image[y:y + h, x:x + w], (50, 50))
			text = "{}: {:.4f}".format(LABELS[classIDs[i]], confidences[i])
			# print(text, (x, y))
			class_data.append(text + ' ' + str(x) + ' ' + str(y))
			cv2.putText(image, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.4, color, 2)

	def take_x_value(elem):
		elem = elem.split()
		return int(elem[2])

	class_data.sort(key=take_x_value)

	for box in class_data:
		print(box)

	# save the output image
	cv2.imwrite('results/'+name, image)

