# Smart Anti-Violence System Using Deep Learning Based Video Surveillance

## 📌 Project Overview

A deep learning-based video surveillance system designed to automatically detect violent activities from video input. The system aims to automate violence monitoring and support faster identification of potentially violent incidents in surveillance footage.

The project combines deep learning and computer vision techniques with a web-based application for processing video input and generating violence detection results.

---

## 🎯 Objectives

- Automatically detect violent activities from surveillance video.
- Reduce dependence on continuous manual monitoring.
- Process video input using deep learning and computer vision techniques.
- Generate automated violence detection results.
- Provide a foundation for real-time violence monitoring and alert systems.

---

## 🧠 Technologies Used

- **Programming Language:** Python
- **Deep Learning:** TensorFlow, Keras
- **Computer Vision:** OpenCV
- **Numerical Computing:** NumPy
- **Data Analysis:** Pandas
- **Machine Learning Utilities:** Scikit-learn
- **Visualization:** Matplotlib
- **Video Processing:** MoviePy
- **Web Framework:** Flask
- **Password Hashing:** Argon2
- **Development Environment:** Jupyter Notebook, Anaconda

---

## 🧠 Deep Learning Model

The project uses a trained deep learning model to classify video sequences as violent or non-violent.

**Model file:** `violence_detector.h5`

**Classification categories:**

- `0` — Non-Violence
- `1` — Violence

The model processes video frames and produces a classification result based on the learned patterns in the training data.

The model is integrated into the project's prediction and application workflows.

---

## ⚙️ Project Workflow

```text
Video Input
     |
     v
Video Processing
     |
     v
Frame Extraction
     |
     v
Frame Preprocessing
     |
     v
Trained Deep Learning Model
     |
     v
Violence Classification
     |
     v
Violence / Non-Violence Result
```

---

## 📊 Model Performance

The model was evaluated using standard classification metrics.

| Evaluation Metric | Score |
|---|---:|
| Accuracy | 84% |
| Precision | 80% |
| Recall | 100% |
| F1-Score | 88.89% |

These metrics are used to evaluate the model's ability to identify violent and non-violent video samples.
**Note:** These results reflect the evaluated test dataset. Performance on real-world surveillance footage may differ depending on video quality, lighting, camera angle, and the characteristics of the input data.

---

## 📁 Project Structure

```text
smart-anti-violence-detection/
│
├── models/                   # Model-related files
├── scripts/                  # Supporting scripts
├── static/                   # Static web application assets
├── templates/                # Flask HTML templates
├── utils/                    # Utility modules
├── presentation/             # Project presentation
│
├── app.py                    # Main Flask application
├── predict.py                # Prediction functionality
├── create_database.py        # Database creation and setup
├── utils1.py                 # Supporting utility functions
├── __init__.py                # Python package initialization
├── violence_project.ipynb     # Project notebook
├── violence_detector.h5      # Trained deep learning model
├── requirements.txt          # Python dependencies
├── .gitignore                # Files excluded from Git
└── README.md                 # Project documentation
```

*The directory listing describes the intended project organization. Some folders or files may be excluded from the public GitHub repository, particularly large datasets and generated files.*

---



