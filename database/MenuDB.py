'''
Created on 26-Jun-2017

@author: sriram
'''
from pymongo.mongo_client import MongoClient
from bson.objectid import ObjectId

class MenuDB:
    
    def __init__(self):
        #connection to seller collection
        client = MongoClient('localhost', 27017)
        db = client['zing']
        self.sellermenu = db.sellermenu
       
        
    def createBlankSellerEntry(self, sellerId):
        self.sellermenu.insert_one({"sellerId" : sellerId, "sellerRatings" : 0.0, "dishes" : []})
        
        
    def getSellerMenu(self, sellerId):
        return list(self.sellermenu.find({"sellerId" : sellerId}))
        
    def addSellerMenu(self, sellerId, baseDishId, dishData):
        #self.sellermenu.update({"sellerId" : sellerId},{"$push" : { "dishes" : dishData}})
        results = self.sellermenu.update_one({"sellerId" : sellerId, "baseDishId" : baseDishId }, {"$set" : dishData}, True)
        return results.upserted_id
    
    def updateSellerMenu(self, sellerId, dishId, dishData):
        self.sellermenu.update_one({"_id" : ObjectId(dishId) }, {"$set" : dishData}, True)
        
        
    def getSellerCategories(self, sellerId):
        #db.sellermenu3.distinct("dishes.cuisineId",{"sellerId":"4t0fbdkfk"})
        return self.sellermenu.distinct("cuisineId", {"sellerId" : sellerId}) 
    
    
    def getDishPhoto(self, dishId):
        return self.sellermenu.find_one({"_id" : ObjectId(dishId)}, {"image" : 1, "_id" : 0})
    
    def setDishPhoto(self, dishId, imageData):
        self.sellermenu.update({ "_id" : ObjectId(dishId)}, { "$set" : {"image" : imageData}})
        
    def getDishDescription(self, dishId):
        return self.sellermenu.find_one({"_id" : ObjectId(dishId)}, {"description" : 1, "_id" : 0})
    
    def setDishDescription(self, dishId, description):
        self.sellermenu.update({ "_id" : ObjectId(dishId)}, { "$set" : {"description" : description}})