from bson.objectid import ObjectId

from torrents.file import TorrentFile

class TestTorrentFile:

    def test_get_output_file(self):
        id1 = ObjectId()
        file1 = TorrentFile(id1)
        assert file1.get_output_file() == 'torrent_files/' + str(id1) + '.torrent'
