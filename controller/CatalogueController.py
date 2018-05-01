'''
Created on 26-Jun-2017

@author: sriram
'''
from database.CatalogueDB import CatalogueDB
import json
from bson.json_util import dumps
class GetAllCategories:
    
    def on_get(self, req, resp):
        
        db = CatalogueDB()
        
        #initialize return values
        status = 1
        message = "No Error Exist"
        
        data = db.getAllCategories()
        #fill response object
        response = {
            'status': status,
            'errorMessage': message,
            "data" : data
        }
        
        #add response object to return variable
        resp.body = dumps(response)
        
class GetAllDishes:
    
    def on_post(self, req, resp):
        
        #get seller object from request
        categoriesObject = json.loads(req.stream.read())
        categoriesList = categoriesObject["categories"]
         
        db = CatalogueDB()
        
        #initialize return values
        status = 1
        message = "No Error Exist"
        
        data = db.getAllDishes(categoriesList)
        #fill response object
        response = {
            'status': status,
            'errorMessage': message,
            "data" : data
        }
        
        #add response object to return variable
        resp.body = dumps(response)
        
        
class GetIngredients:
    
    def on_post(self, req, resp):
        
        #get seller object from request
        categoriesObject = json.loads(req.stream.read())
        db = CatalogueDB()
        
        dishId = categoriesObject["dishId"]
        ingredientIds = db.getDishIngredientIds(dishId)
        print "ingredientIds", ingredientIds
        
        
        #initialize return values
        status = 1
        message = "No Error Exist"

        data = db.getDishIngredients(ingredientIds)

        
        #fill response object
        response = {
            'status': status,
            'errorMessage': message,
            "data" : data
        }
        
        #add response object to return variable
        resp.body = dumps(response)
        
        
class GetAllIngredients:
    
    def on_get(self, req, resp):
        db = CatalogueDB()
        
        #initialize return values
        status = 1
        message = "No Error Exist"
        
        data = db.getAllIngredients()
        #fill response object
        response = {
            'status': status,
            'errorMessage': message,
            "data" : data
        }
        
        #add response object to return variable
        resp.body = dumps(response)
        
class GetBoxTypes:
    def on_get(self, req, resp):
        db = CatalogueDB()
        
        #initialize return values
        status = 1
        message = "No Error Exist"
        
        data = db.getBoxTypes()
        #fill response object
        response = {
            'status': status,
            'errorMessage': message,
            "data" : data
        }
        
        #add response object to return variable
        resp.body = dumps(response)
        
class GetDishesByType:
    
    def on_post(self, req, resp):
        
        #get seller object from request
        categoriesObject = json.loads(req.stream.read())
        dishType = categoriesObject["dishType"]
        
        db = CatalogueDB()
        
        #initialize return values
        status = 1
        message = "No Error Exist"

        data = db.getDishesType(dishType)

        
        #fill response object
        response = {
            'status': status,
            'errorMessage': message,
            "data" : data
        }
        
        #add response object to return variable
        resp.body = dumps(response)