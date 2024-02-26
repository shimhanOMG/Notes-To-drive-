from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os


def Upload_to_math(file_path):

    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)


    with open(file_path, 'r') as file:  # Modified
          fn = os.path.basename(file.name)
          file_drive = drive.CreateFile({"title": fn })
    file_drive.SetContentFile(file_path)  # Added
    

    '''file_drive = drive.CreateFile({
        "title":file_path.split("/")[-1],
        "parents": [{"id":"161XQrWs_-g53GssAxdDWA2V8583nVJrB"}],
        
        }
    )'''
    
    file_drive.Upload()
    print("File uploaded successfully")


Upload_to_math("end.png")