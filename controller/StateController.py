'''
Created on 23-Jun-2017

@author: sriram
'''
import json
from database.StateDB import StateDB
from bson import json_util

class AddState:
    """
    This class deals with registering the seller
    """
    def on_post(self, req, resp):
        """Handles GET requests"""
        
        #get seller object from request
        stateObject = json.loads(req.stream.read())
        
        #database object
        statedb = StateDB()
        
        #initialize return values
        status = 1
        message = "No Error Exist"
        
        stateName = stateObject["name"]
        
        if statedb.checkState(stateName):
            statedb.addState(stateObject)
        else:
            status = 0
            message = "State Already Exist"
        #fill response object
        response = {
            'status': status,
            'errorMessage': message
        }
        
        #add response object to return variable
        resp.body = json.dumps(response)

class GetStates:
    
    def on_get(self, req, resp):
        
        statedb = StateDB()
        resp.body =  json.dumps(statedb.getAllStates())
        
        