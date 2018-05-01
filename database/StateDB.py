'''
Created on 23-Jun-2017

@author: sriram
'''
from pymongo import MongoClient
import pymongo

class StateDB:
    """
    This class performs all database operations related to seller collection
    """
    
    def __init__(self):
        #connection to seller collection
        client = MongoClient('localhost', 27017)
        db = client['zing']
        self.state = db.state
        
    
    def addState(self, stateObject):
        """ 
        This method adds seller object to database
        """
        self.state.insert_one(stateObject)
        
        
        
    def checkState(self, stateName):
        """ 
        This method adds seller object to database
        """
        countResult = self.state.find({"name" : stateName}).count()
        return countResult == 0
    
    def getAllStates(self):
        """ 
        This method return all the states in the database
        """
        return sorted(self.state.distinct("name"))