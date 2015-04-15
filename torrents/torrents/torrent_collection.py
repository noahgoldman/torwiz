from torrents.torrent import Torrent, TorStatus
from torrents import database as DB

"""
A class to contain a collection of torrents
"""
class TorrentCollection(object):

    def __init__(self, tordb):
        self.tordb = tordb
        self.torrents = []

    # Make the class iterable
    def __iter__(self):
        return iter(self.torrents)

    # Get all torrents from the database
    def refresh(self):
        self.torrents = map(Torrent, DB.get_all(self.tordb))

    def not_started(self):
        return [t for t in self.torrents if not t.is_started()]

    def marked_delete(self):
        return [t for t in self.torrents if t.marked_delete()]

    # Update the database with the torrent objects
    def update(self):
        for torrent in self.torrents:
            DB.update_full(self.tordb, torrent.id, torrent.serialize())
