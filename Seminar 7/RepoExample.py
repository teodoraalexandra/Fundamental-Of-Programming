'''
Created on Nov 12, 2016

@author: Arthur
'''




def repo_test():
    carRepo = Repository()
    clientRepo = Repository()
    
    carRepo.store(Car(1, "AB 01 RTY", "Mazda", "CX-3"))
    carRepo.store(Car(2, "NT 99 PUX", "Dacia", "Dokker"))
    assert len(carRepo) == 2

    carRepo.delete(1)
    assert len(carRepo) == 2
    
    try:
        carRepo.delete(1)
        assert False
    except Exception:
        pass
    
    
    clientRepo.store(Client(1001, "2850369887452", "Maria Popescu"))
    clientRepo.store(Client(1002, "2880365882446", "Ion Andone"))
    assert len(clientRepo) == 2
    
    '''
    Not a test, just showing off :)
    '''
    print("This is our car repo:")
    print(carRepo)
    
    print("This is our client repo:")
    print(clientRepo)
 
 
repo_test()