import unittest
from seminar07.repository.Repository import Repository
from seminar07.domain.Client import Client
from seminar07.repository.RepositoryException import RepositoryException

class RepositoryTest(unittest.TestCase):
    '''
    Unit test case example for Repository
    '''
    def setUp(self):
        self._repo = Repository()
    
    def testRepo(self):
        self.assertEqual(len(self._repo), 0)
        z = Client("1", "1840101223366", "Anna")
        self._repo.store(z)
        self.assertEqual(len(self._repo), 1)
        self.assertRaises(RepositoryException , self._repo.store, z)
        
        z = Client("2", "1840101223366", "Anna")
        self._repo.store(z)
        self.assertEqual(len(self._repo), 2)
        '''
        And so on for the other Repository operations
        '''