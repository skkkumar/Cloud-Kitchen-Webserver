'''
Created on 25-Jun-2017

@author: sriram
'''
from database.LocationDB import LocationDB
import json

class GetLocations:
    def on_get(self, req, resp):
        """Handles GET requests"""
        
        
        #database object
        db = LocationDB()
        
        #initialize return values
        status = 1
        message = ""
        
       
        
        #fill response object
        response = {
            'status': status,
            "data" : db.getLocations(),
            'errorMessage': message
        }
        
        #add response object to return variable
        resp.body = json.dumps(response)
        
class AddArea:
    def on_post(self, req, resp):
        """Handles GET requests"""
        
        #get seller object from request
        areaObject = json.loads(req.stream.read())
        
        #database object
        db = LocationDB()
        
        #initialize return values
        status = 1
        message = "No Error Exist"
        """
        stateName = stateObject["name"]
        
        if statedb.checkState(stateName):
            statedb.addState(stateObject)
        else:
            status = 0
            message = "State Already Exist"
        """
        db.addArea(areaObject)
        
        #fill response object
        response = {
            'status': status,
            'errorMessage': message
        }
        
        #add response object to return variable
        resp.body = json.dumps(response)