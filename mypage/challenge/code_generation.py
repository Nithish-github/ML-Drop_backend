import base64
import cv2
import numpy as np
# import torch

# # Load the YOLOv5 model
# model = torch.hub.load("ultralytics/yolov5", "yolov5s")  # or yolov5n - yolov5x6, custom


def apply_filter(image_base64, filter_type, **kwargs):
    """
    Apply filters to the image.
    
    :param image_base64: base64 encoded image
    :param filter_type: type of filter to apply ('gray', 'blur', 'object_detection', etc.)
    :param kwargs: additional arguments for filters like kernel size for blur, contrast factor, etc.
    :return: base64 encoded processed image
    """
    # Decode the base64 image
    image_data = base64.b64decode(image_base64)
    np_image = np.frombuffer(image_data, np.uint8)
    image = cv2.imdecode(np_image, cv2.IMREAD_COLOR)

    # Apply the specified filter
    if filter_type == 'gray':
        processed_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    elif filter_type == 'blur':
        # Get the kernel size from kwargs (default is 5)
        ksize = kwargs.get('ksize', 5)
        processed_image = cv2.GaussianBlur(image, (ksize, ksize), 0)

    elif filter_type == 'sharpen':
        kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])  # Sharpening kernel
        processed_image = cv2.filter2D(image, -1, kernel)

    elif filter_type == 'edge_detection':
        processed_image = cv2.Canny(image, 100, 200)  # Edge detection using Canny

    elif filter_type == 'brightness_contrast':
        # Adjust brightness and contrast using alpha and beta from kwargs
        alpha = kwargs.get('alpha', 1.2)  # Contrast factor (1.0 leaves contrast unchanged)
        beta = kwargs.get('beta', 50)  # Brightness (0 leaves brightness unchanged)
        processed_image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

    elif filter_type == 'resize':
        # Resize to a specific width and height
        width = kwargs.get('width', image.shape[1])  # Default is the original width
        height = kwargs.get('height', image.shape[0])  # Default is the original height
        processed_image = cv2.resize(image, (width, height))

    # elif filter_type == 'object_detection':
    #     results = model(image)
    #     r_img = results.render()  # Returns a list with the images as np.array
    #     processed_image = r_img[0]  # Image with boxes as np.array

    elif filter_type == 'web_cam':
        cap = cv2.VideoCapture(0)
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
