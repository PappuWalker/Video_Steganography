import cv2
import numpy as np

def text_to_binary(text):
    return ''.join(format(ord(char), '08b') for char in text)

def hide_message(video_path, message, output_path):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error: Could not open video file {video_path}")
        return

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    binary_message = text_to_binary(message) + '0' * 32  # Add 32 zeros as end marker
    message_index = 0
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if message_index < len(binary_message):
            for i in range(frame.shape[0]):
                for j in range(frame.shape[1]):
                    for k in range(3):
                        if message_index < len(binary_message):
                            frame[i, j, k] = (frame[i, j, k] & 254) | int(binary_message[message_index])
                            message_index += 1
                        else:
                            break
                if message_index >= len(binary_message):
                    break
            if message_index >= len(binary_message):
                break

        out.write(frame)

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        out.write(frame)

    cap.release()
    out.release()
    print(f"Message hidden in video: {output_path}")
    print(f"Message length: {len(message)} characters, {len(binary_message)} bits")
    print(f"Binary message: {binary_message}")

# Example usage
input_video = "C:\\Users\\admin\\Desktop\\stegno\\main_models\\stegno2.mp4"
output_video = "C:\\Users\\admin\\Desktop\\stegno\\main_models\\encrypted.mp4"
secret_message = "your secret shit here"

hide_message(input_video, secret_message, output_video)