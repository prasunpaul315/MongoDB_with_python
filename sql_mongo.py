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
        
# SELECT STUDENT_ID AS _id, COUNT(STUDENT_ID) AS Total Count FROM GRADE GROUP BY STUDENT_ID
elif(argv[1].lower().replace(" ", "") == "select student_id as _id, count(student_id) as Total Count from grade group by student_id ".lower().replace(" ", "")):
    #id = int(re.sub("\D", "", argv[1]))

    agg_result= col.aggregate( 
    [{ 
    "$group" :  
        {"_id" : "$student_id",  
         "Total Count" : {"$sum" : 1},
         }}
    ])

    s_id = []
    total = []
    for i in agg_result:
        s_id.append(i['_id'])
        total.append(i['Total Count'])
    
    df = pd.DataFrame({"student_id" : s_id, "Total Count" : total })
    
    df.to_csv('test.csv', index=False)
    print("result is successfully saved on test.csv")
    

else:
    print("SQL query is not programmed!")

    
