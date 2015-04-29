from flask import Flask, render_template, request, redirect
import os
from pymongo import MongoClient
from flask.ext.pymongo import PyMongo
from bson import json_util
#ENUM to represent the torrent status
class TorStatus:
    UNSTARTED = 0
    DOWNLOADING = 1
    STOPPED = 2
    FINISHED = 3
    DELETE = 4
def connect():
		connection = MongoClient('localhost', 27017)
		handle = connection["torwiz"]
		return handle


app = Flask(__name__)
handle = connect()

#sets the route for which html template to display
@app.route("/index" ,methods=['GET'])
@app.route("/", methods=['GET'])
def index():
    torrents = [x for x in handle.torrents.find()]
    return render_template('index.html', torrents=torrents)

@app.route("/write", methods=['POST'])
def write():
    userinput = request.form.get("userinput")
    handle.torrents.insert({"name": userinput, 'dlrate': None, "source":userinput, "status": TorStatus.UNSTARTED, 'seeds': 0, 'leech': 0, 'size': 0, 'size_done': 0, 'start_time': 0, 'hash': None})

    return redirect ("/")
#all the torrents in the collection get deleted
@app.route("/deleteall", methods=['GET'])
def deleteall():
    handle.torrents.remove()
    return redirect ("/")
#refresh the progress bar to update completion status
@app.route('/refresh', methods=['GET'])
def refresh():
    torrents = [x for x in handle.torrents.find()]
    return json_util.dumps(torrents) 

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))

    app.run(host='0.0.0.0', port=port, debug=True)
