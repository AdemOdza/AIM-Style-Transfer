import pickle

filename='model.pkl'
knn = {}
pickle.dump(knn, open(filename, 'wb'))