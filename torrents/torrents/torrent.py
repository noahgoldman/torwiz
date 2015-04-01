"""
A class to encapsulate a torrent object.

Fields:
    name: str,
    started: bool,
    dlrate: int,
    status: bool?,
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

    # Initialize a torrent object from  
    def init_from_db(self, obj):
        self.name = obj['name']
        self.started = obj['started']
        self.dlrate = obj['dlrate']
        self.status = obj['status']
        self.source = obj['source']
        self.seeds = obj['seeds']
        self.leech = obj['leech']
        self.size = obj['size']
        self.size_done = obj['size_done']
        self.start_time = obj['startdate']
        self.hash = obj['hash']
