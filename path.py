import cv2
from ultralytics import YOLO

model = YOLO("C:/Users/LENOVO/anaconda3/envs/Mediapipe_Anaconda/Fresh_Fruit/training/best.pt")

results = model("C:/Users/LENOVO/Downloads/download.jpg",show=True,save=True)