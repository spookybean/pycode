from enum import Enum

class UserStatus(Enum):
    ACTIVE = 1
    INACTIVE = 0
    DELETED = -1


class User:
    def __init__(self, name, status):
        self.name = name
        self.status = status
    
    def __str__(self):
        return str(dict(name=self.name, status=self.status))


user1 = User('John', UserStatus.ACTIVE.value)
user2 = User('Jane', UserStatus.INACTIVE.value)
user3 = User('Jane', UserStatus.DELETED.value)
user4 = User('Jane', UserStatus.INACTIVE.value)

print(user1)
print(user2)
print(user3)
print(user4)