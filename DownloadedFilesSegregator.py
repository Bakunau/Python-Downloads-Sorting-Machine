import os
import shutil

class FileSegregator:
    def __init__(self, source_folder):
        self.source_folder = source_folder

    def move_files(self, destination_folder, extensions):
        # List all files in the source folder
        files = os.listdir(self.source_folder)

        # Iterate through each file
        for file_name in files:
            # Check if the file ends with any of the specified extensions
            if file_name.endswith(extensions):
                # Create the destination folder if it doesn't exist
                os.makedirs(destination_folder, exist_ok=True)

                # Move the file to the destination folder
                source_path = os.path.join(self.source_folder, file_name)
                destination_path = os.path.join(destination_folder, file_name)
                shutil.move(source_path, destination_path)

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

# Define destination folders
docs_destination_folder = r"C:\Users\user\Downloads\Documents"
programs_destination_folder = r"C:\Users\user\Downloads\Programs"
photos_destination_folder = r"C:\Users\user\Downloads\Photos"
programming_docs_destination_folder = r"C:\Users\user\Downloads\Programming Documents"
web_docs_destination_folder = r"C:\Users\user\Downloads\Web Documents"
videos_and_tracks_destination_folder = r"C:\Users\user\Downloads\Videos and Songs"

# Define source folder
source_folder = r"C:\Users\user\Downloads"

# Instantiate the FileSegregator class
file_segregator = FileSegregator(source_folder)

# Move documents to the destination folder
file_segregator.move_documents(docs_destination_folder)

# Move programs to the destination folder
file_segregator.move_programs(programs_destination_folder)

# Move photos to the destination folder
file_segregator.move_photos(photos_destination_folder)

# Move programming documents to the destination folder
file_segregator.move_programming_docs(programming_docs_destination_folder)

# Move web documents to the destination folder
file_segregator.move_web_docs(web_docs_destination_folder)

# Move videos and songs to the destination folder
file_segregator.move_videos_and_tracks(videos_and_tracks_destination_folder)

