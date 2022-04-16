from datetime import date
from pprint import pprint
from marshmallow import Schema, fields, ValidationError


class ArtistSchema(Schema):
    name = fields.Str()


class AlbumSchema(Schema):
    title = fields.Str()
    release_date = fields.Date()
    artist = fields.Nested(ArtistSchema())


bowie = dict(name="David Bowie")
album = dict(artist=bowie, title="Hunky Dory", release_date=date(1971, 12, 17))

schema = AlbumSchema()
result = schema.dump(album)

data = {
    'artist': {'name': 'David Bowie'},
    'title': '10',
    'release_date': '1971-12-17'
}

try:
    input_data = schema.load(data)
except ValidationError:
    print('invalid data')
else:
    print('valid data')
    pprint(input_data, indent=2)