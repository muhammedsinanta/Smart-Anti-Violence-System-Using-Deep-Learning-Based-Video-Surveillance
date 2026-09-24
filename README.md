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

- Python
- Deep Learning
- Computer Vision
- TensorFlow / Keras
- OpenCV
- NumPy
- YOLOv7
- CNN
- Flask
- Jupyter Notebook

---

## 🔄 System Workflow

```text
Video Input
     ↓
Video Preprocessing
     ↓
Frame Processing
     ↓
Deep Learning / Computer Vision Model
     ↓
Violence Detection
     ↓
Prediction Result
     ↓
Application Output
```

## 🏗️ System Architecture

The project follows a video surveillance pipeline consisting of data collection, preprocessing, feature/model processing, model development, training/testing and deployment.

The overall workflow is:

Data Collection
       ↓
Data Preprocessing
       ↓
Exploratory Data Analysis
       ↓
Model Implementation
       ↓
Deep Learning / Computer Vision
       ↓
Model Training & Testing
       ↓
Video Input
       ↓
Violence Prediction
       ↓
Application Output

## 📊 Model Performance

The model was evaluated using standard classification metrics.

Metric	Score
Accuracy	84%
Precision	80%
Recall	100%
F1-Score

## 🧪 Evaluation Metrics

The project evaluates the violence detection model using:

Accuracy
Precision
Recall
F1-Score
Classification Report

These metrics are used to evaluate the model's ability to identify violent and non-violent video samples.

## 📁 Project Structure

smart-anti-violence-detection/
│
├── models/
│   └── Model-related files
│
├── presentation/
│   └── Project presentation
│
├── scripts/
│   └── Supporting scripts
│
├── static/
│   └── CSS, JavaScript and static assets
│
├── templates/
│   └── HTML templates
│
├── utils/
│   └── Utility modules
│
├── app.py
├── create_database.py
├── predict.py
├── utils1.py
├── __init__.py
├── violence_project.ipynb
├── violence_detector.h5
├── requirements.txt
├── README.md

```

##🧠 Trained Model

The repository includes the trained deep learning model:

violence_detector.h5

The trained model is used by the prediction pipeline to generate violence detection results from video input.

