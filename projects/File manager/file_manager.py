import os
import shutil

images = [".jpg", ".png", ".jpeg"]
documents = [".pdf", ".txt"]
videos = [".mp4"]

contents = os.listdir()

for file in contents:
    extensions = os.path.splitext(file)
    if os.path.isfile(file):
        if extensions[1] in images:
            os.makedirs("Images", exist_ok=True)
            destination = "/Users/karam/Coding/AI Engineer/projects/File manager/test/Images"
            shutil.move(file, destination)
            print(f"{file} has been moved")

        elif extensions[1] in documents:
            os.makedirs("Documents", exist_ok=True)
            destination = "/Users/karam/Coding/AI Engineer/projects/File manager/test/Documents"
            shutil.move(file, destination)
            print(f"{file} has been moved")

        elif extensions[1] in videos:
            os.makedirs("Videos", exist_ok=True)
            destination = "/Users/karam/Coding/AI Engineer/projects/File manager/test/Videos"
            shutil.move(file, destination)
            print(f"{file} has been moved")
        
        else:
            print(f"{file} has an invlaid format")

    
