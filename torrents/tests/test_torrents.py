from datetime import datetime
import hashlib

from torrents.torrent import Torrent

class TestTorrents:

    test_objs = {
            'name': 'Test1',
            'started': True,
            'dlrate': 10,
            'status': 0,
            'source': 'http://testurl.com',
            'seeds': 15,
            'leech': 20,
            'size': 20000,
            'size_done':  10000,
            'startdate': datetime(2007, 12, 6, 16, 29, 43, 79043),
            'hash': hashlib.md5('This is a test').hexdigest()
    }

    def test_constructor(self):
        tor1 = Torrent()

        assert not hasattr(tor1, 'name')
        assert not hasattr(tor1, 'started')
        assert not hasattr(tor1, 'seeds')

        tor2 = Torrent(self.test_objs)

        assert hasattr(tor2, 'name')
        assert hasattr(tor2, 'started')
        assert hasattr(tor2, 'seeds')


    def test_init_from_db(self):
        torrent = Torrent()
        torrent.init_from_db(self.test_objs)

        assert torrent.name == self.test_objs['name']
