from pymongo import MongoClient
import pandas as pd
import json

client = MongoClient()
db = client.get_database("companies")

def offices_nearto(df_coor,max_meters,name_coor_column,db_tocompare):
    points = []
    lst=[]
    for k,v in df_coor.iterrows():
        point = {
            "type":"Point",
            "coordinates":json.loads(v[name_coor_column])
        }
        points.append(point)
    for i in points:
        res = db_tocompare.find({"coord":{"$near":i,"$maxDistance":max_meters}})
        lst += list(res)   
    return [str(i['_id']) for i in lst]



def intersection(lst1, lst2): 
    tup1 = map(tuple, lst1) 
    tup2 = map(tuple, lst2)  
    return ["".join(i) for i in list(map(list, set(tup1).intersection(tup2)))]




#[i["offices"][] for i in lst]