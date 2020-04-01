class Repository:
    """
    Repository for storing domain objects
    """
    def __init__(self):
        self._objects = []

    def store(self, obj):
        if self.find(obj.id) != None:
            raise RepositoryException("Object having id= " + str(obj.id) + " already in repo!")

        self._objects.append(obj)

    def update(self, object):
        pass

    def find(self, objectId):
        for obj in self._objects:
            if objectId == obj.id:
                return obj
        return None

    def delete(self, objectId):
        pass
    
    def getAll(self):
        return self._objects

    def __len__(self):
        return len(self._objects)

    def __str__(self):
        r = ""
        for e in self._objects:
            r += str(e)
            r += "\n"
        return r
