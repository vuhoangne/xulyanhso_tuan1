import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

"""
Bài 5: Viết chương trình sử dụng mean filter cho các hình trong thư mục Exercise
"""

def create_sample_images():
    # Tạo thư mục để lưu ảnh mẫu nếu chưa tồn tại
    if not os.path.exists('Exercise'):
        os.makedirs('Exercise')
    
    # Tạo một số ảnh mẫu với các hình dạng khác nhau
    # Ảnh 1: Hình tròn
    circle_img = np.zeros((300, 300, 3), dtype=np.uint8)
    cv2.circle(circle_img, (150, 150), 100, (0, 0, 255), -1)
    cv2.imwrite('Exercise/circle.jpg', circle_img)
    
    # Ảnh 2: Hình vuông
    square_img = np.zeros((300, 300, 3), dtype=np.uint8)
    cv2.rectangle(square_img, (50, 50), (250, 250), (0, 255, 0), -1)
    cv2.imwrite('Exercise/square.jpg', square_img)
    
    # Ảnh 3: Hình tam giác
    triangle_img = np.zeros((300, 300, 3), dtype=np.uint8)
    triangle_pts = np.array([[150, 50], [50, 250], [250, 250]], np.int32)
    triangle_pts = triangle_pts.reshape((-1, 1, 2))
    cv2.fillPoly(triangle_img, [triangle_pts], (255, 0, 0))
    cv2.imwrite('Exercise/triangle.jpg', triangle_img)
    
    # Thêm nhiễu vào các ảnh để thấy rõ hiệu quả của mean filter
    # Ảnh 4: Hình tròn có nhiễu
    noisy_circle = circle_img.copy()
    noise = np.random.randint(0, 100, noisy_circle.shape, dtype=np.uint8)
    noisy_circle = cv2.add(noisy_circle, noise)
    cv2.imwrite('Exercise/noisy_circle.jpg', noisy_circle)
    
    # Ảnh 5: Hình vuông có nhiễu
    noisy_square = square_img.copy()
    noise = np.random.randint(0, 100, noisy_square.shape, dtype=np.uint8)
    noisy_square = cv2.add(noisy_square, noise)
    cv2.imwrite('Exercise/noisy_square.jpg', noisy_square)
    
    print("Đã tạo các ảnh mẫu trong thư mục 'Exercise'.")
    return True

def apply_mean_filter(image, kernel_size):
    """
    Áp dụng mean filter (bộ lọc trung bình) cho ảnh
    """
    return cv2.blur(image, (kernel_size, kernel_size))

def exercise5():
    # Tạo thư mục để lưu ảnh kết quả nếu chưa tồn tại
    if not os.path.exists('output'):
        os.makedirs('output')
    
    # Kiểm tra xem thư mục Exercise có tồn tại không
    if not os.path.exists('Exercise'):
        print("Thư mục 'Exercise' không tồn tại. Đang tạo ảnh mẫu...")
        create_sample_images()
    
    # Lấy danh sách các file ảnh trong thư mục Exercise
    image_files = [f for f in os.listdir('Exercise') if f.endswith(('.jpg', '.jpeg', '.png'))]
    
    if not image_files:
        print("Không tìm thấy ảnh trong thư mục 'Exercise'.")
        return
    
    # Áp dụng mean filter với các kích thước kernel khác nhau
    kernel_sizes = [3, 5, 9, 15]
    
    for image_file in image_files:
        # Đọc ảnh
        img_path = os.path.join('Exercise', image_file)
        img = cv2.imread(img_path)
        
        if img is None:
            print(f"Không thể đọc ảnh {img_path}. Bỏ qua.")
            continue
        
        # Chuyển từ BGR sang RGB để hiển thị
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        # Áp dụng mean filter với các kích thước kernel khác nhau
        filtered_images = []
        for kernel_size in kernel_sizes:
            filtered_img = apply_mean_filter(img, kernel_size)
            filtered_img_rgb = cv2.cvtColor(filtered_img, cv2.COLOR_BGR2RGB)
            filtered_images.append((filtered_img, filtered_img_rgb, kernel_size))
            
            # Lưu ảnh đã lọc
            output_filename = f"output/{os.path.splitext(image_file)[0]}_mean_{kernel_size}.jpg"
            cv2.imwrite(output_filename, filtered_img)
        
        # Hiển thị ảnh gốc và các ảnh đã lọc
        plt.figure(figsize=(15, 10))
        
        # Hiển thị ảnh gốc
        plt.subplot(2, 3, 1)
        plt.imshow(img_rgb)
        plt.title(f'Ảnh gốc: {image_file}')
        plt.axis('off')
        
        # Hiển thị các ảnh đã lọc
        for i, (_, filtered_rgb, kernel_size) in enumerate(filtered_images):
            plt.subplot(2, 3, i + 2)
            plt.imshow(filtered_rgb)
            plt.title(f'Mean Filter (kernel={kernel_size}x{kernel_size})')
            plt.axis('off')
        
        plt.tight_layout()
        plt.savefig(f"output/{os.path.splitext(image_file)[0]}_comparison.jpg")
        plt.show()
    
    print("Đã áp dụng mean filter cho tất cả các ảnh trong thư mục 'Exercise' và lưu kết quả vào thư mục 'output'.")

# Chạy chương trình
if __name__ == "__main__":
    # Đảm bảo chúng ta đang ở đúng thư mục
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    exercise5()
