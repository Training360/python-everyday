from xml.dom import minidom
from os import path

file = minidom.parse(f'{path.dirname(__file__)}/models.xml')

# use getElementsByTagName() to get tag
models = file.getElementsByTagName('model')
print(models)

# # one specific item attribute
print('model #2 attribute:')
print(models[1].attributes['name'].value)

# # all item attributes
print('All attributes:')
for model in models:
    print(model.attributes['name'].value)

# # one specific item's data
print('model #2 data:')
print(models[1].firstChild.data)
print(models[1].childNodes[0].data)

# # all items data
print('All model data:')
for elem in models:
    print(elem.firstChild.data)
