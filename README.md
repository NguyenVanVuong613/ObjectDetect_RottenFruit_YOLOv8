# NHẬN DIỆN HOA QUẢ TƯƠI HOẶC HƯ HẠI SỬ DỤNG YOLOV8 VÀ FLASK API
Dự án này triển khai hệ thống phát hiện đối tượng bằng YOLOv8, một mô hình học sâu tiên tiến để phát hiện đối tượng theo thời gian thực, được tích hợp với API Flask để triển khai dịch vụ web. Hệ thống phát hiện và phân loại các đối tượng trong luồng hình ảnh hoặc video, cung cấp nền tảng mạnh mẽ cho nhiều ứng dụng khác nhau như giám sát, hệ thống tự động, v.v.

## Cài đặt chương trình

### Clone Repository

```sh
git clone https://github.com/NguyenVanVuong613/ObjectDetect_RottenFruit_YOLOv8.git
cd ObjectDetect_RottenFruit_YOLOv8
```

### Tải các thư viện cần thiết
```cmd
pip install -r requirements.txt
```

## Chạy chương trình
Chương trình có 2 tính năng chính đó là nhận diện thời gian thực và nhận diện qua file path

## Chạy chương trình nhận diện qua ảnh
Mở terminal và chạy lệnh:
### 
```cmd
python app.py
```
Sau khi chạy chương trình sẽ hiện lên:
![image](https://github.com/NguyenVanVuong613/ObjectDetect_RottenFruit_YOLOv8/assets/171783698/8ac665c8-e9bc-44e7-9831-ca7ce02053b1)

Click vào một trong 2 địa chỉ và màn hình trình duyệt sẽ hiện lên như sau:
![image](https://github.com/NguyenVanVuong613/ObjectDetect_RottenFruit_YOLOv8/assets/171783698/77b2107b-7c6d-40b7-aecf-a084ac0f2034)

Chọn file ảnh trong thư mục, ấn upload và đợi kết quả nhận diện

## Chạy chương trình nhận diện thời gian thực
Mở terminal và chạy lệnh:
### 
```cmd
python real_time.py
```

Chương trình sẽ hiện lên cửa sổ camera cho việc nhận diện
Ấn q để thoát chương trình
