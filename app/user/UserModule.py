import dataclasses
import logging
from datetime import date

import orjson
from flask import Flask, abort, make_response, request
from flask_api import status
from flask_restx import Api, Resource

from app.user.UserDao import UserDao
from app.user.UserModel import User

app = Flask(__name__)
app.config.update(
    DEBUG=True,
    TESTING=True,
    LOGGER_NAME='TrailerPlanLog'
)
api = Api(app)
nameSpace = api.namespace('trailerplan/api/v1.1/users', description='TrailerPlan User API')


FORMAT = '%(asctime)-15s %(message)s'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger('TrailerPlanApiLogger')
logger.setLevel(logging.DEBUG)


@nameSpace.route("/")
class UserCollectionController(Resource):

    def get(self):
        """ Retrieve all users """
        users = UserDao(data).getUsers()
        logger.debug('List of users : ' + orjson.dumps(users).decode("utf-8"))
        return getResponseHttp(users)

    @api.response(201, 'User successfully created')
    def post(self):
        """ Create a user """
        trailer_str = orjson.loads(request.data) if request.data else abort(status.HTTP_400_BAD_REQUEST)
        dao = UserDao(data)
        trailer_obj = dao.create(trailer_str)
        logger.debug(orjson.dumps(trailer_obj).decode("utf-8"))
        return getResponseHttp(trailer_obj)


@nameSpace.route("/<int:id>")
@api.response(404, 'User not found.')
class UserItemController(Resource):

    def get(self, id):
        """ Retrieve a user by id """
        dao = UserDao(data)
        trailer2display = dao.get(id) if dao.getLength() > id else abort(404)
        logger.debug('User requested : ' + orjson.dumps(trailer2display).decode("utf-8"))
        return getResponseHttp(trailer2display)

    @api.response(204, 'User successfully updated.')
    def put(self, id):
        """ Update a user by id """
        trailer_obj = orjson.loads(request.data) if request.data else abort(status.HTTP_400_BAD_REQUEST)
        dao = UserDao(data)
        dao.update(id, trailer_obj)
        logger.debug(orjson.dumps(trailer_obj).decode("utf-8"))
        return None, 204

    @api.response(204, 'User successfully deleted')
    def delete(self, id):
        """ Delete a user by id """
        dao = UserDao(data)
        trailer_obj = data.pop(id) if 0 < id < dao.getLength() else abort(status.HTTP_400_BAD_REQUEST)
        logger.debug(orjson.dumps(trailer_obj).decode("utf-8"))
        return None, 204


def getResponseHttp(obj2dump):
    response = make_response(orjson.dumps(obj2dump).decode("utf-8"))
    response.headers['Content-Type'] = 'application/json'
    return response


@dataclasses.dataclass
class UserPopulate(object):
    def initialisationData(data):
        data.append(User(0, None, 'Kilian', 'Jornet', 'masculin', date.fromisoformat('1987-10-27'), 'Sabadell', 'Espagne'))
        data.append(User(1, None, 'Sebastien', 'Chaigneau', 'masculin', date.fromisoformat('1972-02-23'), 'Châtellerault', 'France'))
        data.append(User(2, 'Madame', 'Caroline', 'Chaverot', 'féminin', date.fromisoformat('1976-10-16'), 'Genève', 'Suisse'))
        data.append(User(3, None, 'Eric', 'Clavery', 'masculin', date.fromisoformat('1980-06-07'), 'Coutances', 'France'))
        data.append(User(4, None, 'François', 'Delabarre', 'masculin', date.fromisoformat('1968-01-03'), 'Lille', 'France'))
        data.append(User(5, 'Madame', 'Corinne', 'Favre', 'féminin', date.fromisoformat('1970-12-15'), 'Chambéry', 'France'))
        data.append(User(6, 'Madame', 'Emilie', 'Forsberg', 'féminin', date.fromisoformat('1986-12-11'), 'Sollefteå', 'Suède'))
        data.append(User(7, 'Madame', 'Anna', 'Frost', 'féminin', date.fromisoformat('1981-11-01'), 'Dunedin', 'Nouvelle-Zélande'))
        data.append(User(8, 'Madame', 'Maud', 'Gobert', 'féminin', date.fromisoformat('1977-04-25'), None, 'France'))
        data.append(User(9, None, 'Antoine', 'Guillon', 'masculin', date.fromisoformat('1970-06-16'), 'Yvelines', 'France'))
        data.append(User(10, None, 'Scott', 'Jurek', 'masculin', date.fromisoformat('1973-10-26'), 'Duluth', 'Etats-Unis'))
        data.append(User(11, None, 'Anton', 'Krupicka', 'masculin', date.fromisoformat('1983-08-08'), 'Nebraska', 'Etats-Unis'))
        data.append(User(12, 'Madame', 'Nathalie', 'Mauclair', 'féminin', date.fromisoformat('1970-05-09'), None, 'France'))
        data.append(User(13, None, 'Dawa', 'Dachhiri Sherpa', 'masculin', date.fromisoformat('1969-11-03'), 'Taksindu Solukumbu', 'Népal'))
        data.append(User(14, None, 'Xavier', 'Thévenard', 'masculin', date.fromisoformat('1988-03-06'), 'Nantua', 'France'))
        return data


data = []
if __name__ == '__main__':
    UserPopulate.initialisationData(data)
    app.run(host='0.0.0.0', port=int("5000"), debug=True)