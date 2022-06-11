from functools import partial


int_map = partial(int, base=2)

a = ['01110011', '01101111', '01100011', '01101011', '01100101', '01110100']

string = ''.join([chr(i) for i in list(map(int_map, a))])

print(string)