import xml.etree.cElementTree as ET
from xml.dom import minidom
import random
import uuid
from faker import Faker

def make_fake_data():
    fake = Faker()

    out = {
        "id": str(uuid.uuid4()),
        "name": fake.first_name(),
        "last_name": fake.last_name(),
        "age": random.randint(18, 99)
    }
    return out

data = [make_fake_data() for i in range(1000)]

# data = [
#     {'id' : 1, 'name' : 'jim', 'last_name': 'jones', 'age': 22},
#     {'id' : 2, 'name' : 'jack', 'last_name': 'douglas', 'age': 23},
#     {'id' : 3, 'name' : 'sam', 'last_name': 'jackson', 'age': 24},
#     {'id' : 4, 'name' : 'ralph', 'last_name': 'smith', 'age': 25}
#         ]


xml = ET.Element("data")

for value in data:
    id = ET.SubElement(xml, "id")
    name = ET.SubElement(id, "name")
    last_name = ET.SubElement(id, "last_name")
    age = ET.SubElement(id, "age")

    id.text = str(value['id'])
    name.text = str(value['name'])
    last_name.text = str(value['last_name'])
    age.text = str(value['age'])

tree = ET.ElementTree(xml)

xmlstr = minidom.parseString(ET.tostring(xml)).toprettyxml(indent="   ")
with open("New_Database.xml", "w") as f:
    f.write(xmlstr)

#tree.write('data.xml')