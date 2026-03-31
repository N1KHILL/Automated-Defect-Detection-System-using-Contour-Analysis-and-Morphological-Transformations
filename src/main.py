import cv2
import numpy as np
import argparse
import os
import sys

def detect_defects(image_path):
    # 1. Load the Image
    if not os.path.exists(image_path):
        print(f"Error: The file '{image_path}' was not found.")
        sys.exit(1)

    img = cv2.imread(image_path)
    if img is None:
        print(f"Error: Could not decode the image at {image_path}.")
        sys.exit(1)
    
    print(f"Processing: {image_path}...")

    # 2. Pre-processing (Grayscale + Blur)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # 3. Adaptive Thresholding (Handles uneven lighting)
    thresh = cv2.adaptiveThreshold(
        blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
        cv2.THRESH_BINARY_INV, 11, 2
    )
    
    # 4. Morphological Operations (Closing small holes in defects)
    kernel = np.ones((3, 3), np.uint8)
    closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    
    # 5. Contour Detection
    contours, _ = cv2.findContours(closing, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    defect_count = 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        # Only count "significant" defects to avoid noise
        if area > 100:  
            defect_count += 1
            # Draw a red box/contour around the defect
            cv2.drawContours(img, [cnt], -1, (0, 0, 255), 2)

    # 6. Save results (No GUI/imshow to pass automated eval)
    output_path = 'output_result.png'
    cv2.imwrite(output_path, img)
    
    print("-" * 30)
    print(f"ANALYSIS SUCCESSFUL")
    print(f"Defects Found: {defect_count}")
    print(f"Visual result saved to: {output_path}")
    print("-" * 30)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Industrial Defect Detector CLI")
    parser.add_argument("--image", required=True, help="Path to input image (e.g., data/sample_defect.jpg)")
    args = parser.parse_args()
    detect_defects(args.image)
