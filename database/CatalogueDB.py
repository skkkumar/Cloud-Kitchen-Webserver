'''
Created on 26-Jun-2017

@author: sriram
'''
from pymongo.mongo_client import MongoClient
from bson.objectid import ObjectId

class CatalogueDB:
    
    def __init__(self):
        #connection to seller collection
        client = MongoClient('localhost', 27017)
        db = client['zing']
        self.cuisinecatalogue = db.cuisinecatalogue
        self.dishcatalogue = db.dishcatalogue
        self.ingredientcatalogue = db.ingredientcatalogue
        self.boxtype = db.boxtype
        
        
    def getAllCategories(self):
        
        return list(self.cuisinecatalogue.find())
    
    def getAllDishes(self, categoriesList):
        
       
        
        return list(self.dishcatalogue.find({"cuisineId" : {"$in" : categoriesList}}))
    
    
    def getDishIngredientIds(self, dishId):
        return self.dishcatalogue.distinct("ingredients.ingredientId", {"_id":ObjectId(dishId)})
    
    def getDishIngredients(self, ingredientIds):
        
        ingredientIds1 = []
        for ingredientId in ingredientIds:
            ingredientIds1.append(ObjectId(ingredientId))
        
        return list(self.ingredientcatalogue.find({"_id" : {"$in" : ingredientIds1}}))
        
        
    def getAllIngredients(self):
        
        return list(self.ingredientcatalogue.find())
    
    
    def getBoxTypes(self):
        return list(self.boxtype.find())
    
    
    def getDishesType(self, dishType):
        return list(self.dishcatalogue.find({"dishType" : dishType}))
