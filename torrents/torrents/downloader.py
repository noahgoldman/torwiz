import libtorrent as lt

class Downloader:

    def __init__(self):
        self.ses = None
        self.handles = {}

    def start(self, session):
        # Start the session
        self.ses = session
        self.ses.listen_on(6881, 6891)

        # Configure settings
        settings = lt.session_settings()
        settings.user_agent = 'Torwiz XP Pro 2003 Ultimate Alfalfa 720 noscope yolo 0.0.1337'
        self.ses.set_settings(settings)

    def add_torrent(self, id, data):
        e = lt.bdecode(data)
        info = lt.torrent_info(e)

        params = { 'save_path': './data/' + str(id), \
                   'storage_mode': lt.storage_mode_t.storage_mode_sparse, \
                   'ti': info }
        h = self.ses.add_torrent(params)

        self.handles[id] = h
        return h.name()

    def delete(self, id):
        self.ses.remove_torrent(self.handles[id])

    def get_status_by_id(self, id):
        return self.handles[id].status()
