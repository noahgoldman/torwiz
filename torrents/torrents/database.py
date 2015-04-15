def get_all(tordb):
    return tordb.find()

def delete(tordb, obj_id):
    tordb.remove([obj_id])

def insert(tordb, obj):
    return tordb.insert(obj)
