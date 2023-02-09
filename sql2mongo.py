#!/integ/tools/python3/bin/python3
import pandas as pd
import pymongo
from sys import argv
import sys
import re
import sqlvalidator
from typing import Any, List, Optional, Set
import json

def readJSON():
    # reading mongo command  from sql2mongo.json
    jsonFile = open('sql2mongo.json', 'r')
    values = json.load(jsonFile)
    return values

def connection_establishment():
    # database connection establishment 
    client = pymongo.MongoClient('mongodb://integ:integ_rocks@sjo-sv-integ01:27017,sjo-sv-integ06:27017,sjo-sv-integ07:27017/?replicaSet=rs01')

    values = readJSON()

    # 'db' variable stores database name & 'col' variable stores collection name
    db, col = values.get('collection').split(".")
    mydb = client[db]
    collection = mydb[col]


    query = values.get('query')
    limit = values.get('limit')
    if(values.get('projection')):
        projection = values.get('projection')
    else:
        projection = ""    

    # the variable 'true_fields' stores all fields present on all documents of a perticular collection
    true_fields = list(collection.find_one().keys())

    # the variable 'necessary_field' stores all necessary fields to show
    necessary_field = list(projection.keys())

    for i in necessary_field:
        if(i not in true_fields):
            print("incorrect field entered")
            sys.exit(0)

    return necessary_field, query, collection

def makeCSV():
    necessary_field, query,collection = connection_establishment()
    def enable_field(necessary_field):
        dic = dict()
        for i in necessary_field:
            dic.update({i:1})

        return dic
    d = enable_field(necessary_field)
    df = pd.DataFrame(columns=necessary_field , data=collection.find(query , d))
    #print(df.head())
    df.to_csv('test.csv')
    print("result is successfully saved on test.csv")
    sys.exit(0)
makeCSV()








jsonFile.close()
