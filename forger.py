import json
import sys

# print(f"Argv[0]: {sys.argv[1]}")

f = open(sys.argv[1])
g = open(sys.argv[2])

data = json.load(f)
template = json.load(g)
# entry = open(data['character']['name'].json, "w") 
entry = open("test.json", "w")

# print("CHARACTER")
# for i in data['character']:
#     print(i)

# print(data["character"]["attribs"][0]['name'])

template["img"] = data["avatar"]
template["token"]["img"] = data["avatar"]
print("Avatar Forged\nToken Forged")

for i in data['attribs']:
    # print(f"{i['name']}: {i['current']}")
    if i["name"] == "name":
        template["name"] = i["current"]
        template["token"]["name"] = i["current"]
        print("Name Forged")
    
    # Attributes
    if i["name"] == "strength":
        template["data"]["attributes"]["strength"]["value"] = i["current"]
        print("Strength Forged")
    if i["name"] == "agility":
        template["data"]["attributes"]["agility"]["value"] = i["current"]
        print("Agility Forged")
    if i["name"] == "intellect":
        template["data"]["attributes"]["intellect"]["value"] = i["current"]
        print("Intellect Forged")
    if i["name"] == "will":
        template["data"]["attributes"]["will"]["value"] = i["current"]
        print("Will Forged")
    if i["name"] == "perception":
        template["data"]["attributes"]["perception"]["value"] = i["current"]
        print("Perception Forged")

    # Characteristics
    if i["name"] == "damage":
        template["data"]["characteristics"]["health"]["max"] = i["max"]
        print("Health/Damage Forged")
    if i["name"] == "defense":
        template["data"]["characteristics"]["defense"] = i["current"]
        print("Defense Forged")
    if i["name"] == "size":
        template["data"]["characteristics"]["size"] = i["current"]
        print("Size Forged")
    if i["name"] == "speed_display":
        template["data"]["characteristics"]["speed"] = i["current"]
        print("Speed Forged")
    if i["name"] == "power":
        template["data"]["characteristics"]["power"] = i["current"]
        print("Power Forged")
    if i["name"] == "insanity":
        template["data"]["characteristics"]["insanity"] = i["current"]
        print("Insanity Forged")
    if i["name"] == "corruption":
        template["data"]["characteristics"]["corruption"] = i["current"]
        print("Corruption Forged")

#print(f"Entry Name: {entry_name}")
datadump = json.dumps(template, indent=4)
entry.write(datadump)
entry.close()
    

