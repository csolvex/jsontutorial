import json

numbers = [2,3,5,7,11,13,21,88,23,24,27,45]

filename = 'numbers.json'
with open(filename) as f_obj:
    numbas = json.load(f_obj)
for i in numbas:
    print (i)
    




