from typing import List, Optional
from datetime import datetime
from pydantic import (
    BaseModel,
    EmailStr,
    ValidationError,
    PositiveInt,
    NegativeInt,
    conlist,
    constr,
    validator
    )


class User(BaseModel):
    id: PositiveInt
    username: constr(
        min_length=4,
        max_length=8,
        strip_whitespace=True,
        regex='^[A-Za-z]+$'
        )
    password: constr(min_length=4, max_length=8, strip_whitespace=True)
    confirm_password: constr(min_length=4, max_length=8, strip_whitespace=True)
    alias: Optional[constr(
        min_length=4,
        max_length=8,
        strip_whitespace=True,
        regex='^[A-Za-z]+$')] = 'anonymous'
    email: EmailStr
    timestamp: Optional[datetime] = datetime.utcnow()
    friends: List[int] = []
    best_friends: conlist(PositiveInt, min_items=1, max_items=4)
    strip_str: Optional[constr(min_length=4, max_length=8, strip_whitespace=True)]


    @validator('confirm_password')
    def passwords_match(cls, v, values, **kwargs):
        if 'password' in values and v != values['password']:
            raise ValueError('passwords do not match')
        return v


data = {
    'id': '1',
    'username': ' waia',
    'password': 'abcd',
    'confirm_password': 'adfsdf ',
    'alias': 'lmao ',
    'timestamp': '2020-08-03 10:30',
    'friends': [1, '2', b'3'],
    'email': 'a@a.com',
    'strip_str': ' a asdf ',
    'best_friends': [1, 2, 3, 4]
}


try:
    user = User(**data)
except ValidationError as e:
    print(e)
else:
    print(user)