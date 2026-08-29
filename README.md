# 📁 Business File Organizer Automation

A smart, automated Python script designed to clean up messy directories by instantly sorting files into dedicated, organized folders based on their file extensions. Built to optimize professional workflows, reduce clutter, and save time.

`⚡ Runtime: Python 3.x` | `🛠️ Stack: Standard OS & Shutil` | `📄 License: MIT`


## 🚀 Key Features
* **Dynamic File Categorization:** Automatically maps and routes files like Images, Documents, Videos, Music, and Archives into structured folders.
* **Smart Duplicate Handling:** Appends incremental counters (e.g., photo_1.jpg) to filenames if a file with the same name already exists in the target folder, preventing accidental overwrites.
* **Activity Logging System:** Generates a real-time `file_organizer.log` file tracking execution time, successfully moved files, and errors.
* **Robust Error Handling:** Safely handles locked or busy files without crashing the entire automation process.

## 📊 How It Works
### Before Automation (Messy Folder)
```text
test-files/
├── photo.jpg
├── report.pdf
├── data.xlsx
├── song.mp3
├── random.zip
└── movie.mp4
```

### After Automation (Organized Structure)
```text
test-files/
├── Documents/
│   ├── report.pdf
│   └── data.xlsx
├── Images/
│   └── photo.jpg
├── Music/
│   └── song.mp3
├── Videos/
│   └── movie.mp4
└── Archives/
    └── random.zip
```

## ⚙️ Configuration & Customization
By default, the script scans the current directory where it is executed. If you want to customize target extensions or folder names, open `main.py` and modify the category dictionary:

```python
DIRECTORIES = {
    "HTML": [".html", ".htm"],
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".xlsx", ".txt"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".tar", ".rar"]
}
```

## 📋 Prerequisites
* **Python 3.x** installed on your system.
* No external libraries are required (Built entirely using Python's standard `os`, `shutil`, and `datetime` modules).

## 💻 Quick Start & Setup
1. **Clone the repository:**
   ```bash
   git clone https://github.com.git
   ```
2. **Navigate into the folder:**
   ```bash
   cd file-organizer
   ```
3. **Run the script:**
   ```bash
   python main.py
   ```
4. **Check the logs:** Open `file_organizer.log` to view the operation history.

## 🤝 Contributing
Contributions are welcome! If you want to add support for more file extensions or implement a GUI:
1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License
Distributed under the **MIT License**. See `LICENSE` for more information.
