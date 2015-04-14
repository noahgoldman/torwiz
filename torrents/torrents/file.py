import urllib

import os

OUTPUT_DIR = 'torrent_files'

"""
A class to handle downloading torrent files locally and managing their contents
"""
class TorrentFile:

    def __init__(self, id):
        self.id = id

    def get_output_file(self):
        return os.path.join(OUTPUT_DIR, str(self.id) + '.torrent')

    def get_from_url(self, url):
        urlopener = urllib.URLopener()
        urlopener.retrieve(url, self.get_output_file()) 

    def get_data(self):
        return open(self.get_output_file(), 'rb').read()
