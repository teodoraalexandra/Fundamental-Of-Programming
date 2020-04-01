class RepositoryError(Exception):
    def __init__(self, msg):
        self._msg = msg

    @property
    def message(self):
        return self._msg

import random

def test():
    i = random.randint(0, 2)
    if i == 0:
        raise ValueError('VE')
    elif i == 1:
        raise TypeError('TE')
    else:
        raise RepositoryError('RE')

def test2():
    test()

'''
for i in range(10):
    try:
        test2()
    except RepositoryError as ee:
        print('repo')
    except ValueError as ee:
        print('value')
    except Exception as ee:
        print('other exception')

'''