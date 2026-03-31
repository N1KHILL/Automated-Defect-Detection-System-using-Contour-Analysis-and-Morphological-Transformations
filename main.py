import cv2
import numpy as np
import argparse
import sys

def detect_defects(image_path):
    # 1. Load and Grayscale
    img = cv2.imread(image_path)
    if img is None:
        print(f"Error: Could not load image at {image_path}")
        return
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # 2. Gaussian Blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # 3. Canny Edge Detection or Thresholding
    # Here we use Adaptive Thresholding for varying lighting
    thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                   cv2.THRESH_BINARY_INV, 11, 2)
    
    # 4. Morphological Operations to close gaps
    kernel = np.ones((3,3), np.uint8)
    closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    
    # 5. Contour Detection
    contours, _ = cv2.findContours(closing, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    defect_count = 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 100:  # Threshold to ignore small noise
            defect_count += 1
            cv2.drawContours(img, [cnt], -1, (0, 0, 255), 2)

    print(f"Analysis Complete: Found {defect_count} potential defects.")
    cv2.imwrite('output_result.png', img)
    print("Result saved as output_result.png")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CV Defect Detector CLI")
    parser.add_argument("--image", required=True, help="Path to the input image")
    args = parser.parse_args()
    detect_defects(args.image)
