#!pip install pymongo

#importing necessary modules
import pandas as pd
import pymongo
from sys import argv
import re


client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')


mydb = client['grade']
col = mydb.result

# SELECT * FROM GRADE
if(argv[1].lower().replace(" ", "") == "select * from grade".replace(" ", "")):
    
    df = pd.DataFrame(columns=col.find_one().keys() , data=col.find({}))
    #print(df.head())

    # storing dataframe into csv file
    df.to_csv('test.csv', index=False)

    print("result is successfully saved on test.csv")


# SELECT SCORES FROM GRADE WHERE STUDENT_ID = <ANY-STUDENT_ID>
elif(''.join((x for x in argv[1] if not x.isdigit())).lower().replace(" ", "") == "select scores from grade where student_id = ".replace(" ", "")):
    id = int(re.sub("\D", "", argv[1]))
    if(id>=0 and id<=49):
        #print(id)
        df = pd.DataFrame(columns=["scores"] , data=col.find({"student_id":id} , {"scores":1, "_id":0}))
        #print(df.shape)
        #df.head()
        df.to_csv('test.csv', index=False)
        print("result is successfully saved on test.csv")

    else:
        print("given student_id does not exist")

else:
    print("SQL query is not programmed!")

    
