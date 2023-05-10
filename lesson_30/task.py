import json

with open("task.json", "r") as file:
    data = json.load(file)

print(data)

# {
#   "colors": [
#     {
#       "color": "black",
#       "rgb": "255, 255, 255",
#       "hex": "#000"
#     },
#     {
#       "color": "white",
#       "rgb": "0, 0, 0",
#       "hex": "#FFF"
#     }

# =============================================================================================================

# {
#   "colors": [
#     {
#       "color": "black",
#       "category": "hue",
#       "type": "primary",
#       "code": {
#         "rgba": [
#           255,
#           255,
#           255,
#           1
#         ],
#         "hex": "#000"
#       }

list_of_colours = []
for item in data["colors"]:
    new_format = {}
    color = item["color"]
    rgba_list = item["code"]["rgba"][:-1]
    rgb = ", ".join([str(x) for x in rgba_list])
    hexx = item["code"]["hex"]
    new_format.update({"color": color, "rgb": rgb, "hex": hexx})
    list_of_colours.append(new_format)


new_dict = {"colors": list_of_colours}

with open("task_result.json", "w") as file:
    json.dump(new_dict, file, indent=2)
