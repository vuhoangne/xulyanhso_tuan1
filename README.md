# Bài tập xử lý ảnh số

Repo này chứa các bài tập thực hành về xử lý ảnh số, sử dụng thư viện OpenCV và các thư viện hỗ trợ khác trong Python.

## Cài đặt

Để chạy các bài tập này, bạn cần cài đặt các thư viện sau:

```
pip install numpy opencv-python matplotlib
```

## Bài tập 1: Đọc và hiển thị ảnh

Bài tập này thực hiện các thao tác cơ bản với ảnh:
- Đọc ảnh từ file
- Hiển thị ảnh gốc
- Chuyển đổi ảnh sang ảnh xám (grayscale)
- Hiển thị ảnh xám
- Lưu ảnh xám ra file

Hàm `exercise1()` thực hiện các bước trên và lưu kết quả vào thư mục `bai1_output`.

## Bài tập 2: Hoán đổi kênh màu

Bài tập này thực hiện các thao tác hoán đổi kênh màu RGB của ảnh:
- Tạo một ảnh mẫu có các kênh màu R, G, B
- Hiển thị ảnh gốc
- Hoán đổi các kênh màu theo các cách khác nhau (RGB -> BGR, RGB -> GRB, v.v.)
- Hiển thị các ảnh đã hoán đổi kênh màu
- Lưu các ảnh kết quả ra file

Hàm `exercise2()` thực hiện các bước trên và lưu kết quả vào thư mục `bai2_output`.

## Bài tập 3: Chuyển đổi không gian màu

Bài tập này thực hiện chuyển đổi ảnh giữa các không gian màu khác nhau:
- Đọc ảnh từ file
- Chuyển đổi ảnh từ RGB sang các không gian màu khác (HSV, Lab, YCrCb)
- Hiển thị ảnh gốc và các ảnh đã chuyển đổi
- Lưu các ảnh kết quả ra file

Hàm `exercise3()` thực hiện các bước trên và lưu kết quả vào thư mục `bai3_output`.

## Bài tập 4: Phân tách kênh màu

Bài tập này thực hiện phân tách ảnh thành các kênh màu riêng biệt:
- Đọc ảnh từ file
- Phân tách ảnh thành các kênh màu R, G, B
- Hiển thị ảnh gốc và từng kênh màu riêng biệt
- Lưu các ảnh kết quả ra file

Hàm `exercise4()` thực hiện các bước trên và lưu kết quả vào thư mục `bai4_output`.

## Bài tập 5: Xử lý histogram

Bài tập này thực hiện các thao tác xử lý histogram của ảnh:
- Đọc ảnh từ file
- Tính toán và hiển thị histogram của ảnh
- Cân bằng histogram (histogram equalization)
- Hiển thị ảnh gốc và ảnh đã cân bằng histogram
- Lưu các ảnh kết quả ra file

Hàm `exercise5()` thực hiện các bước trên và lưu kết quả vào thư mục `bai5_output`.

## Bài tập 6: Khử nhiễu ảnh

Bài tập này áp dụng các bộ lọc khử nhiễu khác nhau cho ảnh:
- Gaussian Blur
- Median Blur
- Bilateral Filter

Hàm `exercise6()` thực hiện các bước trên và hiển thị kết quả.

## Bài tập 7: Xác định biên

Bài tập này sử dụng các bộ lọc để xác định biên của ảnh và lưu kết quả.

## Bài tập 8: Chương trình đổi màu RGB ngẫu nhiên

Chương trình này thực hiện đổi màu RGB ngẫu nhiên của các hình trong thư mục Exercise:
- Đọc ảnh từ file
- Hoán đổi ngẫu nhiên các kênh màu RGB
- Hiển thị và lưu kết quả

Hàm `randomize_rgb_colors()` thực hiện các bước trên và lưu kết quả vào thư mục `Random_RGB_Images`.

## Bài tập 9: Chương trình bổ sung

Bài tập này thực hiện các thao tác bổ sung theo yêu cầu cụ thể của bài tập.

## Cách chạy

Để chạy tất cả các bài tập, mở file `lab1_all_exercises.ipynb` trong Jupyter Notebook và chạy từng cell.

Hoặc bạn có thể chạy từng bài tập riêng biệt bằng cách gọi hàm tương ứng:

```python
from lab1_all_exercises import exercise1, exercise2, exercise3, exercise4, exercise5, exercise6, randomize_rgb_colors

# Chạy bài tập 1
exercise1()

# Chạy bài tập 2
exercise2()

# Chạy bài tập 3
exercise3()

# Chạy bài tập 4
exercise4()

# Chạy bài tập 5
exercise5()

# Chạy bài tập 6
exercise6()

# Chạy bài tập 7
# Add appropriate function call for Exercise 7 if needed

# Chạy bài tập 8
randomize_rgb_colors()

# Chạy bài tập 9
# Add appropriate function call for Exercise 9 if needed

```

## Lưu ý

- Mỗi bài tập sẽ tạo một thư mục output riêng để lưu kết quả
- Đảm bảo bạn có quyền ghi vào thư mục hiện tại để tạo các thư mục output
- Một số bài tập có thể yêu cầu ảnh đầu vào, hãy đảm bảo các file ảnh tồn tại trong đường dẫn được chỉ định
