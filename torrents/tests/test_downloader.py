import os

from mock import Mock, patch
import pytest
from bson.objectid import ObjectId

from torrents.downloader import Downloader
#path of torrent file
def path_to_fixture(name):
    module_dir = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(module_dir, 'fixtures', name)

@pytest.fixture
def dl_obj():
    ses = Mock()
    ses.listen_on = Mock()

    downloader = Downloader()
    downloader.ses = ses
    return downloader

class TestDownloader:
    #tests to see if torrent file is downloading
    def test_start(self, dl_obj):
        ses = Mock()
        ses.listen_on = Mock()

        dl_obj.start(ses)

        assert ses.listen_on.called_once
    #test to see if a torrent was successfully added
    def test_add_torrent(self, dl_obj):
        dl_obj.ses.add_torrent = Mock()
        dl_obj.start(dl_obj.ses)

        data = open(path_to_fixture('test1.torrent'), 'rb').read()
        dl_obj.add_torrent(ObjectId(), data)

        assert dl_obj.ses.add_torrent.called_once
