import libtorrent as lt
from pymongo import MongoClient

def run():
    # Initialize the database
    client = MongoClient() 
    print("initialized database")


if __name__=='__main__':
    run()
