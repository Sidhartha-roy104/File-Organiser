# File Organiser (FAST AND ROBUST)

File Organiser is a simple and fast Python script that cleans up messy folders by sorting files into clear, meaningful directories based on their file type.  
It is designed to be practical, predictable, and safe — no AI, no internet, and no background services.

If you have a folder full of mixed PDFs, documents, images, code files, and downloads, this tool helps you organize it in one run.

---

## What this script does

The script scans a folder you choose and:
- Identifies each file by its extension
- Creates folders only when they are needed
- Moves files into the correct folders
- Generates a summary file explaining what was done

Everything happens locally and finishes very quickly, even for large folders.

---

## Folder structure created

Depending on the files present, the script may create folders such as:

Code  
PDFs  
Text_Files  
Word_Documents  
Excel_Sheets  
PowerPoint  
Markdown  
Images  
Videos  
Audio  
Archives  
Executables  
Data  
Fonts  
Configs  
Logs  
Others  

Each file is placed in the folder that best matches its type.

---

## Example summary output

After the script runs, a `summary.txt` file is created in the project directory.  
It looks similar to this:

SUMMARY REPORT  
Execution time: 2025-01-01 14:32:10  
Total files processed: 37  

Folder breakdown:  
Code: 12  
PDFs: 4  
Word_Documents: 6  
Excel_Sheets: 3  
PowerPoint: 2  
Images: 7  
Others: 3  

File movements:  
report.pdf -> PDFs/  
notes.txt -> Text_Files/  
data.xlsx -> Excel_Sheets/  
slides.pptx -> PowerPoint/  
main.py -> Code/  

This makes it easy to see exactly what happened.

---

## How to run

Requirements:
- Python 3.8 or higher
- Works on Windows, macOS, and Linux
- No external libraries required

Steps:
1. Clone the repository
2. Run the script using `python agent.py`
3. Enter the path to the folder you want to organize

The folder will be cleaned and organized immediately.

---

## Performance

The script uses simple rule-based logic, so it is very fast.

100 files: less than a second  
1,000 files: a fraction of a second  
7,000 files: under one second  
Large folders with tens of thousands of files are also handled smoothly.

---

## Safety and behavior

- Files are only moved, never modified or deleted
- Existing folders are not changed
- Safe to stop with Ctrl+C
- Fully offline and deterministic

---

## Common use cases

Cleaning the Downloads folder  
Organizing college or office documents  
Sorting project resources  
General desktop cleanup  

---

## License

This project is free to use for learning, personal projects, and everyday productivity.  
If you find it useful, feel free to star the repository.
