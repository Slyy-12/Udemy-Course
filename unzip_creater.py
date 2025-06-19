import zipfile
import pathlib

def extract_archive(archivepath, dest_dir):
    with zipfile.ZipFile(archivepath, 'r') as archive:
        for filepath in archivepath:
            archive.extractall(dest_dir)

if __name__ == "__main__":
    extract_archive(filepaths=["e1.py", "e2.py"], dest_dir="dest")