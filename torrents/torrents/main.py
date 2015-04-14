import libtorrent as lt
from pymongo import MongoClient

from torrents.torrent_collection import TorrentCollection

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

    print("wow, such connection, much mongo")

    # Make a torrent collection object
    torrents = TorrentCollection(client.torrents)

    while True:
        for torrent in torrents.marked_delete():
            # Delete the torrents
            pass
        for torrent in torrents.not_started():
            # start the torrents
            pass

if __name__=='__main__':
    run()
