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

    print("wow, such connection, much mongo")

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
        torrents.get_torrents()

        for torrent in torrents.marked_delete():
            downloader.delete(torrent.id)
        for torrent in torrents.not_started():
            print("gettin some rents")
            # Download the torrent file
            torfile = TorrentFile(torrent.id)
            torfile.get_from_url(torrent.source)
            
            downloader.add_torrent(torrent.id, torfile.get_data())
            torrent.set_started()

def init_db(tordb):
    tordb.drop() 

    t1 = Torrent()
    t1.name = 'Shrek'
    t1.status = 0
    t1.source = 'http://torcache.net/torrent/7B973E55B2198EAC530440DC7D9589DD708F5692.torrent?title=[kickass.to]shrek.2001.1080p.brrip.x264.1gb.yify'
    t1.id = insert(tordb, t1.serialize())

    t2 = Torrent()
    t2.name = 'Wolverine'
    t2.status = 0
    t2.source = 'http://torcache.net/torrent/D91FBB667D8F7E9CC653123AABF37BB4851B2270.torrent?title=[kickass.to]the.wolverine.2013.extended.1080p.brrip.x264.yify'
    t2.id = insert(tordb, t2.serialize())

    print("wow we inserted")

if __name__=='__main__':
    run()
