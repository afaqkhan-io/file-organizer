# 📁 Business File Organizer Automation

A lightweight Python automation script that organizes files into folders based on their extensions. It is designed as a simple example of practical desktop file automation.

`Python 3.x` · `Standard Library` · `MIT License`

## 🚀 Features

- **Automatic categorization:** Sorts common images, documents, videos, music, and archive files.
- **Duplicate handling:** Adds an incrementing suffix when a target filename already exists.
- **Activity logging:** Records successful moves and errors in `file_organizer.log`.
- **Error handling:** Continues processing when an individual file cannot be moved.

## 📊 Example

Before:

```text
test-files/
├── photo.jpg
├── report.pdf
├── data.xlsx
├── song.mp3
├── random.zip
└── movie.mp4
```

After:

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

## ⚙️ Customization

Edit the category dictionary in `main.py` to add or remove supported extensions and destination folders.

## 📋 Requirements

- Python 3.x
- No third-party packages are required.

## 💻 Setup & Usage

```bash
git clone https://github.com/afaqkhan-io/file-organizer.git
cd file-organizer
python main.py
```

> **Important:** Run the script on a test directory first. The program moves files and can change the directory structure of the folder it scans.

## 📄 License

Distributed under the **MIT License**. See `LICENSE` for details.
