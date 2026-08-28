# 📁 Business File Organizer Automation

A smart, automated Python script designed to clean up messy directories by instantly sorting files into dedicated, organized folders based on their file extensions. Built to optimize professional workflows, reduce clutter, and save time.

## 🚀 Key Features

- **Dynamic File Categorization:** Automatically maps and routes files like Images, Documents, Videos, Music, and Archives into structured folders.
- **Smart Duplicate Handling:** Appends incremental counters (e.g., `photo_1.jpg`) to filenames if a file with the same name already exists in the target folder, preventing accidental overwrites.
- **Activity Logging System:** Generates a real-time `file_organizer.log` file tracking execution time, successfully moved files, and errors.
- **Robust Error Handling:** Safely handles locked or busy files without crashing the entire automation process.

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

## 🛠️ Tech Stack & Modules

- **Language:** Python 3.x
- **Core Modules:** 
  - `os` (Directory traversal and path manipulation)
  - `shutil` (High-level safe file operations)
  - `datetime` (Precise log timestamping)

## 💻 Quick Start & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   ```
2. **Navigate into the folder:**
   ```bash
   cd file-organizer
   ```
3. **Run the script:**
   ```bash
   python main.py
   ```
4. **Check the logs:**
   Open `file_organizer.log` to view the operation history.
