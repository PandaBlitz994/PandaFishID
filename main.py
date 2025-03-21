import cv2
from ultralytics import YOLO
import yaml
import math

confidenceMin = 0.5 # 0.5 = 50%, thats the minimum confidunce for a detection to happen.
NewFishMin = 0.25

cap = cv2.VideoCapture(0)
cap.set(3, 1980)
cap.set(4, 1080)

trained_model = YOLO(r'runs\detect\train28\weights\best.pt')

with open(r"dataset/dataset.yaml", "r") as file:
    data = yaml.safe_load(file)

classNames = data["names"]


while True:
    success, img = cap.read()
    results = trained_model(img, stream=True)
    for r in results:
        boxes = r.boxes

    for box in boxes:
        # bounding box
        x1, y1, x2, y2 = box.xyxy[0]
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2) # convert to int values

        # put box in cam
        

        # confidence
        confidence = math.ceil((box.conf[0]*100))/100
        # if confidence < 0.4 and confidence > NewFishMin:
        #     org = [x1, y1 - 10]  # Position text slightly above the bounding box
        #     font = cv2.FONT_HERSHEY_TRIPLEX
        #     fontScale = 1
        #     color = (0, 0, 255)  # Red color for "new fish"
        #     thickness = 4
        #     cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
        #     cv2.putText(img, "new fish", org, font, fontScale, color, thickness)
        #     continue
        # elif confidence < NewFishMin:
        #     continue
        print("Confidence --->",confidence)

        # class name
        cls = int(box.cls[0])
        print("Class name -->", classNames[cls])

        # object details
        
        org = [x1, y1 - 10]
        font = cv2.FONT_HERSHEY_TRIPLEX
        fontScale = 1
        color = (255, 0, 0)
        thickness = 2
        if confidence > confidenceMin:
            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
            cv2.putText(img, classNames[cls] + " " + str(int(confidence*100)) + "%", org, font, fontScale, color, thickness)

    cv2.imshow('Webcam', img)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()