from flask import Flask
from flask_restful import abort, fields, marshal_with, reqparse, Resource, Api
from models import AccountModel
from database import Database
import status

#data we want to render to messageModel class (JSON representation)
account_fields = {
    'id': fields.Integer,
    'uri': fields.Url('message_endpoint'),
    'type': fields.String,
    'number': fields.String,
    'name': fields.String,
    'first_name': fields.String,
    'address': fields.String,
    'birthdate': fields.String,
    'longitude': fields.Float,
    'latitude': fields.Float,
}

class Account(Resource):
    def abort_if_account_doesnt_exist(self, id):
        if len(db.get(id)) == 0:
            abort(
                status.HTTP_404_NOT_FOUND,
                message="Account {0} doesn't exist".format(id))

    @marshal_with(account_fields)
    def get(self, id):
        self.abort_if_account_doesnt_exist(id)
        return db.get(id)

    def delete(self, id):
        self.abort_if_account_doesnt_exist(id)
        db.delete(id)
        return '', status.HTTP_204_NO_CONTENT

    @marshal_with(account_fields)
    def put(self, id):
        self.abort_if_account_doesnt_exist(id)
        account = AccountModel.fromData(db.get(id))
        print(account.name)
        parser = reqparse.RequestParser()
        parser.add_argument('type', type=str)
        parser.add_argument('number', type=str)
        parser.add_argument('name', type=str)
        parser.add_argument('first_name', type=str)
        parser.add_argument('address', type=str)
        parser.add_argument('birthdate', type=str)
        args = parser.parse_args()
        if 'type' in args and args['type'] != None:
            account.type = args['type']
        if 'number' in args and args['number'] != None:
            account.number = args['number']
        if 'name' in args and args['name'] != None:
            account.name = args['name']
        if 'first_name' in args and args['first_name'] != None:
            account.first_name = args['first_name']
        if 'address' in args and args['address'] != None:
            account.address = args['address']
        if 'birthdate' in args and args['birthdate'] != None:
            account.birthdate = args['birthdate']
        db.put(id, account.type, account.number, account.name, account.first_name, account.address, account.birthdate,
               account.latitude, account.longitude)
        return account


class AccountList(Resource):
    @marshal_with(account_fields)
    def get(self):
        return [v for v in db.view()]
        #return [v for v in account_manager.accounts.values()]

    @marshal_with(account_fields)
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('type', type=str, required=True, help='Account type cannot be blank!')
        parser.add_argument('number', type=str, required=True, help='Account number cannot be blank!')
        parser.add_argument('name', type=str, required=True, help='User Name cannot be blank!')
        parser.add_argument('first_name', type=str, required=True, help='User Fist Name cannot be blank!')
        parser.add_argument('address', type=str, required=True, help='User address cannot be blank!')
        parser.add_argument('birthdate', type=str, required=True, help='User birthdate cannot be blank!')
        args = parser.parse_args()
        account = AccountModel(
            account_type = args['type'],
            account_number = args['number'],
            name = args['name'],
            first_name = args['first_name'],
            address = args['address'],
            birthdate = args['birthdate'],
            )
        account.id = db.get_max_id()+1
        db.post(account.type, account.number, account.name, account.first_name, account.address, account.birthdate,
                account.latitude, account.longitude)
        return account, status.HTTP_201_CREATED

db = Database("accounts.db")
app = Flask(__name__)
api = Api(app)
api.add_resource(AccountList, '/api/accounts/')
api.add_resource(Account, '/api/accounts/<int:id>', endpoint='message_endpoint')

if __name__ == '__main__':
    app.run(debug=True)