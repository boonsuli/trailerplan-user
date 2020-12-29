from datetime import date
from munch import DefaultMunch
import dataclasses

from app.user.UserModel import User


@dataclasses.dataclass
class UserDao(object):
    def __init__(self, pData):
        self.users = pData

    def getUsers(self):
        return self.users

    def setUsers(self, users):
        self.users = users

    def get(self, idx):
        # userFinded should be find in a easiest way, it is just to show an example of list comprehension
        userFinded = [usr2 for usr2 in self.users if usr2.id == idx]
        return userFinded[0] or None

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
