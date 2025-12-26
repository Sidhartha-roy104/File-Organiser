import os
import shutil
from datetime import datetime

# ==================================================
# EXTENSION → FOLDER MAP (DETAILED)
# ==================================================

EXTENSION_MAP = {
    # Code
    "Code": [
        ".py", ".java", ".js", ".c", ".cpp", ".cs",
        ".ts", ".go", ".rs", ".php", ".rb", ".sh"
    ],

    # Documents (SEPARATED)
    "PDFs": [".pdf"],
    "Text_Files": [".txt"],
    "Word_Documents": [".doc", ".docx"],
    "Excel_Sheets": [".xls", ".xlsx"],
    "PowerPoint": [".ppt", ".pptx"],
    "Markdown": [".md"],

    # Media
    "Images": [
        ".png", ".jpg", ".jpeg", ".gif", ".svg",
        ".webp", ".bmp", ".tiff", ".ico"
    ],
    "Videos": [
        ".mp4", ".mkv", ".avi", ".mov", ".webm"
    ],
    "Audio": [
        ".mp3", ".wav", ".aac", ".flac", ".ogg"
    ],

    # Other types
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Executables": [".exe", ".msi", ".bat", ".cmd"],
    "Data": [".csv", ".json", ".xml", ".yaml", ".yml", ".sql"],
    "Fonts": [".ttf", ".otf", ".woff", ".woff2"],
    "Configs": [".env", ".ini", ".cfg", ".conf", ".toml"],
    "Logs": [".log"]
}

DEFAULT_FOLDER = "Others"

# ==================================================
# FAST LOOKUP TABLE
# ==================================================

EXT_LOOKUP = {}
for folder, extensions in EXTENSION_MAP.items():
    for ext in extensions:
        EXT_LOOKUP[ext] = folder

# ==================================================
# FILE OPERATIONS
# ==================================================

def list_files(folder):
    return [
        f for f in os.listdir(folder)
        if os.path.isfile(os.path.join(folder, f))
    ]

def ensure_folder(path):
    os.makedirs(path, exist_ok=True)

def move_file(src, dst):
    shutil.move(src, dst)

# ==================================================
# CLASSIFIER
# ==================================================

def classify_file(filename):
    ext = os.path.splitext(filename)[1].lower()
    return EXT_LOOKUP.get(ext, DEFAULT_FOLDER)

# ==================================================
# MAIN
# ==================================================

def main():
    folder = input("Enter path to folder: ").strip()

    if not os.path.isdir(folder):
        print("❌ Invalid folder path")
        return

    files = list_files(folder)

    if not files:
        print("⚠️ Folder is empty")
        return

    print(f"📊 Total files found: {len(files)}")

    summary = {}
    folder_count = {}

    for file in files:
        category = classify_file(file)
        summary[file] = category
        folder_count[category] = folder_count.get(category, 0) + 1

        target_dir = os.path.join(folder, category)
        ensure_folder(target_dir)

        src = os.path.join(folder, file)
        dst = os.path.join(target_dir, file)

        move_file(src, dst)

    # ==================================================
    # WRITE SUMMARY REPORT
    # ==================================================

    with open("summary.txt", "w", encoding="utf-8") as f:
        f.write("SUMMARY REPORT\n")
        f.write("==============\n\n")
        f.write(f"Execution time: {datetime.now()}\n")
        f.write(f"Total files processed: {len(files)}\n\n")

        f.write("Folder breakdown:\n")
        for folder_name, count in sorted(folder_count.items()):
            f.write(f"  {folder_name}: {count}\n")

        f.write("\nFile movements:\n")
        for file, category in summary.items():
            f.write(f"  {file} -> {category}/\n")

    print("✅ DONE — Files organized & summary generated")

# ==================================================
# ENTRY
# ==================================================

if __name__ == "__main__":
    main()
