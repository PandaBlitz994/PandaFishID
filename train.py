from ultralytics import YOLO

yolo = YOLO(r".\runs\detect\train28\weights\last.pt")
# yolo = YOLO('yolov8n.pt')
yolo.train(
    data='.\dataset\dataset.yaml',
    epochs = 1, # epochs = how many itirations the model will do
    batch = 18,
    optimizer = 'Adam'
)
valid_results = yolo.val()
print(valid_results)

