import pickle

'''Pickle is used to pack data,
a kind of Data management/ Database'''

cars = ['Audi', 'BMW', 'Lamborghini', 'Mercedes', 'Bugati', 'Ferrari']

# Pickling a python list/object
with open('mycar.pkl', 'wb') as fileObj:
    pickle.dump(cars, fileObj)

with open('mycar.pkl', 'rb') as fileObj:
    myCar = pickle.load(fileObj)

print(myCar)