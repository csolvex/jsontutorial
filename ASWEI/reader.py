import json
#from pprint import pprint

with open('quotes.json', 'r') as f:
     data = json.load(f)
     print (data)
     #pprint (data)
   
         