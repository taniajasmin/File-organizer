## File Organizer
A simple Python script to automatically organize messy folders by sorting files into categories based on their type.


### 🌟 Features
- One-click organization for any folder on your computer
- Smart categorization of files into intuitive folders (Images, Documents, Software, etc.)
- Duplicate file handling to ensure nothing gets overwritten
- Simple interface that anyone can use
- Works across platforms (Windows, Mac, Linux)


### 📋 How It Works
The File Organizer scans your selected folder and automatically sorts files by type:

- 📸 Images: jpg, png, gif, etc.
- 📄 Documents: pdf, docx, txt, etc.
- 📊 Spreadsheets: xlsx, csv, etc.
- 📱 Software: exe, msi, app, etc.
- 🎵 Music: mp3, wav, flac, etc.
- 🎬 Videos: mp4, mov, avi, etc.
- 💻 Code: py, js, html, etc.
...and many more!


### 🚀 Usage
1. Run the script: python file_organizer.py
2. Enter the folder path you want to organize (or use a shortcut like "downloads")
3. Review the folder details and confirm
4. Watch as your files get neatly sorted!

``` 🗂️ Desktop File Organizer Pro
==================================================

📁 Enter the folder path to organize: C:\Users\YourName\Downloads

🎯 Selected folder: C:\Users\YourName\Downloads
📊 Contains 143 files

Proceed with organization? (yes/no): yes

🔄 Organizing files...
```


✨ Example Results
Before:
```
Downloads/
├── presentation.pptx
├── vacation.jpg
├── resume.pdf
├── setup.exe
├── notes.txt
└── ... (dozens more random files)
```
After:
```
Downloads/
├── Documents/
│   ├── resume.pdf
│   └── notes.txt
├── Images/
│   └── vacation.jpg
├── Presentations/
│   └── presentation.pptx
├── Software/
│   └── setup.exe
└── ... (other category folders)
```


### 💡 Why I Built This
I was tired of having a messy downloads folder with hundreds of files. This simple script has saved me hours of manual organization and helps me find files quickly when I need them.

### 🔧 Requirements
- Python 3.6 or higher
- No external libraries needed (uses only standard library)

### 📝 License
MIT License - feel free to use and modify!

==================================================

**Made with ❤️ to end download folder chaos**
