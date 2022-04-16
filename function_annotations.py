def func(a: str='a', b: str='b') -> dict:
    return {'a': a, 'b': b}


if __name__ == '__main__':
    func('c', 'd')
    print(func())