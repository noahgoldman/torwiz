import os

"""
A class to encapsulate a torrent object.

Fields:
    name: str,
    started: bool,
    dlrate: int,
    status: enum TorStatus class,
    source: string?,
    seeds: int,
    leech: int,
    size: int,
    size_done: int,
    startdate: date,
    hash: string,
"""

# An enum to represent the status of a torrent
class TorStatus:
    UNSTARTED = 0
    DOWNLOADING = 1
    STOPPED = 2
    FINISHED = 3
    DELETE = 4

class Torrent(object):

    def __init__(self, obj=None):
        if obj is not None:
            self.init_from_db(obj)
        else:
            self.name = None
            self.dlrate = None 
            self.status = None
            self.source = None
            self.seeds = None
            self.leech = None
            self.size = None
            self.size_done = None
            self.start_time = None
            self.hash = None

    # Initialize a torrent object from db
    def init_from_db(self, obj):
        self.id = obj['_id']
        self.name = obj['name']
        self.dlrate = obj['dlrate']
        self.status = obj['status']
        self.source = obj['source']
        self.seeds = obj['seeds']
        self.leech = obj['leech']
        self.size = obj['size']
        self.size_done = obj['size_done']
        self.start_time = obj['start_time']
        self.hash = obj['hash']
        # sets status to started
    def is_started(self):
        return self.status != TorStatus.UNSTARTED
        # sets status to delete
    def marked_delete(self):
        return self.status == TorStatus.DELETE

    def finished(self):
        return self.status == TorStatus.FINISHED

    def files_dir(self):
        return os.path.join('data', str(self.id))

    def serialize(self):
        return {
                'name': self.name,
                'dlrate': self.dlrate,
                'status': self.status,
                'source': self.source,
                'seeds': self.seeds,
                'leech': self.leech,
                'size': self.size,
                'size_done': self.size_done,
                'start_time': self.start_time,
                'hash': self.hash
        }

    def set_started(self):
        self.status = TorStatus.DOWNLOADING
    #updates container fields with information from status
    def update_from_status(self, status):
        #self.name = status.name
        
        # Handle changing the status
        if status.finished_time != 0:
            self.status = TorStatus.FINISHED

        self.dlrate = status.download_rate
        self.seeds = status.num_seeds
        self.leech = status.num_peers
        self.size = status.total_wanted
        self.size_done = status.total_download
        self.start_time = status.added_time
        self.hash = str(status.info_hash)
