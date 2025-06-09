from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = 'mongodb+srv://alexandrebodin5:pzL3SDOhQLbaiqva@fastapi.t8ygffa.mongodb.net/?retryWrites=true&w=majority&appName=FastAPI'

client = MongoClient(uri, server_api=ServerApi('1'))

db = client.sample_weatherdata
collection = db['data']