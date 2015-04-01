from torrents.torrent import Torrent, TorStatus

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
    def get_torrents(self):
        self.torrents = []

        for torrent in self.tordb.find():
            self.torrents.append(Torrent(torrent))

    def not_started(self):
        return [t for t in self.torrents if t.status is TorStatus.UNSTARTED]

    def marked_delete(self):
        return [t for t in self.torrents if t.status is TorStatus.DELETE]
