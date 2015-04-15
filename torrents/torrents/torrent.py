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
    DELETE = 3

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

    # Initialize a torrent object from
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

    def is_started(self):
        return self.status != TorStatus.UNSTARTED

    def marked_delete(self):
        return self.status == TorStatus.DELETE

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
