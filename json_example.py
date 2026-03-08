import json
import os

current_dir = os.getcwd()
json_file_path = current_dir + "/json_file.json"

data = {
    "name" : "Konpal",
    "skills" : [".NET", "Python"]
}

with open(json_file_path, "w") as f:
    json.dump(data, f, indent=2)

# read json file data

with open(json_file_path, "r") as f:
    loaded_data = json.load(f)
    print(loaded_data["name"])