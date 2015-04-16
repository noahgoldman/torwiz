import libtorrent as lt
from pymongo import MongoClient

from torrents.torrent_collection import TorrentCollection
from torrents.downloader import Downloader
from torrents.file import TorrentFile
from torrents.database import insert
from torrents.torrent import Torrent

"""
The basic flow of the main loop should be:

    Check if any torrents are finished and should be deleted:
        if true, delete them
    Check if any torrents have not been started and should be:
        if true, start them
    Update the status of each torrent in the database

"""
def run():
    # Initialize the database
    client = MongoClient()

    # Make a torrent collection object
    db = client.torwiz
    torrent_collection = db.torrents
    torrents = TorrentCollection(torrent_collection)

    init_db(torrent_collection)

    # Create the torrenting process
    session = lt.session()
    downloader = Downloader()
    downloader.start(session)

    while True:
        torrents.refresh()

        # delete torrents that are marked for deletion
        for torrent in torrents.marked_delete():
            downloader.delete(torrent.id)

        # Start torrents that haven't been started
        for torrent in torrents.not_started():
            # Download the torrent file
            torfile = TorrentFile(torrent.id)
            torfile.get_from_url(torrent.source)
            
            torrent.name = downloader.add_torrent(torrent.id, torfile.get_data())
            torrent.set_started()

        for torrent in torrents:
            torrent.update_from_status(downloader.get_status_by_id(torrent.id))

        torrents.update()

def init_db(tordb):
    tordb.drop() 

if __name__=='__main__':
    run()
