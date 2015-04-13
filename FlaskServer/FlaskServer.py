from flask import Flask, render_template, request, redirect
import os
from pymongo import MongoClient
from flask.ext.pymongo import PyMongo

def connect():
		connection = MongoClient("ds041157.mongolab.com",41157)
		handle = connection["torwizdb"]
		handle.authenticate("root","poopdick")
		return handle


app = Flask(__name__)
handle = connect()


@app.route("/index" ,methods=['GET'])
@app.route("/", methods=['GET'])
def index():
    userinputs = [x for x in handle.torrents.find()]
    return render_template('index.html', userinputs=userinputs)

@app.route("/write", methods=['POST'])
def write():
    userinput = request.form.get("userinput")
    oid = handle.torrents.insert({"url":userinput})
    return redirect ("/")

@app.route("/deleteall", methods=['GET'])
def deleteall():
    handle.torrents.remove()
    return redirect ("/")


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))

    app.run(host='0.0.0.0', port=port, debug=True)