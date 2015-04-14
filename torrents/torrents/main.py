import libtorrent as lt
from pymongo import MongoClient

from torrents.torrent_collection import TorrentCollection
from torrents.downloader import Downloader

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
    client = MongoClient('mongo', 27017) 

    print("wow such connection")

    # Make a torrent collection object 
    torrents = TorrentCollection(client.torrents)

    # Create the torrenting process
    session = lt.session()
    downloader = Downloader()
    downloader.start(session)

    while True:
        for torrent in torrents.marked_delete():
            downloader.delete(torrent.id)
        for torrent in torrents.not_started():
            # start the torrents
            pass

if __name__=='__main__':
    run()
