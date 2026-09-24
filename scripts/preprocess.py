import cv2
import os

def extract_frames(video_path, output_folder, frame_rate=5):
    os.makedirs(output_folder, exist_ok=True)
    cap = cv2.VideoCapture(video_path)
    count = 0
    frame_count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        if count % frame_rate == 0:
            frame_path = os.path.join(output_folder, f"frame_{frame_count}.jpg")
            cv2.imwrite(frame_path, frame)
            frame_count += 1
        count += 1

    cap.release()
    cv2.destroyAllWindows()

# Example usage
# extract_frames("sample.mp4", "frames/")
