 
 
import falcon
import json
from controller.SellerController import RegisterSeller, LoginSeller,\
    GetVerificationStatus
from controller.StateController import AddState, GetStates
from controller.LocationController import GetLocations, AddArea
from controller.CatalogueController import GetAllCategories, GetAllDishes,\
    GetIngredients, GetAllIngredients, GetBoxTypes, GetDishesByType
from controller.MenuController import SetSellerMenu, GetSellerMenu, SetDishPhoto,\
    GetDishPhoto, SetDishDescription, GetDishDescription
 
class HomePage(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.content_type = 'text/html'
        with open('index.html', 'r') as f:  
            resp.body = f.read()

class JqueryLoad(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.content_type = 'text/html'
        with open('jquery-3.2.1.js', 'r') as f:
            resp.body = f.read()


api = falcon.API()
api.add_route('/', HomePage())
api.add_route('/js', JqueryLoad())

api.add_route('/registerSeller', RegisterSeller())
api.add_route('/loginSeller', LoginSeller())
api.add_route('/getVerificationStatus', GetVerificationStatus())

api.add_route('/addState', AddState())
api.add_route('/getAllStates', GetStates())
api.add_route('/getAllLocations', GetLocations())
api.add_route('/addArea', AddArea())

api.add_route('/getAllCategories', GetAllCategories())
api.add_route('/getAllDishes', GetAllDishes())
api.add_route('/getIngredients', GetIngredients())
api.add_route('/getAllIngredients', GetAllIngredients())
api.add_route('/getBoxTypes', GetBoxTypes())
api.add_route('/getDishesByType', GetDishesByType())

api.add_route('/setSellerMenu', SetSellerMenu())
api.add_route('/getSellerMenu', GetSellerMenu())
api.add_route('/setDishPhoto', SetDishPhoto())
api.add_route('/getDishPhoto', GetDishPhoto())
api.add_route('/setDishDescription', SetDishDescription())
api.add_route('/getDishDescription', GetDishDescription())