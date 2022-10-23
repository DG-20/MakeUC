from pymongo import MongoClient

HOST_LINK = "mongodb+srv://MakeUC:MakeUC123@cluster0.a3gqkxm.mongodb.net/?retryWrites=true&w=majority"


def connect_to_db():
    return MongoClient(HOST_LINK).block
