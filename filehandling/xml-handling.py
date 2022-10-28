
from xml.dom import minidom


file = minidom.parse('models.xml')
models = file.getElementsByTagName('model')

print(models[0].attributes['name'].value)
print(models[1].firstChild.data)
print(models[1].childNodes[0].data)
