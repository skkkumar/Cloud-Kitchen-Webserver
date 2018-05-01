'''
Created on 25-Jun-2017

@author: sriram
'''
from pymongo.mongo_client import MongoClient
from uuid import uuid4
class LocationDB:
    def __init__(self):
        #connection to seller collection
        client = MongoClient('localhost', 27017)
        db = client['zing']
        self.location = db.location
        
    def getLocations(self):
        return self.location.find_one({},{"_id":0})
    
    
    def addArea(self, locationObject):
        country = locationObject["country"]
        state = locationObject["state"]
        city = locationObject["city"]
        keyname = country + "." + state + "." + city
        
        locationObject["id"] = str(uuid4() )
        
        locationObject.pop('country', None)
        locationObject.pop('state', None)
        locationObject.pop('city', None)
        self.location.update({},{"$push" : {keyname : locationObject}})