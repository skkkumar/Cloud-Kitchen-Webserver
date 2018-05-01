import json
from database.SellerDB import SellerDB
from database.MenuDB import MenuDB

class RegisterSeller:
    """
    This class deals with registering the seller
    """
    def on_post(self, req, resp):
        """Handles GET requests"""
        
        #get seller object from request
        sellerObject = json.loads(req.stream.read())
        print "received seller data" , sellerObject
        
        #database object
        sellerdb = SellerDB()
        
        #initialize return values
        sellerId = ""
        status = 1
        message = ""
        
        #extract values from seller object
        emailAddress = sellerObject["emailAddress"]
        print emailAddress
        mobileNumber = sellerObject["mobileNumber"]
        print mobileNumber
        
        #check if email is already registered
        emailCheck = sellerdb.checkEmailPresent(emailAddress)
        if emailCheck:
            #check if mobile number is already registered
            mobileCheck = sellerdb.checkMobilePresent(mobileNumber)
            if mobileCheck:
                #add seller detail to database and return seller id
                sellerObject["verifiedStatus"] = False
                sellerId = sellerdb.addSeller(sellerObject)
                print "sellerId", sellerId
                
            else:
                status = 0
                message = "Mobile number already exists."
        else:
            status = 0
            message = "Email already exists."
        
        #fill response object
        response = {
            'status': status,
            'errorMessage': message,
            'sellerId' : str(sellerId)
        }
        
        #add response object to return variable
        resp.body = json.dumps(response)


class LoginSeller:
    """
    This class deals with login the seller
    """
    def on_post(self, req, resp):
        """Handles GET requests"""
        
        #get seller object from request
        sellerObject = json.loads(req.stream.read())
        print "received seller data" , sellerObject
        
        #database object
        sellerdb = SellerDB()
        
        #initialize return values
        sellerId = ""
        status = 1
        message = ""
        
        #extract values from seller object
        emailAddress = sellerObject["emailAddress"]
        print emailAddress
        mobileNumber = int(sellerObject["mobileNumber"])
        print mobileNumber
        password = sellerObject["password"]
        print password
        
        #check if mobile number is entered
        if mobileNumber > 0:
            #get password for mobile number
            actualPassword, sellerId = sellerdb.getPasswordMobile(mobileNumber)
            if actualPassword != password:
                status = 0
                message = "The mobile number or password entered is wrong."
        else:
            #get password for mobile number
            actualPassword, sellerId = sellerdb.getPasswordEmail(emailAddress)
            if actualPassword != password:
                status = 0
                message = "The email address or password entered is wrong."
        
        #fill response object
        response = {
            'status': status,
            'errorMessage': message,
            'sellerId' : str(sellerId)
        }
        
        #add response object to return variable
        resp.body = json.dumps(response)
        
        
class GetVerificationStatus:
    def on_post(self, req, resp):
        """Handles GET requests"""
        
        #get seller object from request
        sellerObject = json.loads(req.stream.read())
        print "received seller data" , sellerObject
        
        #database object
        sellerdb = SellerDB()
        
        #initialize return values
        status = 1
        message = ""
        
        #extract values from seller object
        sellerId = sellerObject["sellerId"]
        
        data = sellerdb.getVerifiedStatus(sellerId)
        
        #fill response object
        response = {
            'status': status,
            'errorMessage': message,
            'data' : data
        }
        
        #add response object to return variable
        resp.body = json.dumps(response)
        
        
class GetSellerProfile:
    
    
    pass

class UpdateSellerProfile:
    
    pass