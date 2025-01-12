from ultralytics import YOLO

trained_model = YOLO(r'C:\Reps\PandaFishID\runs\detect\train14\weights\best.pt')

results = trained_model.predict(

    source = r"C:\Reps\PandaFishID\test_data", 

    conf = 0.05,

    save = True
)

