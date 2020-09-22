import os
from flask import Flask
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

# Defines the env varible with the password
from os import path
if path.exists("env.py"):
  import env 

MONGODB_URI = os.environ.get('MONGO_URI')
# end

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'task_manager'
app.config["MONGO_URI"] = 'MONGO_URI'


@app.route('/')
def hello():
    return 'Hello World ...again'

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)