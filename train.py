from ultralytics import YOLO

yolo = YOLO('yolov8n.pt')
yolo.train(
    data='C:\Reps\PandaFishID\dataset\dataset.yaml',
    epochs = 300 # epochs = how many itirations the model has
)
valid_results = yolo.val()
print(valid_results)