class IterableStructure:
    def __init__(self):
        self.__data = []
        self.index = -1

    def __iter__(self):
        '''
        The iterator for the class
        '''
        return iter(self.__data)

    def __next__(self):
        '''
        A getter for the next element in the list
        '''
        if self.index > len(self.__data) - 1:
            raise StopIteration
        else:
            self.index += 1
        return self.__data[self.index]

    def __len__(self):
        '''
        Return the length of the list
        '''
        return len(self.__data)

    def __setitem__(self, index, val):
        '''
        Set a value for the list at a given index
        '''
        self.__data[index] = val

    def __getitem__(self, index):
        '''
        Get the item at a given index
        '''
        return self.__data[index]

    def __delitem__(self, index):
        '''
        Delete an element at a given index
        '''
        del self.__data[index]

    def append(self, x):
        self.__data.append(x)

    def remove(self, element):
        self.__data.remove(element)

    def clear(self):
        self.__data.clear()

    def getAll(self):
        return self.__data
