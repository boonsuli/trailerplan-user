from flask import Flask, abort, make_response, request
from flask_api import status
from datetime import date
from flask_restx import Api, Resource
from munch import DefaultMunch
import dataclasses
import logging
import orjson


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


def default(obj):
    if isinstance(obj, ShortAddress):
        return obj.toJson()
    raise TypeError


@dataclasses.dataclass
class Object(object):
    """oject model"""
    def toJson(self):
        return orjson.dumps(self.__dict__, default=default).decode("utf-8")


@dataclasses.dataclass
class AbstractClass(Object):
    """abstract object model"""
    def __init__(self):
        self.creationDate = date.day, self.modificationDate = date.day


@dataclasses.dataclass
class ShortAddress(AbstractClass):
    """object model of an short address"""
    def __init__(self, pId=-1, city='Paris', country='France'):
        self.id, self.city, self.country = pId, city, country

    def toString(self):
        str2return = '' if self.city is None else "à {0} ".format(self.city)
        str2return += "en {0}".format(self.country)
        return str2return


@dataclasses.dataclass
class Address(ShortAddress):
    """object model of an address"""
    def __init__(self, pId=-1, num=1, typeVoie='rue', voie='de la Paix', zipCode='75009'):
        ShortAddress.__init__(self)
        self.id, self.num, self.typeVoie, self.libelleVoie, self.zipCode = pId, num, typeVoie, voie, zipCode

    def toString(self):
        return "{0} {1} {2} {3}".format(self.num, self.typeVoie, self.libelleVoie, self.zipCode)


@dataclasses.dataclass
class User(AbstractClass):
    """object model of an user"""
    def __init__(self, pId=-1, civility=None, firstName='', lastName='', sexe='', birthday=date.today(), city='', country=''):
        self.id, self.firstName, self.lastName, self.sexe, self.birthday = \
            pId, firstName, lastName, sexe, birthday
        self.address = ShortAddress(self.id, city, country)
        self.civility = 'Monsieur' if civility is None else civility

    def setAddress(self, adresse):
        self.address = adresse

    def toString(self):
        str2return = "{0} {1} {2} né le {3} {4}" \
            .format(self.firstName, self.lastName.upper(), self.sexe, self.birthday, self.address.toString())
        return str2return


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


@dataclasses.dataclass
class UserDao(object):
    def __init__(self, pData):
        self.users = pData

    def getUsers(self):
        return self.users

    def setUsers(self, users):
        self.users = users

    def get(self, idx):
        # usrFinded should be find in a easiest way, it is just to show an example of list comprehension
        usrFinded = [usr2 for usr2 in self.users if usr2.id == idx]
        return usrFinded[0] or None

    def create(self, trailer_str):
        trailer_obj = DefaultMunch.fromDict(trailer_str, User())
        trailer_obj['id'] = self.users.__len__()
        trailer_obj.adresse['id'] = self.users.__len__()
        trailer_obj['birthday'] = date.fromisoformat(trailer_obj['birthday'])
        usr_obj = trailer_obj

        self.users.append(usr_obj)
        return usr_obj

    def update(self, id, usr2update):
        trailer_obj = DefaultMunch.fromDict(usr2update, User())
        self.users[id] = trailer_obj
        return usr2update

    def delete(self, id):
        usr2delete = self.get(id)
        self.users.remove(usr2delete)

    def getLength(self):
        return self.users.__len__()


data = []
if __name__ == '__main__':
    UserPopulate.initialisationData(data)
    app.run(host='0.0.0.0', port=int("5000"), debug=True)