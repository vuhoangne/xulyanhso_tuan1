import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

"""
Bài 2: Viết chương trình nạp một ảnh và hoán đổi giá trị các màu. Lưu các ảnh vào máy.
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

def exercise2():
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
    
    # Hoán đổi các kênh màu
    # 1. Hoán đổi R và G (Red và Green)
    rg_swapped = img_rgb.copy()
    rg_swapped[:, :, [0, 1]] = rg_swapped[:, :, [1, 0]]
    
    # 2. Hoán đổi R và B (Red và Blue)
    rb_swapped = img_rgb.copy()
    rb_swapped[:, :, [0, 2]] = rb_swapped[:, :, [2, 0]]
    
    # 3. Hoán đổi G và B (Green và Blue)
    gb_swapped = img_rgb.copy()
    gb_swapped[:, :, [1, 2]] = gb_swapped[:, :, [2, 1]]
    
    # 4. Hoán đổi tất cả các kênh (R->G, G->B, B->R)
    all_swapped = img_rgb.copy()
    all_swapped[:, :, [0, 1, 2]] = all_swapped[:, :, [1, 2, 0]]
    
    # Lưu các ảnh
    cv2.imwrite('output/rg_swapped.jpg', cv2.cvtColor(rg_swapped, cv2.COLOR_RGB2BGR))
    cv2.imwrite('output/rb_swapped.jpg', cv2.cvtColor(rb_swapped, cv2.COLOR_RGB2BGR))
    cv2.imwrite('output/gb_swapped.jpg', cv2.cvtColor(gb_swapped, cv2.COLOR_RGB2BGR))
    cv2.imwrite('output/all_swapped.jpg', cv2.cvtColor(all_swapped, cv2.COLOR_RGB2BGR))
    
    # Hiển thị ảnh
    plt.figure(figsize=(15, 10))
    
    plt.subplot(231)
    plt.imshow(img_rgb)
    plt.title('Ảnh gốc')
    plt.axis('off')
    
    plt.subplot(232)
    plt.imshow(rg_swapped)
    plt.title('Hoán đổi R và G')
    plt.axis('off')
    
    plt.subplot(233)
    plt.imshow(rb_swapped)
    plt.title('Hoán đổi R và B')
    plt.axis('off')
    
    plt.subplot(234)
    plt.imshow(gb_swapped)
    plt.title('Hoán đổi G và B')
    plt.axis('off')
    
    plt.subplot(235)
    plt.imshow(all_swapped)
    plt.title('Hoán đổi tất cả (R->G, G->B, B->R)')
    plt.axis('off')
    
    plt.tight_layout()
    plt.show()
    
    print("Đã lưu các ảnh hoán đổi màu vào thư mục 'output'.")

# Chạy chương trình
if __name__ == "__main__":
    # Đảm bảo chúng ta đang ở đúng thư mục
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    create_sample_image()
    exercise2()
