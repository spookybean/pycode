from hashlib import sha256


x = 'some string'

hash = sha256(x.encode('utf-8')).hexdigest()

print(hash)