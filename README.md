# File Organizer

A Python automation tool that organizes files into categorized folders based on their file extensions.

## Features

* Automatically scans files from a target folder
* Detects file types using extensions
* Creates destination folders automatically
* Moves files into categorized folders
* Supports:

  * PDF files (`.pdf`)
  * Word documents (`.docx`)
  * Text files (`.txt`)
  * Images (`.jpg`, `.jpeg`, `.png`)

## Project Structure

```text
File-Organizer/
│
├── main.py
├── test_files/
├── PDFs/
├── Documents/
├── Images/
└── Text/
```

## How It Works

1. Reads all files from the `test_files` directory.
2. Identifies each file's extension.
3. Maps the extension to a destination folder.
4. Creates the folder if it does not already exist.
5. Moves the file into the appropriate folder.

## Example

### Before

```text
test_files/
│
├── resume.pdf
├── notes.txt
├── photo.jpeg
├── report.docx
```

### After

```text
PDFs/
└── resume.pdf

Text/
└── notes.txt

Images/
└── photo.jpeg

Documents/
└── report.docx
```

## Technologies Used

* Python 3
* os module
* shutil module

## Future Improvements

* Support additional file types (`.csv`, `.xlsx`, `.mp3`, `.mp4`)
* Recursive folder organization
* GUI using Tkinter
* Streamlit web application
* Automatic Downloads folder organization

## Author

Suraj Gupta
