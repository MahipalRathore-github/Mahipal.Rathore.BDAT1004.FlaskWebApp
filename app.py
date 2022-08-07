from flask import Flask, request, render_template
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
    CONNECTION_STRING= "mongodb+srv://mahipal:mahipal@dataprogramming.2mv3jvm.mongodb.net/?retryWrites=true&w=majority"
    ClientMongo = MongoClient(CONNECTION_STRING)
    dataBaseInstance = ClientMongo["DataProgramming"]
    collectionInstance = dataBaseInstance["Cryptocurrencies"]
    limit =  10 if request.args.get("limit") == None else int(request.args.get("limit"))
    page = 1 if request.args.get("page") == None else int(request.args.get("page"))
    pair = None if request.args.get("pair") == None else request.args.get("pair")
    filter = {} if pair == None else {"symbol" : pair}
    select = {"symbol": 1, "openPrice": 1, "highPrice": 1, "lowPrice": 1, "volume": 1,"openTime":1, "closeTime":1}
    dataFromMongo = list(collectionInstance.find(filter,select).skip(limit * (page - 1)).limit(limit))
    return dumps(dataFromMongo)

@app.route("/api/currency-pairs")
def currencypairs():
    CONNECTION_STRING="mongodb+srv://mahipal:mahipal@dataprogramming.2mv3jvm.mongodb.net/?retryWrites=true&w=majority"
    ClientMongo = MongoClient(CONNECTION_STRING)
    dataBaseInstance = ClientMongo["DataProgramming"]
    collectionInstance = dataBaseInstance["Cryptocurrencies"]
    dataFromMongo = list(collectionInstance.distinct("symbol"))
    return dumps(dataFromMongo)

if __name__=='__main_':
    app.run(debug=True,host="0.0.0.0")