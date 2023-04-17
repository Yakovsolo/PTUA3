import json

data = """{
  "student": [ 

     { 
        "id":"01", 
        "name": "Tom", 
        "lastname": "Price"
        "age": 18, 
        "status": null, 
        "alive": true 
     }, 

     { 
        "id":"02", 
        "name": "Nick", 
        "lastname": "Thameson" 
     } 
  ]   
}"""

data_dict = json.loads(data)
print(data_dict)
print(type(data_dict))

data_dict["student"][1]["name"] = "Kyle"
for student in data_dict["student"]:
    student.update({"gender": "male"})
print(data_dict)

# {'student': [{'id': '01', 'name': 'Tom', 'lastname': 'Price', 'gender': 'male'},
# {'id': '02', 'name': 'Kyle', 'lastname': 'Thameson', 'gender': 'male'}]}

new_json = json.dumps(data_dict, indent=2)
print(new_json)

# {
#   "student": [
#     {
#       "id": "01",
#       "name": "Tom",
#       "lastname": "Price",
#       "gender": "male"
#     },
#     {
#       "id": "02",
#       "name": "Kyle",
#       "lastname": "Thameson",
#       "gender": "male"
#     }
#   ]
# }

with open("example2.json", "w") as file:
    json.dump(data, file, indent=2, sort_keys=True)

with open("example2.json", "r") as file:
    data = json.load(file)

print(data)

# [{'id': '0001', 'type': 'donut', 'name': 'Cake', 'ppu': 0.55, 'batters': {'batter': [{'id': '1001', 'type': 'Regular'},
#  {'id': '1002', 'type': 'Chocolate'}, {'id': '1003', 'type': 'Blueberry'}, {'id': '1004', 'type': "Devil's Food"}]},
# 'topping': [{'id': '5001', 'type': 'None'}, {'id': '5002', 'type': 'Glazed'}, {'id': '5005', 'type': 'Sugar'},
# {'id': '5007', 'type': 'Powdered Sugar'}, {'id': '5006', 'type': 'Chocolate with Sprinkles'}, {'id': '5003', 'type': 'Chocolate'},
# {'id': '5004', 'type': 'Maple'}]}, {'id': '0002', 'type': 'donut', 'name': 'Raised', 'ppu': 0.55, 'batters':
# {'batter': [{'id': '1001', 'type': 'Regular'}]}, 'topping': [{'id': '5001', 'type': 'None'}, {'id': '5002', 'type': 'Glazed'},
# {'id': '5005', 'type': 'Sugar'}, {'id': '5003', 'type': 'Chocolate'}, {'id': '5004', 'type': 'Maple'}]}, {'id': '0003', 'type':
# 'donut', 'name': 'Old Fashioned', 'ppu': 0.55, 'batters': {'batter': [{'id': '1001', 'type': 'Regular'}, {'id': '1002', 'type':
# 'Chocolate'}]}, 'topping': [{'id': '5001', 'type': 'None'}, {'id': '5002', 'type': 'Glazed'}, {'id': '5003', 'type': 'Chocolate'},
# {'id': '5004', 'type': 'Maple'}]}]
