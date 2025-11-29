import datetime
from pathlib import Path
import os
import shutil


def iterate_downloads_folder(log_file):
    """
    Iterate through the Downloads folder and log information about files and directories.
    
    Args:
        log_file: File object to write log entries to
    """
    # Get the Downloads folder path
    downloads_folder = Path.home() / "Downloads"
    
    log_file.write(f"Scanning Downloads folder: {downloads_folder}\n")
    
    # Iterate through all files in the Downloads folder
    if downloads_folder.exists():
        items = list(downloads_folder.iterdir())
        log_file.write(f"Found {len(items)} items in Downloads folder\n")
        
        for item in items:
            if item.is_file():
                HandleFile(log_file, item)
            elif item.is_dir():
                log_file.write(f"  Directory: {item.name}\n")
    else:
        log_file.write(f"Downloads folder not found at: {downloads_folder}\n")

def move_file_to_folder(item, folder_name):
    destination_folder = Path.home() / "Downloads" / folder_name
    destination_path = destination_folder / item.name
    
    os.makedirs(destination_folder, exist_ok=True)
    
    # If destination file exists, remove it to overwrite
    if destination_path.exists():
        if destination_path.is_file():
            os.remove(destination_path)
        elif destination_path.is_dir():
            shutil.rmtree(destination_path)
    
    # Move the file to the destination folder
    shutil.move(str(item), str(destination_path))


def HandleFile(log_file, item):
    file_size = item.stat().st_size
    file_modified = datetime.datetime.fromtimestamp(item.stat().st_mtime)
    log_file.write(f"  File: {item.name} ({file_size} bytes, modified: {file_modified})\n")

    if(item.suffix == ".jpg" or item.suffix == ".jpeg" or item.suffix == ".png" or item.suffix == ".gif" or item.suffix == ".bmp" or item.suffix == ".tiff" or item.suffix == ".ico" or item.suffix == ".webp"):
        move_file_to_folder(item, "images")
    elif(item.suffix == ".mp4" or item.suffix == ".avi" or item.suffix == ".mov" or item.suffix == ".wmv" or item.suffix == ".flv" or item.suffix == ".mkv"):
        move_file_to_folder(item, "videos")
    elif(item.suffix == ".mp3" or item.suffix == ".wav" or item.suffix == ".ogg" or item.suffix == ".aac" or item.suffix == ".m4a" or item.suffix == ".flac"):
        move_file_to_folder(item, "audio")
    elif(item.suffix == ".exe" or item.suffix == ".msi" or item.suffix == ".dmg" or item.suffix == ".pkg" or item.suffix == ".deb" or item.suffix == ".rpm" or item.suffix == ".tar" or item.suffix == ".zip" or item.suffix == ".7z" or item.suffix == ".rar" or item.suffix == ".gz" or item.suffix == ".bz2" or item.suffix == ".xz"):
        move_file_to_folder(item, "installers")
    elif(item.suffix == ".pdf" or item.suffix == ".doc" or item.suffix == ".docx" or item.suffix == ".txt" or item.suffix == ".rtf" or item.suffix == ".odt" or item.suffix == ".html" or item.suffix == ".css" or item.suffix == ".js" or item.suffix == ".php" or item.suffix == ".py" or item.suffix == ".java" or item.suffix == ".cpp" or item.suffix == ".h" or item.suffix == ".hpp" or item.suffix == ".c" or item.suffix == ".cc" or item.suffix == ".hpp" or item.suffix == ".hxx"):
       move_file_to_folder(item, "documents")
    else:
        move_file_to_folder(item, "other")



if __name__ == "__main__":
    # Place the logic you want the Windows Task Scheduler to execute here.
    # For example, writing a simple message to a log file:

    # Log the task execution
    with open("task_scheduler_log.txt", "a") as log_file:
        log_file.write(f"Task executed at {datetime.datetime.now()}\n")
        iterate_downloads_folder(log_file)
