from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identify
from user import UserRegister
from item import Item, ItemList


app = Flask(__name__)
api = Api(app)
app.secret_key = 'alex'

jwt = JWT(app, authenticate, identify)


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

if __name__ == "__main__":
    app.run(port=5000, debug=True)