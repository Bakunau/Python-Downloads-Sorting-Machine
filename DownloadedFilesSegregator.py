import os
import shutil

class FileSegregator:
    def __init__(self, source_folder):
        self.source_folder = source_folder
        self.validate_folder(self.source_folder)

    @staticmethod
    def validate_folder(folder_path):
        """Ensure a folder exists and is accessible."""
        if not os.path.exists(folder_path):
            raise FileNotFoundError(f"Folder '{folder_path}' does not exist.")
        if not os.path.isdir(folder_path):
            raise NotADirectoryError(f"Path '{folder_path}' is not a directory.")

    def move_files(self, destination_folder, extensions):
        """Move files with specific extensions to the destination folder."""
        self.validate_folder(self.source_folder)
        os.makedirs(destination_folder, exist_ok=True)

        for entry in os.scandir(self.source_folder):
            if entry.is_file() and entry.name.endswith(extensions):
                try:
                    shutil.move(entry.path, os.path.join(destination_folder, entry.name))
                    print(f"Moved '{entry.name}' to '{destination_folder}'")
                except Exception as e:
                    print(f"Error moving '{entry.name}': {e}")

    def move_documents(self, destination_folder):
        self.move_files(destination_folder, (".txt", ".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".csv"))

    def move_programs(self, destination_folder):
        self.move_files(destination_folder, (".exe", ".msi", ".bat", ".sh"))

    def move_photos(self, destination_folder):
        self.move_files(destination_folder, (".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".raw"))

    def move_programming_docs(self, destination_folder):
        self.move_files(destination_folder, (".py", ".c", ".cpp", ".java", ".js", ".html", ".css", ".php", ".sql", ".json", ".xml"))

    def move_web_docs(self, destination_folder):
        self.move_files(destination_folder, (".html", ".htm", ".css", ".js", ".json", ".xml", ".php", ".asp", ".aspx", ".jsp"))

    def move_videos_and_tracks(self, destination_folder):
        self.move_files(destination_folder, (".mp3", ".mp4", ".avi", ".mov", ".flv", ".wmv", ".wav", ".m4a", ".ogg", ".flac"))

# Define source folder and destination folders
source_folder = r"C:\Users\user\Downloads"

docs_destination_folder = os.path.join(source_folder, "Documents")
programs_destination_folder = os.path.join(source_folder, "Programs")
photos_destination_folder = os.path.join(source_folder, "Photos")
programming_docs_destination_folder = os.path.join(source_folder, "Programming Documents")
web_docs_destination_folder = os.path.join(source_folder, "Web Documents")
videos_and_tracks_destination_folder = os.path.join(source_folder, "Videos and Songs")

# Instantiate the FileSegregator class
file_segregator = FileSegregator(source_folder)

# Move files to their respective folders
file_segregator.move_documents(docs_destination_folder)
file_segregator.move_programs(programs_destination_folder)
file_segregator.move_photos(photos_destination_folder)
file_segregator.move_programming_docs(programming_docs_destination_folder)
file_segregator.move_web_docs(web_docs_destination_folder)
file_segregator.move_videos_and_tracks(videos_and_tracks_destination_folder)


