from ultralytics import YOLO

yolo = YOLO('yolov8n.pt')
yolo.train(
    data='C:\Reps\PandaFishID\dataset\dataset.yaml',
    epochs = 100 # epochs = how many times the model sees all the dateset
)
valid_results = yolo.val()
print(valid_results)