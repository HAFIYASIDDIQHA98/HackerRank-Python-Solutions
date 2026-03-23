import os
import shutil

def organize_folder(target_dir):
    # Extensions ka map banayein
    extensions = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Documents': ['.pdf', '.docx', '.txt', '.xlsx'],
        'Videos': ['.mp4', '.mkv'],
        'Archives': ['.zip', '.rar']
    }

    for filename in os.listdir(target_dir):
        filepath = os.path.join(target_dir, filename)
        
        # Folder ko skip karein, sirf files check karein
        if os.path.isdir(filepath):
            continue

        # Extension check karein
        file_ext = os.path.splitext(filename)[1].lower()
        
        for folder, exts in extensions.items():
            if file_ext in exts:
                dest_path = os.path.join(target_dir, folder)
                os.makedirs(dest_path, exist_ok=True)
                shutil.move(filepath, os.path.join(dest_path, filename))
                print(f"Moved: {filename} -> {folder}")

if __name__ == "__main__":
    path = input("Enter the full path of the folder to organize: ")
    organize_folder(path)
