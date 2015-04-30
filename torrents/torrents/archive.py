import zipfile
import os

class Archive:

    def __init__(self, path):
        self.path = path

    def write_directory(self, zipf, dir):
        for root, dirs, files in os.walk(dir):
            for file in files:
                zipf.write(os.path.join(root, file))
    
    def zip(self, data_dir):
        with zipfile.ZipFile(self.path, 'w') as zipf:
            self.write_directory(zipf, data_dir)
