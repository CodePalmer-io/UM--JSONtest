import json
import urllib.request
import urllib.error

# URL = 'http://py4e-data.dr-chuck.net/comments_42.json'
URL = 'http://py4e-data.dr-chuck.net/comments_1136303.json'

print('Retrieving', URL)                    # Prints the URL
address = urllib.request.urlopen(URL)       # Opens a connection to URL
data = address.read().decode()              # read the data and converts to unicode for python
print('Retrieved', len(data), 'characters') # counting the length of data

info = json.loads(data)                     # Creates a JSON object from data
info = info["comments"]                     # points at the comments key of the object

total = 0                                   # total accumulation of value['count']
count = 0                                   # the number of occurrence of key['count']

for item in info:                           # iterate through the info object
    count += 1                              # increment count for occurrence
    total += int(item["count"])             # accumulation of sum (parse value as int, as initially its a string)

print("Count: ", count)                     # print count
print("Sum: ", total)                       # print total
