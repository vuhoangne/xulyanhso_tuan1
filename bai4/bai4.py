import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

"""
Bài 4: Viết chương trình nạp một ảnh, chuyển sang hệ màu HSV. Lưu ảnh mới với kênh Hmax= 1/3 Hcũ, Vmax = 3 Vcũ.
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

def exercise4():
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
    
    # Tạo ảnh mới với kênh Hmax = 1/3 Hcũ, Vmax = 3 Vcũ
    h_new = (h / 3).astype(np.uint8)  # Hmax = 1/3 Hcũ
    v_new = np.clip(v * 3, 0, 255).astype(np.uint8)  # Vmax = 3 Vcũ
    
    # Tạo ảnh HSV mới
    img_hsv_new = cv2.merge([h_new, s, v_new])
    
    # Chuyển ảnh HSV mới về BGR để lưu
    img_new = cv2.cvtColor(img_hsv_new, cv2.COLOR_HSV2BGR)
    
    # Lưu ảnh
    cv2.imwrite('output/hsv_modified.jpg', img_new)
    
    # Chuyển ảnh BGR về RGB để hiển thị
    img_new_rgb = cv2.cvtColor(img_new, cv2.COLOR_BGR2RGB)
    
    # Hiển thị ảnh gốc và ảnh đã chỉnh sửa
    plt.figure(figsize=(12, 6))
    
    plt.subplot(121)
    plt.imshow(img_rgb)
    plt.title('Ảnh gốc (RGB)')
    plt.axis('off')
    
    plt.subplot(122)
    plt.imshow(img_new_rgb)
    plt.title('Ảnh mới (Hmax=1/3 Hcũ, Vmax=3 Vcũ)')
    plt.axis('off')
    
    plt.tight_layout()
    plt.show()
    
    # Hiển thị các kênh H, S, V trước và sau khi chỉnh sửa
    plt.figure(figsize=(15, 10))
    
    plt.subplot(231)
    plt.imshow(h, cmap='hsv')
    plt.title('Kênh H gốc')
    plt.axis('off')
    
    plt.subplot(232)
    plt.imshow(s, cmap='gray')
    plt.title('Kênh S gốc')
    plt.axis('off')
    
    plt.subplot(233)
    plt.imshow(v, cmap='gray')
    plt.title('Kênh V gốc')
    plt.axis('off')
    
    plt.subplot(234)
    plt.imshow(h_new, cmap='hsv')
    plt.title('Kênh H mới (1/3 Hcũ)')
    plt.axis('off')
    
    plt.subplot(235)
    plt.imshow(s, cmap='gray')
    plt.title('Kênh S (không đổi)')
    plt.axis('off')
    
    plt.subplot(236)
    plt.imshow(v_new, cmap='gray')
    plt.title('Kênh V mới (3 Vcũ)')
    plt.axis('off')
    
    plt.tight_layout()
    plt.show()
    
    print("Đã lưu ảnh mới với kênh Hmax=1/3 Hcũ, Vmax=3 Vcũ vào thư mục 'output'.")

# Chạy chương trình
if __name__ == "__main__":
    # Đảm bảo chúng ta đang ở đúng thư mục
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    create_sample_image()
    exercise4()
