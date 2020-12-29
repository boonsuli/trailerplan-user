from datetime import date
import dataclasses
import orjson


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
