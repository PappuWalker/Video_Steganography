import cv2
import numpy as np

def text_to_binary(text):
    return ''.join(format(ord(char), '08b') for char in text)

def hide_message(video_path, message, output_path):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error: Could not open video file {video_path}")
        return
    
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
    
    binary_message = text_to_binary(message) + '1111111111111110'  # EOF marker
    message_index = 0
    
    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        frame_count += 1
        for i in range(frame.shape[0]):
            for j in range(frame.shape[1]):
                for k in range(3):  # RGB channels
                    if message_index < len(binary_message):
                        frame[i, j, k] = (frame[i, j, k] & 254) | int(binary_message[message_index])
                        message_index += 1
                    else:
                        out.write(frame)
                        cap.release()
                        out.release()
                        print(f"Processed {frame_count} frames")
                        print(f"Message length: {len(message)} characters, {len(binary_message)} bits")
                        return
        
        out.write(frame)
    
    cap.release()
    out.release()
    print(f"Processed {frame_count} frames")
    print(f"Message length: {len(message)} characters, {len(binary_message)} bits")

def extract_message(video_path):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error: Could not open video file {video_path}")
        return None
    
    binary_message = ""
    frame_count = 0
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        frame_count += 1
        for i in range(frame.shape[0]):
            for j in range(frame.shape[1]):
                for k in range(3):  # RGB channels
                    binary_message += str(frame[i, j, k] & 1)
                    if binary_message[-16:] == '1111111111111110':
                        cap.release()
                        extracted = ''.join(chr(int(binary_message[i:i+8], 2)) for i in range(0, len(binary_message)-16, 8))
                        print(f"Processed {frame_count} frames")
                        print(f"Extracted binary length: {len(binary_message)} bits")
                        return extracted
    
    cap.release()
    print(f"Processed {frame_count} frames")
    print(f"Extracted binary length: {len(binary_message)} bits")
    print("Warning: EOF marker not found")
    return None

# Example usage
input_video = "C:\\Users\\admin\\Desktop\\stegno\\stegno2.mp4"
output_video = "C:\\Users\\admin\\Desktop\\stegno\\stegno3.mp4"
secret_message = "Jerr!!!"

hide_message(input_video, secret_message, output_video)
print("Message hiding complete.")

extracted_message = extract_message(output_video)
print(f"Extracted message: {extracted_message}")

# Verify input video
cap = cv2.VideoCapture(input_video)
if not cap.isOpened():
    print(f"Error: Could not open input video file {input_video}")
else:
    print(f"Input video opened successfully: {input_video}")
    print(f"Video properties:")
    print(f"  Frames: {int(cap.get(cv2.CAP_PROP_FRAME_COUNT))}")
    print(f"  FPS: {cap.get(cv2.CAP_PROP_FPS)}")
    print(f"  Width: {int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))}")
    print(f"  Height: {int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))}")
cap.release()

# Verify output video
cap = cv2.VideoCapture(output_video)
if not cap.isOpened():
    print(f"Error: Could not open output video file {output_video}")
else:
    print(f"Output video created successfully: {output_video}")
    print(f"Video properties:")
    print(f"  Frames: {int(cap.get(cv2.CAP_PROP_FRAME_COUNT))}")
    print(f"  FPS: {cap.get(cv2.CAP_PROP_FPS)}")
    print(f"  Width: {int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))}")
    print(f"  Height: {int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))}")
cap.release()