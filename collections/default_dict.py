from collections import defaultdict

default = defaultdict(bool)

default['name'] = 'abc'

print(default['name'])
print(f'default value for bool: {default["address"]}')