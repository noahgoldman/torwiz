from datetime import datetime
import hashlib

from mock import Mock, patch
import pytest

from torrents.torrent_collection import TorrentCollection
from torrents.torrent import TorStatus

from bson.objectid import ObjectId

@pytest.fixture
def torrents():
    test_obj1 = {
            '_id': ObjectId(),
            'name': 'Test1',
            'started': True,
            'dlrate': 10,
            'status': 0,
            'source': 'http://testurl.com',
            'seeds': 15,
            'leech': 20,
            'size': 20000,
            'size_done':  10000,
            'start_time': datetime(2007, 12, 6, 16, 29, 43, 79043),
            'hash': hashlib.md5('This is a test').hexdigest()
    }
    test_obj2 = {
            '_id': ObjectId(),
            'name': 'Test2',
            'started': False,
            'dlrate': 5,
            'status': 2,
            'source': 'http://testurl2.com',
            'seeds': 20,
            'leech': 100,
            'size': 40000,
            'size_done':  20000,
            'start_time': datetime(2007, 12, 6, 16, 29, 43, 79043),
            'hash': hashlib.md5('This is the second test').hexdigest()
    }

    return [test_obj1, test_obj2]

class TestTorrentCollection(object):
    #Test functionality of refreshing progressbar
    def test_refresh(self, torrents):
        db_mock = Mock()
        db_mock.find = Mock(return_value = torrents)

        coll = TorrentCollection(db_mock)
        coll.refresh()

        assert len(coll.torrents) == 2

        assert coll.torrents[0].hash == torrents[0]['hash']
        assert coll.torrents[1].hash == torrents[1]['hash']
    # Tests if a torrent is not started
    def test_not_started(self, torrents):
        torrents[0]['status'] = TorStatus.UNSTARTED

        db_mock = Mock()
        db_mock.find = Mock(return_value = torrents)

        coll = TorrentCollection(db_mock)
        coll.refresh()
        
        not_started = coll.not_started()
        assert len(not_started) is 1
        assert not_started[0].status == TorStatus.UNSTARTED
    # Tests if a torrent was successfully marked for deletion
    def test_marked_delete(self, torrents):
        torrents[0]['status'] = TorStatus.DELETE

        db_mock = Mock()
        db_mock.find = Mock(return_value = torrents)

        coll = TorrentCollection(db_mock)
        coll.refresh()

        delete = coll.marked_delete()

        assert len(delete) is 1
        assert delete[0].status == TorStatus.DELETE
