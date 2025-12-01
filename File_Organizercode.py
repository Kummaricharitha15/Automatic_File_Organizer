import os
import shutil

# 👉 CHANGE THIS to the folder you want to organize
path = "C:/Users/YourName/Downloads"

# File categories
file_types = {
    "Images": [".png", ".jpg", ".jpeg"],
    "Videos": [".mp4", ".mkv"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Music": [".mp3"],
    "Compressed": [".zip", ".rar"],
}

# Organizing files
for file in os.listdir(path):
    file_path = os.path.join(path, file)

    if os.path.isfile(file_path):
        ext = os.path.splitext(file)[1].lower()

        moved = False
        for folder, extensions in file_types.items():
            if ext in extensions:
                folder_path = os.path.join(path, folder)
                os.makedirs(folder_path, exist_ok=True)
                shutil.move(file_path, folder_path)
                moved = True
                break

        if not moved:
            others = os.path.join(path, "Others")
            os.makedirs(others, exist_ok=True)
            shutil.move(file_path, others)

print("Files organized successfully!")
