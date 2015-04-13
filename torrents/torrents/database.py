def get_all(tordb):
    return tordb.find()

def delete(tordb, obj_id):
    tordb.remove([obj_id])
