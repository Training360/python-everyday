from json import loads, dumps

user_json = '''{
    "firstName": "John",
    "lastName": "Smith",
    "phoneNumbers": [
        {
            "type": "home",
            "number": "212 555-1234"
        },
        {
            "type": "office",
            "number": "646 555-4567"
        }
    ]
}'''

# json to python code
user = loads(user_json)
print(type(user), user)
print(user['phoneNumbers'][0]['number'])

# to json
python_code = {'name': 'Gáll Gergely', 'age': 38}
print(type(dumps(python_code)))
