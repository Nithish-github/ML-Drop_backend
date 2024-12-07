def generate_code(tasks):
    code = "import cv2\nimport numpy as np\n\n"

    if 'input' in tasks:
        code += "# Load the input image\n"
        code += "image = cv2.imread('input_image.jpg')\n"
        code += "if image is None:\n"
        code += "    print('Error: Image not found!')\n"
        code += "    exit()\n\n"
    
    if 'threshold' in tasks:
        code += "# Convert the image to grayscale and apply thresholding\n"
        code += "gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)\n"
        code += "_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)\n\n"
    
    if 'findcontours' in tasks:
        code += "# Find contours in the thresholded image\n"
        code += "contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)\n\n"

    if 'display' in tasks:
        code += "# Draw contours and display the result\n"
        code += "cv2.drawContours(image, contours, -1, (0, 255, 0), 2)\n"
        code += "cv2.imshow('Contours', image)\n"
        code += "cv2.waitKey(0)\n"
        code += "cv2.destroyAllWindows()\n"

    return code


if __name__ == "__main__":
    # Example usage
    tasks = ['input', 'threshold', 'findcontours', 'display']
    generated_code = generate_code(tasks)
    print(generated_code)

