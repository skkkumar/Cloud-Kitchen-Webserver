'''
Created on 26-Jun-2017

@author: sriram
'''
import json
from database.MenuDB import MenuDB
from uuid import uuid4
from bson.json_util import dumps


class SetSellerMenu:
    
    def on_post(self, req, resp):
        
        #get seller object from request
        menuObject = json.loads(req.stream.read())
        sellerId = menuObject["sellerId"]
        dishes = menuObject["data"]["dishes"]
        
        db = MenuDB()
        
        #initialize return values
        status = 1
        message = "No Error Exist"

        #fill in dishId, creation date 
        
        for dishData in dishes:
            dishData["sellerId"] = sellerId
            baseDishId = dishData["baseDishId"]
            if 'dishId' not in dishData:
                dishData["creationDate"] = ""
                dishId = db.addSellerMenu(sellerId, baseDishId, dishData)
            else:
                dishData["modifiedDate"] = ""
                dishId = dishData["dishId"]
                dishData.pop('dishId', None)
                db.updateSellerMenu(sellerId, dishId, dishData)
            

        #fill response object
        response = {
            'status': status,
            'errorMessage': message,
            'data' : dishId
        }
        
        #add response object to return variable
        resp.body = dumps(response)
        
        
class GetSellerMenu:
    
    def on_post(self, req, resp):
        
        #get seller object from request
        menuObject = json.loads(req.stream.read())
        sellerId = menuObject["sellerId"] 
    
        
        db = MenuDB()
        
        #initialize return values
        status = 1
        message = "No Error Exist"
          
        data = {}  
        data["dishes"] = db.getSellerMenu(sellerId)
        data["categories"] = db.getSellerCategories(sellerId)
        
        #fill response objectSetDishPhoto
        response = {
            'status': status,
            'errorMessage': message,
            'data' : data
        }
        
        #add response object to return variable
        resp.body = dumps(response)
        
        
class SetDishPhoto:
    
    def on_post(self, req, resp):
        #get seller object from request
        menuObject = json.loads(req.stream.read())
        dishId = menuObject["dishId"] 
        imageData = menuObject["image"] 
        
        db = MenuDB()
        
        #initialize return values
        status = 1
        message = "No Error Exist"
          
        db.setDishPhoto( dishId, imageData)
        
        #fill response objectSetDishPhoto
        response = {
            'status': status,
            'errorMessage': message
        }
        
        #add response object to return variable
        resp.body = json.dumps(response)
        

class GetDishPhoto:
    
    def on_post(self, req, resp):
        #get seller object from request
        menuObject = json.loads(req.stream.read())
        dishId = menuObject["dishId"] 
        
        db = MenuDB()
        
        #initialize return values
        status = 1
        message = "No Error Exist"
          
        data = db.getDishPhoto(dishId)
        
        #fill response objectSetDishPhoto
        response = {
            'status': status,
            'errorMessage': message,
            'data' : data
        }
        
        #add response object to return variable
        resp.body = json.dumps(response)
        
class SetDishDescription:
    
    def on_post(self, req, resp):
        #get seller object from request
        menuObject = json.loads(req.stream.read())
        dishId = menuObject["dishId"] 
        description = menuObject["description"] 
        
        db = MenuDB()
        
        #initialize return values
        status = 1
        message = "No Error Exist"
          
        db.setDishDescription(dishId, description)
        
        #fill response objectSetDishPhoto
        response = {
            'status': status,
            'errorMessage': message
        }
        
        #add response object to return variable
        resp.body = json.dumps(response)
        

class GetDishDescription:
    
    def on_post(self, req, resp):
        #get seller object from request
        menuObject = json.loads(req.stream.read())
        dishId = menuObject["dishId"] 
        return "dishId", dishId
        
        db = MenuDB()
        
        #initialize return values
        status = 1
        message = "No Error Exist"
          
        data = db.getDishDescription(dishId)
        
        #fill response objectSetDishPhoto
        response = {
            'status': status,
            'errorMessage': message,
            'data' : data
        }
        
        #add response object to return variable
        resp.body = json.dumps(response)