import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

"""
Bài 3: Viết chương trình nạp một ảnh, chuyển thành hệ màu HSV và lưu 3 ảnh với 3 màu khác nhau.
"""

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

def exercise3():
    # Tạo thư mục để lưu ảnh nếu chưa tồn tại
    if not os.path.exists('output'):
        os.makedirs('output')
    
    # Đọc ảnh
    img = cv2.imread('sample_image.jpg')
    
    # Kiểm tra xem ảnh có được đọc thành công không
    if img is None:
        print("Không thể đọc ảnh. Vui lòng kiểm tra đường dẫn.")
        return
    
    # Chuyển từ BGR sang RGB để hiển thị
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # Chuyển từ BGR sang HSV
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    # Tách các kênh H, S, V
    h, s, v = cv2.split(img_hsv)
    
    # Tạo 3 ảnh HSV với 3 màu khác nhau
    # Ảnh 1: Thay đổi Hue (màu sắc)
    hsv_mod1 = img_hsv.copy()
    hsv_mod1[:, :, 0] = (hsv_mod1[:, :, 0] + 60) % 180  # Dịch màu sắc 60 độ
    
    # Ảnh 2: Thay đổi Saturation (độ bão hòa)
    hsv_mod2 = img_hsv.copy()
    hsv_mod2[:, :, 1] = np.clip(hsv_mod2[:, :, 1] * 1.5, 0, 255).astype(np.uint8)  # Tăng độ bão hòa
    
    # Ảnh 3: Thay đổi Value (độ sáng)
    hsv_mod3 = img_hsv.copy()
    hsv_mod3[:, :, 2] = np.clip(hsv_mod3[:, :, 2] * 0.7, 0, 255).astype(np.uint8)  # Giảm độ sáng
    
    # Chuyển các ảnh HSV trở lại BGR để lưu
    img_mod1 = cv2.cvtColor(hsv_mod1, cv2.COLOR_HSV2BGR)
    img_mod2 = cv2.cvtColor(hsv_mod2, cv2.COLOR_HSV2BGR)
    img_mod3 = cv2.cvtColor(hsv_mod3, cv2.COLOR_HSV2BGR)
    
    # Lưu các ảnh
    cv2.imwrite('output/hsv_hue_modified.jpg', img_mod1)
    cv2.imwrite('output/hsv_saturation_modified.jpg', img_mod2)
    cv2.imwrite('output/hsv_value_modified.jpg', img_mod3)
    
    # Chuyển các ảnh BGR về RGB để hiển thị
    img_mod1_rgb = cv2.cvtColor(img_mod1, cv2.COLOR_BGR2RGB)
    img_mod2_rgb = cv2.cvtColor(img_mod2, cv2.COLOR_BGR2RGB)
    img_mod3_rgb = cv2.cvtColor(img_mod3, cv2.COLOR_BGR2RGB)
    
    # Hiển thị ảnh
    plt.figure(figsize=(15, 10))
    
    plt.subplot(221)
    plt.imshow(img_rgb)
    plt.title('Ảnh gốc (RGB)')
    plt.axis('off')
    
    plt.subplot(222)
    plt.imshow(img_mod1_rgb)
    plt.title('Thay đổi Hue (màu sắc)')
    plt.axis('off')
    
    plt.subplot(223)
    plt.imshow(img_mod2_rgb)
    plt.title('Tăng Saturation (độ bão hòa)')
    plt.axis('off')
    
    plt.subplot(224)
    plt.imshow(img_mod3_rgb)
    plt.title('Giảm Value (độ sáng)')
    plt.axis('off')
    
    plt.tight_layout()
    plt.show()
    
    # Hiển thị các kênh H, S, V riêng biệt
    plt.figure(figsize=(15, 5))
    
    plt.subplot(131)
    plt.imshow(h, cmap='hsv')
    plt.title('Kênh H (Hue - Màu sắc)')
    plt.axis('off')
    
    plt.subplot(132)
    plt.imshow(s, cmap='gray')
    plt.title('Kênh S (Saturation - Độ bão hòa)')
    plt.axis('off')
    
    plt.subplot(133)
    plt.imshow(v, cmap='gray')
    plt.title('Kênh V (Value - Độ sáng)')
    plt.axis('off')
    
    plt.tight_layout()
    plt.show()
    
    print("Đã lưu 3 ảnh HSV với 3 màu khác nhau vào thư mục 'output'.")

# Chạy chương trình
if __name__ == "__main__":
    # Đảm bảo chúng ta đang ở đúng thư mục
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    create_sample_image()
    exercise3()
