


import tkinter as tk
from tkinter import filedialog

def upload_file():
    global selected_file
    
    file_path = filedialog.askopenfilename(title="Select a file")
    if file_path:
        selected_file = file_path

    
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

print(selected_file)''''''
