# DETECTING FRESH OR ROTTEN FRUITS USING YOLOv8 AND FLASK API
This project implements an object detection system using YOLOv8, an advanced deep learning model for real-time object detection, integrated with Flask API for deploying a web service. The system detects and classifies objects in image or video streams, providing a robust platform for various applications such as monitoring, automation systems, etc.

## Installing the program

### Clone Repository

```sh
git clone https://github.com/NguyenVanVuong613/ObjectDetect_RottenFruit_YOLOv8.git
cd ObjectDetect_RottenFruit_YOLOv8
```

### Install necessary libraries
```cmd
pip install -r requirements.txt
```

## Running the program
The program has 2 main features: real-time detection and detection via file path.

## Running image detection
Open terminal and run:
### 
```cmd
python app.py
```
After running, the program will display:
![image](https://github.com/NguyenVanVuong613/ObjectDetect_RottenFruit_YOLOv8/assets/171783698/8ac665c8-e9bc-44e7-9831-ca7ce02053b1)

Click on one of the 2 addresses and the browser screen will appear as follows:
![image](https://github.com/NguyenVanVuong613/ObjectDetect_RottenFruit_YOLOv8/assets/171783698/77b2107b-7c6d-40b7-aecf-a084ac0f2034)

Select an image file from the directory, press upload, and wait for detection results.

## Running real-time detection
Open terminal and run:
### 
```cmd
python real_time.py
```

The program will display a camera window for detection.
Press 'q' to exit the program.
