from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import tkinter as tk
from tkinter import filedialog
import cv2
import numpy as np
import os

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
    print(red_pixels)

    # Print the detection result
    if red_pixels > 300:
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
    print(green_pixels)

    if green_pixels > 300:
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
    print(blue_pixels)

    if blue_pixels > 300:
        return True
    else:
        return False
    
def Upload_to_math(file_path):

    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)

    with open(file_path, 'r') as file:  # Modified
          fn = os.path.basename(file.name)
          file_drive = drive.CreateFile({"title": fn,
                                         "parents": [{"id":"161XQrWs_-g53GssAxdDWA2V8583nVJrB"}]
                                         
                                         
                                         
                                          })
    file_drive.SetContentFile(file_path)  # Added
    

    
    
    file_drive.Upload()
    print("File uploaded successfully")
    
    


def Upload_to_science(file_path):

    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)

    with open(file_path, 'r') as file:  # Modified
          fn = os.path.basename(file.name)
          file_drive = drive.CreateFile({"title": fn,
                                         "parents": [{"id":"1osjz7-wD2PLR88YY8ZurtOvo3qh0Y8ar"}]
                                         
                                         
                                         
                                          })
    file_drive.SetContentFile(file_path)  # Added
    

    
    
    file_drive.Upload()
    print("File uploaded successfully")


def Upload_to_english(file_path):

    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)

    with open(file_path, 'r') as file:  # Modified
          fn = os.path.basename(file.name)
          file_drive = drive.CreateFile({"title": fn,
                                         "parents": [{"id":"1TdMTCkkf75zcccwf31kG5qBOKegTDGvC"}]
                                         
                                         
                                         
                                          })
    file_drive.SetContentFile(file_path)  # Added
    

    
    
    file_drive.Upload()
    print("File uploaded successfully")
    



def upload_file():
    global selected_file
    
    file_path = filedialog.askopenfilename(title="Select a file")
    if file_path:
        selected_file = file_path
        root.quit()

    
        # You can store the file_path in a variable or perform other actions with it.

# Create the main window
root = tk.Tk()
root.title("Drive Upload")

# Welcome message label
welcome_label = tk.Label(root, text="Welcome to Drive Upload (notes)",font=("Arial",25))
welcome_label.pack(pady=50)

# Upload button
upload_button = tk.Button(root, text="Upload", command=upload_file,font=("Arial",40))
upload_button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()


if detect_blue(selected_file):
    print("English")
    Upload_to_english(selected_file)
elif detect_green(selected_file):
    print("Science")
    Upload_to_science(selected_file)
elif detect_red(selected_file):
    print("Math")
    Upload_to_math(selected_file)


root = tk.Tk()
root.title("Successfull")
success_label = tk.Label(root, text="Sucessfully Uploaded",font=("Arial",25))
success_label.pack(pady=50)

root.mainloop()







