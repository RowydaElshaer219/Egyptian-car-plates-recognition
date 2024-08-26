import os
from ultralytics import YOLO
import cv2
from sort.sort import *
from util import get_car, read_license_plate, write_csv

# Change working directory
os.chdir(r"C:/Users/FreeComp/Downloads/palte222/Automatic-number-plate-recognition-in-real-time-")

# Initialize models and video capture
coco_model = YOLO("yolov8n.pt")
license_plate_detector = YOLO("best.pt")
cap = cv2.VideoCapture("WhatsApp Video 2023-11-21 at 00.18.32_3e72cc76.mp4")

mot_tracker = Sort()
vehicles = [2, 3, 5, 7]  # Classes for vehicle detection

results = {}
frame_nmr = -1
ret, frame = cap.read()

while ret:
    frame_nmr += 1
    ret, frame = cap.read()

    if ret:
        results[frame_nmr] = {}

        # Detect vehicles
        detections = coco_model(frame)[0]
        detections_ = []

        for detection in detections.boxes.data.tolist():
            x1, y1, x2, y2, score, class_id = detection
            if int(class_id) in vehicles:
                detections_.append([x1, y1, x2, y2, score])

        # Update tracker
        track_ids = mot_tracker.update(np.asarray(detections_))

        # Detect license plates
        license_plates = license_plate_detector(frame)[0]

        for license_plate in license_plates.boxes.data.tolist():
            x1, y1, x2, y2, score, class_id = license_plate

            xcar1, ycar1, xcar2, ycar2, car_id = get_car(license_plate, track_ids)

            if car_id != -1:
                license_plate_crop = frame[int(y1):int(y2), int(x1):int(x2), :]
                license_plate_crop_gray = cv2.cvtColor(license_plate_crop, cv2.COLOR_BGR2GRAY)
                _, license_plate_crop_thresh = cv2.threshold(license_plate_crop_gray, 64, 255, cv2.THRESH_BINARY_INV)

                license_plate_text, license_plate_text_score = read_license_plate(license_plate_crop_thresh)

                if license_plate_text is not None:
                    results[frame_nmr][car_id] = {
                        'car': {'bbox': [xcar1, ycar1, xcar2, ycar2]},
                        'license_plate': {
                            'bbox': [x1, y1, x2, y2],
                            'text': license_plate_text,
                            'bbox_score': score,
                            'text_score': license_plate_text_score
                        }
                    }
