from ultralytics import YOLO

yolo = YOLO(r".\runs\detect\train27\weights\best.pt")
# yolo = YOLO('yolov8n.pt')
yolo.train(
    data='.\dataset\dataset.yaml',
    epochs = 66, # epochs = how many itirations the model has
    batch = 18,
    optimizer = 'Adam'
)
valid_results = yolo.val()
print(valid_results)

