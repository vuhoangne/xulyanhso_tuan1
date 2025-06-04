import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# Tạo ảnh mẫu đơn giản
def create_sample_image():
    # Tạo một ảnh mẫu đơn giản (300x300 với 3 kênh màu)
    sample_img = np.zeros((300, 300, 3), dtype=np.uint8)
    
    # Tạo một số hình dạng với màu sắc khác nhau
    # Hình tròn đỏ
    cv2.circle(sample_img, (150, 150), 100, (0, 0, 255), -1)
    # Hình vuông xanh lá
    cv2.rectangle(sample_img, (50, 50), (250, 250), (0, 255, 0), 10)
    # Đường chéo xanh dương
    cv2.line(sample_img, (0, 0), (300, 300), (255, 0, 0), 5)
    
    # Lưu ảnh mẫu
    cv2.imwrite('sample_image.jpg', sample_img)
    print("Đã tạo ảnh mẫu thành công!")
    return True

#bai1
def exercise1():
    """
    Viết chương trình nạp một ảnh và lưu thành 3 ảnh với 3 màu khác nhau
    """
    # Đọc ảnh
    img = cv2.imread('sample_image.jpg')
    
    # Kiểm tra xem ảnh có được đọc thành công không
    if img is None:
        print("Không thể đọc ảnh. Vui lòng kiểm tra đường dẫn.")
        return
    
    # Chuyển từ BGR sang RGB để hiển thị
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # Tạo 3 ảnh với 3 màu khác nhau
    # Ảnh 1: Chỉ giữ kênh đỏ
    red_img = img_rgb.copy()
    red_img[:, :, 1] = 0  # Xóa kênh xanh lá
    red_img[:, :, 2] = 0  # Xóa kênh xanh dương
    
    # Ảnh 2: Chỉ giữ kênh xanh lá
    green_img = img_rgb.copy()
    green_img[:, :, 0] = 0  # Xóa kênh đỏ
    green_img[:, :, 2] = 0  # Xóa kênh xanh dương
    
    # Ảnh 3: Chỉ giữ kênh xanh dương
    blue_img = img_rgb.copy()
    blue_img[:, :, 0] = 0  # Xóa kênh đỏ
    blue_img[:, :, 1] = 0  # Xóa kênh xanh lá
    
    # Lưu các ảnh
    cv2.imwrite('red_image.jpg', cv2.cvtColor(red_img, cv2.COLOR_RGB2BGR))
    cv2.imwrite('green_image.jpg', cv2.cvtColor(green_img, cv2.COLOR_RGB2BGR))
    cv2.imwrite('blue_image.jpg', cv2.cvtColor(blue_img, cv2.COLOR_RGB2BGR))
    
    # Hiển thị ảnh
    plt.figure(figsize=(15, 5))
    
    plt.subplot(141)
    plt.imshow(img_rgb)
    plt.title('Ảnh gốc')
    plt.axis('off')
    
    plt.subplot(142)
    plt.imshow(red_img)
    plt.title('Ảnh kênh đỏ')
    plt.axis('off')
    
    plt.subplot(143)
    plt.imshow(green_img)
    plt.title('Ảnh kênh xanh lá')
    plt.axis('off')
    
    plt.subplot(144)
    plt.imshow(blue_img)
    plt.title('Ảnh kênh xanh dương')
    plt.axis('off')
    
    plt.tight_layout()
    plt.show()
    
    print("Đã lưu 3 ảnh với 3 màu khác nhau.")

# Chạy chương trình
if __name__ == "__main__":
    create_sample_image()
    exercise1()
