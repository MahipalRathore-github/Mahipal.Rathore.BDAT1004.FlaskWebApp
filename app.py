from flask import Flask, render_template
from pymongo import MongoClient
from flask import jsonify,json
from bson.json_util import dumps

app = Flask(__name__,)

@app.route("/")
def home():
    return render_template("index.html",variable="Currency")

@app.route("/currency")
def currency(): 
    return render_template("currency.html")

@app.route("/api/currencies")
def currencies():
    #return jsonify({'name':'Jimit',
    #               'address':'India'})

    CONNECTION_STRING= "mongodb+srv://mahipal:mahipal@dataprogramming.2mv3jvm.mongodb.net/?retryWrites=true&w=majority"
    ClientMongo = MongoClient(CONNECTION_STRING)
    dataBaseInstance = ClientMongo["DataProgramming"]
    collectionInstance = dataBaseInstance["Cryptocurrencies"]
    dataFromMongo = list(collectionInstance.find())
    return dumps(dataFromMongo)



if __name__=='__main_':
    app.run(debug=True)