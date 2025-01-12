from ultralytics import YOLO
import cv2
import math 

trained_model = YOLO(r'runs\detect\train14\weights\best.pt')

classNames = ["Clown Fish", "Jaguer Gapote", "puffer"]

results = trained_model.predict(
    source = r"C:\Reps\PandaFishID\test_data", 
    conf = 0.05,
    save = True
)

