from flask import Flask, request, render_template
from pymongo import MongoClient
from flask import jsonify,json
from bson.json_util import dumps
import pandas as pd

app = Flask(__name__,)

CONNECTION_STRING="mongodb+srv://mahipal:mahipal@dataprogramming.2mv3jvm.mongodb.net/?retryWrites=true&w=majority"
ClientMongo = MongoClient(CONNECTION_STRING)
dataBaseInstance = ClientMongo["DataProgramming"]
collectionInstance = dataBaseInstance["Cryptocurrencies"]
dataFromMongo = list(collectionInstance.find())

@app.route("/")
def home():
    return render_template("index.html",variable="Currency")

@app.route("/googleTable")
def googleTable():
    
    dataFrame =  pd.DataFrame(dataFromMongo)
    del dataFrame['_id']
    df1=dataFrame
    df1['variance'] = (df1.highPrice.astype(float).astype(int)) - (df1.lowPrice.astype(float).astype(int))
    df2 =df1[df1['variance'] > 1459]
    mydata = df2.to_dict('index')
    return render_template("googleTable.html",data=mydata)

@app.route("/currency")
def currency():

    df1=pd.DataFrame(dataFromMongo, columns=['symbol','volume'])
    df1['volume'] = df1['volume'].astype(float).astype(int)
    df2 =df1[df1['volume'] > 0]
    df3 = df2.groupby(['symbol'])['volume'].mean().astype(int)
    data_dict = df3.to_dict()
    new_data_dict = dict(filter(lambda val: val[1] > 999999999, data_dict.items()))
    finalData={'cryto':'volume'}
    finalData.update(new_data_dict)

    return render_template("currency.html",data=finalData)
    #return render_template("currency.html")


@app.route("/api/currencies")
def currencies():
<<<<<<< HEAD

=======
    CONNECTION_STRING= "mongodb+srv://mahipal:mahipal@dataprogramming.2mv3jvm.mongodb.net/?retryWrites=true&w=majority"
    ClientMongo = MongoClient(CONNECTION_STRING)
    dataBaseInstance = ClientMongo["DataProgramming"]
    collectionInstance = dataBaseInstance["Cryptocurrencies"]
>>>>>>> 468d80b7544aa596e6138e7ec62b82d74275321d
    limit =  10 if request.args.get("limit") == None else int(request.args.get("limit"))
    page = 1 if request.args.get("page") == None else int(request.args.get("page"))
    pair = None if request.args.get("pair") == None else request.args.get("pair")
    filter = {} if pair == None else {"symbol" : pair}
    select = {"symbol": 1, "openPrice": 1, "highPrice": 1, "lowPrice": 1, "volume": 1,"openTime":1, "closeTime":1}
    dataFromMongo = list(collectionInstance.find(filter,select).skip(limit * (page - 1)).limit(limit))
    return dumps(dataFromMongo)

@app.route("/api/currency-pairs")
def currencypairs():
<<<<<<< HEAD
    dataFromMongo = list(collectionInstance.distinct("symbol"))
    return dumps(dataFromMongo)

@app.route("/api/allcurrencies")
def allcurrencies():
    return dumps(dataFromMongo)

if __name__=='__main_':
    app.run(debug=True,host="0.0.0.0")
=======
    CONNECTION_STRING="mongodb+srv://mahipal:mahipal@dataprogramming.2mv3jvm.mongodb.net/?retryWrites=true&w=majority"
    ClientMongo = MongoClient(CONNECTION_STRING)
    dataBaseInstance = ClientMongo["DataProgramming"]
    collectionInstance = dataBaseInstance["Cryptocurrencies"]
    dataFromMongo = list(collectionInstance.distinct("symbol"))
    return dumps(dataFromMongo)

if __name__=='__main_':
    app.run(debug=True,host="0.0.0.0")
>>>>>>> 468d80b7544aa596e6138e7ec62b82d74275321d
