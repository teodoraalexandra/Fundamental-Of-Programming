import pickle

l = []
f = open("grades.pickle", "wb")
pickle.dump(l,f)
f.close()