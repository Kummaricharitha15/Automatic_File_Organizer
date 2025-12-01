# Automatic_File_Organizer
📂 Automatic File Organizer

Project Description

The Automatic File Organizer is a Python program that automatically organizes all files in a selected folder into categories such as Images, Videos, Documents, Music, Compressed files, and Others. It helps keep folders clean and structured without manual effort.

This project demonstrates Python file handling, directory management, and automation skills.


---

Features

Automatically detects all files in a folder.

Categorizes files into folders:

Images: .png, .jpg, .jpeg

Videos: .mp4, .mkv

Documents: .pdf, .docx, .txt

Music: .mp3

Compressed: .zip, .rar

Others: Any other file types.


Creates folders automatically if they don’t exist.

Moves files into corresponding folders.

Easy to extend with more file types.



---

How It Works

1. The user sets the folder path in the path variable.


2. The program scans all files in that folder.


3. It checks the file extension and moves the file into the corresponding category folder.


4. Files without a matching category are moved to the Others folder.


5. After running, the folder is neatly organized.




---

Installation

1. Install Python 3.x from Python.org


2. Create a folder for the project and open VS Code.


3. Create a new file organizer.py and paste the code.


4. Change the path variable to the folder you want to organize.


5. Run the code in VS Code.




---

Usage

1. Open the Python file in VS Code.


2. Update the folder path:



path = "C:/Users/YourName/Downloads"

3. Run the program (F5 or ▶ Run).


4. After execution, check your folder — files are now organized into subfolders.




---

Example

Before running:

Downloads/
    photo.png
    song.mp3
    resume.pdf
    movie.mp4
    notes.txt

After running:

Downloads/
    Images/
        photo.png
    Music/
        song.mp3
    Documents/
        resume.pdf
        notes.txt
    Videos/
        movie.mp4
    Others/


---

Technologies Used

Python 3.x

os module (for file and directory operations)

shutil module (for moving files)



---

Future Improvements

Ask the user to input the folder path instead of editing code.

Organize files by date or size.

Create a GUI version using Tkinter.

Add logging to keep track of moved files.



---

Conclusion

This project is a simple but practical automation tool that helps keep any folder neat and organized, and demonstrates Python programming and file management skills.


---
