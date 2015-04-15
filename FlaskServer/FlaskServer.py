from flask import Flask, render_template, request, redirect
import os
from pymongo import MongoClient
from flask.ext.pymongo import PyMongo
class TorStatus:
    UNSTARTED = 0
    DOWNLOADING = 1
    STOPPED = 2
    FINISHED = 3
    DELETE = 3
def connect():
		connection = MongoClient('localhost', 27017)
		handle = connection["torwiz"]
		return handle


app = Flask(__name__)
handle = connect()


@app.route("/index" ,methods=['GET'])
@app.route("/", methods=['GET'])
def index():
    torrents = [x for x in handle.torrents.find()]
    return render_template('index.html', torrents=torrents)

@app.route("/write", methods=['POST'])
def write():
    userinput = request.form.get("userinput")
    handle.torrents.insert({"url":userinput, "status": TorStatus.UNSTARTED})

    #tell the user that it added successfully or not

    return redirect ("/")

@app.route("/deleteall", methods=['GET'])
def deleteall():
    handle.torrents.remove()
    return redirect ("/")


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))

    app.run(host='0.0.0.0', port=port, debug=True)
