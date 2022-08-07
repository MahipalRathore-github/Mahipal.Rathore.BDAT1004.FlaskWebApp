import requests
from pymongo import MongoClient
import schedule
import time

# SETS GLOBAL VARIABLES
def setGlobalVar():
    
    global API
    global CONNECTION_STRING
    global MongoDataBase
    global MongoCollection
    
    API="https://api2.binance.com/api/v3/ticker/24hr"
    CONNECTION_STRING= "mongodb+srv://mahipal:mahipal@dataprogramming.2mv3jvm.mongodb.net/?retryWrites=true&w=majority"
    MongoDataBase="DataProgramming"
    MongoCollection="Cryptocurrencies"
    print("setGlobalVar: SUCCESS")


# CONNECT TO MONGODB
def connectMongoDB():
    
    # Creating connection using MongoClient
    global collectionInstance
    ClientMongo = MongoClient(CONNECTION_STRING)
    dataBaseInstance = ClientMongo[MongoDataBase]
    collectionInstance = dataBaseInstance[MongoCollection]
    
    if(ClientMongo):
        print("connectMongoDB: SUCCESS")
    else:
        print("Error while connecting to MongoDB")

#FUNCTION TO GET DATA FROM API DYNAMICALLY
def getDataFromAPI():
    apiData = requests.get(API)
    if apiData.status_code == 200:
        
        global DataFromAPI
        DataFromAPI = apiData.json()
        print("getDataFromAPI: SUCCESS")
    else:
        print("Could not fetch data from API: ")
        exit()

# INGEST DATA IN MONGODB
def IngestDataInMongoDB():
    
    collectionInstance.insert_many(DataFromAPI)
    print("IngestDataInMongoDB: SUCCESS")

def batchProcessingJob():

    getDataFromAPI()
    IngestDataInMongoDB()


#main 
# set attribute and make connection to mongo
setGlobalVar()
connectMongoDB()

# ingest data to mongo every 24 hours

schedule.every().day.at('08:00').do(batchProcessingJob)
#schedule.every(5).seconds.do(batchProcessingJob)


while True:
    schedule.run_pending()
    time.sleep(10)