import os
import numpy as np
import cv2
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, LSTM, Dense, Dropout, TimeDistributed
from tensorflow.keras.preprocessing.image import img_to_array
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical

# Load dataset
def load_data(data_dir, img_size=(64, 64), sequence_length=10):
    labels = {"violence": 1, "non_violence": 0}
    sequences, labels_list = [], []

    for label in labels:
        folder_path = os.path.join(data_dir, label)
        videos = os.listdir(folder_path)

        for video in videos:
            video_path = os.path.join(folder_path, video)
            frames = []

            cap = cv2.VideoCapture(video_path)
            while len(frames) < sequence_length:
                ret, frame = cap.read()
                if not ret:
                    break
                frame = cv2.resize(frame, img_size)
                frame = img_to_array(frame) / 255.0
                frames.append(frame)

            cap.release()

            if len(frames) == sequence_length:
                sequences.append(frames)
                labels_list.append(labels[label])

    return np.array(sequences), np.array(labels_list)

X, y = load_data("dataset/")
y = to_categorical(y, num_classes=2)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define model
model = Sequential([
    TimeDistributed(Conv2D(32, (3,3), activation='relu', input_shape=(64, 64, 3))),
    TimeDistributed(MaxPooling2D((2,2))),
    TimeDistributed(Conv2D(64, (3,3), activation='relu')),
    TimeDistributed(MaxPooling2D((2,2))),
    TimeDistributed(Flatten()),
    LSTM(64, return_sequences=False),
    Dense(64, activation='relu'),
    Dropout(0.5),
    Dense(2, activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=10, batch_size=8, validation_data=(X_test, y_test))

model.save("models/violence_detector.h5")
