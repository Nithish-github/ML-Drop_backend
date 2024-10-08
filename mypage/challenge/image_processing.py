# image_processing.py
import base64
import cv2
import numpy as np
import torch
model = torch.hub.load("ultralytics/yolov5", "yolov5s")  # or yolov5n - yolov5x6, custom


def apply_filter(image_base64, filter_type):
    # Decode the base64 image
    image_data = base64.b64decode(image_base64)
    np_image = np.frombuffer(image_data, np.uint8)
    image = cv2.imdecode(np_image, cv2.IMREAD_COLOR)

    # Apply the specified filter
    if filter_type == 'gray':
        processed_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    elif filter_type == 'blur':
        processed_image = cv2.GaussianBlur(image, (5, 5), 0)
    elif filter_type =='object_detection':
        results = model(image)
        r_img = results.render() # returns a list with the images as np.array
        processed_image = r_img[0] # image with boxes as np.array

    elif filter_type =='web_cam':

        cap = cv2.VideoCapture(0)

        # Check if the webcam is opened successfully
        if not cap.isOpened():
            print("Error: Could not open webcam.")
            exit()

        ret, processed_image = cap.read()

        cap.release()

    else:
        raise ValueError("Invalid filter type provided.")

    # Encode the processed image back to base64
    _, buffer = cv2.imencode('.jpg', processed_image)
    processed_image_base64 = base64.b64encode(buffer).decode('utf-8')

    return processed_image_base64



