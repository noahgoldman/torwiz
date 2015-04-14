import libtorrent as lt

class Downloader:

    def __init__(self):
        self.ses = None

    def start(self, session):
        # Start the session
        self.ses = session
        self.ses.listen_on(6881, 6891)

    def add_torrent(self, id, data):
        e = lt.bdecode(data)
        info = lt.torrent_info(e)

        params = { 'save_path': './data/', \
                   'storage_mode': lt.storage_mode_t.storage_mode_sparse, \
                   'ti': info }
        h = self.ses.add_torrent(params)

    def delete(self, id):
        self.ses.remove_torrent(self.handles[id])

    def handles(self):
        return self.ses.get_torrents()
