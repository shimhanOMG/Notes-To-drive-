import cv2
import numpy as np


def detect_red(image_path):
    """
    Detects the presence of red color in an image and prints a message accordingly.

    Args:
        image_path (str): Path to the image file.

    Returns:
        None
    """

    # Load the image and convert it to HSV color space for better color detection
    img = cv2.imread(image_path)
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Define the lower and upper bounds of the red color range in HSV (Hue, Saturation, Value)
    lower_red = np.array([0, 50, 50], dtype=np.uint8)  # Adjust values if necessary
    upper_red = np.array([10, 255, 255], dtype=np.uint8)  # Adjust values if necessary

    # Create a mask using the defined color range
    mask = cv2.inRange(hsv_img, lower_red, upper_red)

    # Count the non-zero pixels in the mask to determine if red is present
    red_pixels = cv2.countNonZero(mask)

    # Print the detection result
    if red_pixels > 500:
        return True
    else:
        return False
    


def detect_green(image_path ):

    img = cv2.imread(image_path)
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower_green = np.array([40, 50, 50], dtype=np.uint8)  # Adjust values if necessary
    upper_green = np.array([80, 255, 255], dtype=np.uint8)  # Adjust values if necessary
    mask = cv2.inRange(hsv_img, lower_green, upper_green)

    green_pixels = cv2.countNonZero(mask)

    if green_pixels > 500:
        return True
    else:
        return False
    
def detect_blue(image_path):
    img = cv2.imread(image_path)
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower_blue = np.array([100, 50, 50], dtype=np.uint8)  # Adjust values if necessary
    upper_blue = np.array([140, 255, 255], dtype=np.uint8)  # Adjust values if necessary
    mask = cv2.inRange(hsv_img, lower_blue, upper_blue)

    blue_pixels = cv2.countNonZero(mask)

    if blue_pixels > 300:
        return True
    else:
        return False
    





