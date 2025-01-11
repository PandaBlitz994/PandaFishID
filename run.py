from ultralytics import YOLO

trained_model = YOLO(r'C:\Reps\PandaFishID\runs\detect\train4\weights\last.pt')

results = trained_model.predict(
    source = r"C:\Reps\PandaFishID\test_data", 
    conf = 0.25,
    save = True
)

