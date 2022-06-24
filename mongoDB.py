import pymongo

def mongodb():
    #server
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")

    mydb = myclient["DuzceTV"]

    if mydb.list_collection_names().count("Veriler"):
        mydb.drop_collection("Veriler")

    mycol = mydb["Veriler"]

    return mycol
