import os
import shutil


folder_map = {
    ".pdf" : "PDFs",
    ".docx" : "Documents",
    ".txt" : "Text",
    ".jpg" : "Images",
    ".png" : "Images",
    ".jpeg" : "Images"
}

files = os.listdir("test_files")

for file in files: 

    name, extension = os.path.splitext(file)

    destination_folder = folder_map[extension]

    os.makedirs(destination_folder, exist_ok=True)
    
    source_path = os.path.join("test_files", file)

    destination_path = os.path.join(
        destination_folder,file
    )

    shutil.move(source_path, destination_path)

    