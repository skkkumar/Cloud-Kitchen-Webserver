from pymongo import MongoClient
from bson.objectid import ObjectId


class SellerDB:
    """
    This class performs all database operations related to seller collection
    """
    
    def __init__(self):
        #connection to seller collection
        client = MongoClient('localhost', 27017)
        db = client['zing']
        self.seller = db.seller
        
    
    def addSeller(self, sellerObject):
        """
        This method adds seller object to database
        """
        #date = ISODate().getTime()
        sellerId = self.seller.insert_one(sellerObject).inserted_id
        return sellerId
    
    
    
    def checkEmailPresent(self, emailAddress):
        """
        This method checks if email address is present in the database
        """
        countResult = self.seller.find({"emailAddress" : emailAddress}).count()
        print "email count ", countResult
        return countResult == 0
    
    
    def checkMobilePresent(self, mobileNumber):
        """
        This method checks if email address is present in the database
        """
        countResult = self.seller.find({"mobileNumber" : mobileNumber}).count()
        print "phone count ", countResult
        return countResult == 0
    
    
    def getPasswordEmail(self, emailAddress):
        """
        This method returns password for email address based login
        """
        doc = self.seller.find_one({"emailAddress" : emailAddress}, {"password" : 1})
        
        password = doc["password"]
        sellerId = doc["_id"]

        print "password", password
        return password, sellerId
            
    
    def getPasswordMobile(self, mobileNumber):
        """
        This method returns password for mobile number login
        """
        doc = self.seller.find_one({"mobileNumber" : mobileNumber}, {"password" : 1})
        
        password = doc["password"]
        sellerId = doc["_id"]

        print "password", password
        return password, sellerId
    
    
    def getVerifiedStatus(self, sellerId):
        return self.seller.find_one({"_id" : ObjectId(sellerId)}, {"verifiedStatus" : 1, "_id" : 0})
         