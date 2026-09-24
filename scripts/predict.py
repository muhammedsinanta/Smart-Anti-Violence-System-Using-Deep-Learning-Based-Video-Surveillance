import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model

model = load_model("models/violence_detector.h5")

def predict_video(video_path, img_size=(64, 64), sequence_length=10):
    frames = []
    cap = cv2.VideoCapture(video_path)

    while len(frames) < sequence_length:
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.resize(frame, img_size)
        frame = frame / 255.0
        frames.append(frame)

    cap.release()

    if len(frames) == sequence_length:
        frames = np.array([frames])
        prediction = model.predict(frames)[0]
        return "Violence" if np.argmax(prediction) == 1 else "Non-Violence"
    else:
        return "Insufficient frames for prediction"

# Example usage:
# print(predict_video("test_video.mp4"))
