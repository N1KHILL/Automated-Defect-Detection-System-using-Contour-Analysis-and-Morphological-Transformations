## 📌 Project Overview
The **Automated Surface Defect Detector** is a Computer Vision-based quality assurance tool designed for industrial manufacturing environments. It automates the detection of physical anomalies—such as cracks, voids, and surface irregularities—on mechanical components. 

By utilizing deterministic image processing techniques rather than heavy deep learning models, this tool remains lightweight, explainable, and capable of real-time execution in resource-constrained environments.

---

## 🚀 Getting Started

Follow these steps to set up the environment and run the project locally.

### 1. Prerequisites
* **Python 3.8 or higher**
* **pip** (Python package installer)

### 2. Environment Setup
Clone the repository and navigate to the project root:
```bash
git clone [https://github.com/](https://github.com/){your-username}/{repo-name}.git
cd {repo-name}
```

Create and activate a virtual environment (recommended):
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Installation
Install the necessary dependencies using the provided requirements file:
```bash
pip install -r requirements.txt
```
*Note: Primary dependencies include `opencv-python` and `numpy`.*

---

## 💻 Usage

This project is fully executable via the command line. Ensure your input images are located in the `data/` folder (or provide a direct path).

### Running the Detector
Run the following command in your terminal:
```bash
python src/main.py --image data/sample_part.jpg
```

### Command Line Arguments
| Argument | Description | Required |
| :--- | :--- | :--- |
| `--image` | Path to the input image file for analysis. | Yes |

---

## 🛠 Technical Pipeline
The system processes images through a multi-stage Computer Vision pipeline:

1.  **Preprocessing:** Grayscale conversion and Gaussian Blurring to eliminate high-frequency noise.
2.  **Adaptive Segmentation:** Uses localized thresholding to handle uneven industrial lighting conditions.
3.  **Morphological Refining:** Employs 'Closing' operations to unify fragmented defect pixels.
4.  **Contour Filtering:** Identifies and measures structural anomalies, filtering out noise based on a minimum area threshold ($Area > \epsilon$).

---

## 📁 Repository Structure
```text
├── data/               # Contains sample test images (Good/Defective)
├── src/                
│   └── main.py         # Primary CLI Entry point and CV logic
├── requirements.txt    # Project dependencies
├── README.md           # Project documentation
└── Report.pdf          # Detailed technical analysis
```

---

## ⚖️ License
This project is licensed under the MIT License - see the LICENSE file for details.
```

---

### Important Final Reminders for your GitHub:

1.  **Requirements File:** Ensure you have a file named `requirements.txt` in your root directory containing:
    ```text
    opencv-python
    numpy
    ```
2.  **Data Folder:** Make sure to upload at least one or two sample images to a folder named `data` so the evaluator can actually run your example command.
3.  **No GUI:** As mentioned earlier, ensure your code uses `cv2.imwrite()` to save results and **does not** use `cv2.imshow()`, as automated testing environments usually do not have a display attached and will crash.

Would you like me to help you draft the `requirements.txt` file or generate some dummy data instructions?
