
import os
import shutil

def organize_files(folder):
    categories = {
        "Images": [".jpg", ".jpeg", ".png"],
        "Documents": [".pdf", ".doc", ".docx", ".txt"],
        "Videos": [".mp4", ".mkv", ".avi"],
        "Audio": [".mp3", ".wav"],
        "Code": [".py", ".c", ".cpp"],
    }

    for filename in os.listdir(folder):
        source = os.path.join(folder, filename)

        if not os.path.isfile(source):
            continue

        extension = os.path.splitext(filename)[1].lower()
        category = "Others"

        for name, extensions in categories.items():
            if extension in extensions:
                category = name
                break

        destination_folder = os.path.join(folder, category)
        os.makedirs(destination_folder, exist_ok=True)

        destination = os.path.join(destination_folder, filename)

        if os.path.exists(destination):
            print("Skipped duplicate:", filename)
            continue

        shutil.move(source, destination)
        print("Moved:", filename, "to", category)

    print("File organization completed!")

if __name__ == "__main__":
    folder = input("Enter folder path: ").strip()
    if os.path.isdir(folder):
        organize_files(folder)
    else:
        print("Invalid folder path.")
