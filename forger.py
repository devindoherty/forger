import json
import sys
import string

# print(f"Argv[0]: {sys.argv[1]}")

f = open(sys.argv[1])
g = open(sys.argv[2])
data = json.load(f)
template = json.load(g)
filename = "forger_" + data["name"].lower() + ".json"
# entry = open(data['character']['name'].json, "w") 
entry = open(filename, "w")

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
        template["data"]["characteristics"]["insanity"]["value"] = i["current"]
        print("Insanity Forged")
    if i["name"] == "corruption":
        template["data"]["characteristics"]["corruption"] = i["current"]
        print("Corruption Forged")

    # Traits

    if "repeating_npctraits" and "npctrait_name" in i["name"]:
        start = i["name"].index('-')
        end = i["name"].index('_', start+1)
        feature_id = i["name"][start+1:end]
        print(f"{i['current']} Feature Found\nFeature ID: {feature_id}")
        template["items"].append(
            {
                "_id": feature_id,
                "name": i['current'],
                "type": "feature",
                "img": "icons/containers/bags/sack-cloth-tan.webp",
                "data": {
                    "description": ""
                  },
                "effects": [],
                "folder": "null",
                "sort": 0,
                "permission": {
                    "default": 0,
                    "KW6XDTTvkV8qWXT9": 3
                },
                "flags": {}
        })
    
    if "npctrait_description" in i["name"]:
        start = i["name"].index('-')
        end = i["name"].index('_', start+1)
        feature_id = i["name"][start+1:end]
        for j in template["items"]:
            if j["_id"] == feature_id:
                j["data"]["description"] = i["current"]
    
    

    # Special Actions
    if "repeating_specialactions" and "specialaction_name" in i["name"]:
        print(f"{i['current']} Special Action Found")
    
    # Attacks
    if "repeating_attacks" and "attack_name" in i["name"]:
        start = i["name"].index('-')
        end = i["name"].index('_', start+1)
        feature_id = i["name"][start+1:end]
        print(f"{i['current']} Weapon Found\nWeapon ID: {feature_id}")
        template["items"].append(
            {
                "_id": feature_id,
                "name": i["current"],
                "type": "weapon",
                "img": "systems/demonlord/assets/icons/weapons/swords/sword11.webp",
                "data": {
                    "description": "",
                    "action": {
                        "active": "true",
                        "attack": "",
                        "against": "",
                        "damageactive": "",
                        "damage": "",
                        "damagetype": "",
                        "boonsbanesactive": "",
                        "boonsbanes": "",
                        "plus20active": "",
                        "plus20": "",
                        "plus20damage": "",
                        "defense": "",
                        "defenseboonsbanes": "",
                        "damagetypes": [],
                        "strengthboonsbanesselect": "false",
                        "agilityboonsbanesselect": "false",
                        "intellectboonsbanesselect": "false",
                        "willboonsbanesselect": "false",
                        "perceptionboonsbanesselect": "false",
                        "extraeffect": "",
                        },
                "activatedEffect": {
                    "activation": {
                        "type": "",
                        "cost": 0
                    },
                    "duration": {
                        "value": 0,
                        "type": ""
                    },
                    "target": {
                        "value": "",
                        "type": ""
                    },
                    "texture": "",
                    "range": "",
                    "uses": {
                        "value": 0,
                        "max": 0,
                        "per": "null"
                    }
                    },
                    "enchantment": {
                    "attackbonus": 0,
                    "challengebonus": 0,
                    "damage": "",
                    "defense": 0,
                    "speed": 0,
                    "perception": 0,
                    "effect": "",
                    "uses": {
                        "value": 0,
                        "max": 0
                    }
                    },
                    "hands": "",
                    "properties": "",
                    "strengthmin": "",
                    "wear": "true",
                    "quantity": 1,
                    "availability": "C",
                    "value": ""
                },
                "effects": [],
                "folder": "null",
                "sort": 0,
                "permission": {
                    "default": 0,
                    "KW6XDTTvkV8qWXT9": 3
                },
                "flags": {}
            })
    
# def id_finder(start, end)

#print(f"Entry Name: {entry_name}")
datadump = json.dumps(template, indent=4)
entry.write(datadump)
entry.close()


