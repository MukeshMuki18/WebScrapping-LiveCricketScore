import os
from flask import Flask
from bs4 import BeautifulSoup
import requests
import pymongo
# import dns
# from pymongo import MongoClient

my_secret = os.environ['password']
client = pymongo.MongoClient(f"mongodb+srv://Mukesh:{my_secret}@cluster0.xwvbzhz.mongodb.net/?retryWrites=true&w=majority")
db = client['test']

collection=db['test']

app = Flask(__name__)
l=[]
@app.route('/')
def index():
    data=requests.get("https://www.google.com/search?q=cricket+live+score&rlz=1C1GCEA_enIN950IN950&oq=cricket+live+score&aqs=chrome.0.69i59l2j0i67i131i433l2j69i60l4.1499j0j7&sourceid=chrome&ie=UTF-8#sie=m;/g/11rnf0plxg;5;/m/026y268;dt;fp;1;;;").text
    soup = BeautifulSoup(data,"lxml")

    score =  soup.find_all('div',class_="BNeawe deIvCb AP7Wnd")
    
    # print(collection.find({"name":"user"}))
    team = soup.find_all('div',class_='BNeawe s3v9rd AP7Wnd lRVwie' )

    team1, score1=team[1].text, score[1].text
    team2, score2=team[2].text, score[2].text
    update= {
      "_id": 1,
      "team1": team1,
      "team2": team2,
      "score1": score1,
      "score2": score2
    }
    collection.update_one({"_id":1}, {"$set":update})
    return 'collection added successfully'
    # collection.insert_one(update)
    # duplicate_check= collection.find({"score1":score1, "score2":score2})
    
    # duplicate_check=collection.find({"team1":"NED"})
    # for i in duplicate_check:
    #   print(i['score2'])
  
    # print(duplicate_check)
    # for i in duplicate_check:
    #   print(i)
    #   return "Data already exist"
    # collection.insert_one(update)
    # print("collection added successfully")
  
    

app.run(host='0.0.0.0', port=81)
