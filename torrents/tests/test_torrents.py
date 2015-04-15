from datetime import datetime
import hashlib

from mock import Mock, patch

from torrents.torrent import Torrent

from bson.objectid import ObjectId

class TestTorrents:

    test_obj1 = {
            '_id': ObjectId(),
            'name': 'Test1',
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
    test_obj2 = {
            '_id': ObjectId(),
            'name': 'Test2',
            'dlrate': 5,
            'status': 0,
            'source': 'http://testurl2.com',
            'seeds': 20,
            'leech': 100,
            'size': 40000,
            'size_done':  20000,
            'startdate': datetime(2007, 12, 6, 16, 29, 43, 79043),
            'hash': hashlib.md5('This is the second test').hexdigest()
    }



    def test_constructor(self):
        tor1 = Torrent()

        assert not tor1.name
        assert not tor1.seeds

        tor2 = Torrent(self.test_obj1)

        assert tor2.name
        assert tor2.seeds


    def test_init_from_db(self):
        torrent = Torrent()
        torrent.init_from_db(self.test_obj1)

        assert torrent.name == self.test_obj1['name']
