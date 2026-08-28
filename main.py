import os
import shutil
from datetime import datetime

# 1. Folders aur unke Extensions ka dynamic map
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".xls", ".pptx", ".csv"],
    "Music": [".mp3", ".wav", ".aac", ".flac"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Archives": [".zip", ".tar", ".gz", ".rar", ".7z"],
}


def log_message(message):
    """Activity ko terminal aur log file dono mein save karne ke liye"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {message}"
    print(message)  # Terminal pe dikhane ke liye
    with open("file_organizer.log", "a", encoding="utf-8") as log_file:
        log_file.write(log_entry + "\n")


def get_unique_path(target_folder, filename):
    """Agar file pehle se maujood ho, to unique naam generate karne ke liye"""
    name, ext = os.path.splitext(filename)
    counter = 1
    destination = os.path.join(target_folder, filename)

    while os.path.exists(destination):
        filename = f"{name}_{counter}{ext}"
        destination = os.path.join(target_folder, filename)
        counter += 1

    return destination


def organize_files(source_dir):
    log_message("--- File Organizer Started ---")

    if not os.path.exists(source_dir):
        log_message(f"Error: Source directory '{source_dir}' nahi mili.")
        return

    # Source directory ke andar saari files check karna
    for filename in os.listdir(source_dir):
        source_path = os.path.join(source_dir, filename)

        # Sirf files ko move karna hai, folders ko nahi
        if os.path.isfile(source_path):
            # log file aur main.py ko khud move hone se bachana
            if filename in ["main.py", "file_organizer.log"]:
                continue

            _, extension = os.path.splitext(filename)
            extension = extension.lower()

            # Sahi folder decide karna
            moved = False
            for folder_name, extensions in FILE_TYPES.items():
                if extension in extensions:
                    target_folder = os.path.join(source_dir, folder_name)
                    os.makedirs(target_folder, exist_ok=True)

                    # Duplicate check karke safe path lena
                    destination = get_unique_path(target_folder, filename)

                    try:
                        shutil.move(source_path, destination)
                        log_message(f"Moved: {filename} -> {folder_name}/")
                        moved = True
                    except Exception as e:
                        log_message(f"Error moving {filename}: {str(e)}")
                    break

            # Agar extension list mein nahi hai, to 'Others' folder mein daalna
            if not moved:
                target_folder = os.path.join(source_dir, "Others")
                os.makedirs(target_folder, exist_ok=True)
                destination = get_unique_path(target_folder, filename)
                try:
                    shutil.move(source_path, destination)
                    log_message(f"Moved (Unknown type): {filename} -> Others/")
                except Exception as e:
                    log_message(f"Error moving {filename}: {str(e)}")

    log_message("--- File Organizer Finished ---")


if __name__ == "__main__":
    # Aapka test-files folder path
    target_directory = "./test-files"
    organize_files(target_directory)
