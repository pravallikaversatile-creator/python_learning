import json

with open("info.json") as f:
    data=json.load(f) #Python parsing the json file
    print(f"Printing json file contents: {data}")
    print("Printing keys of the json file: ")
    for k in data:
        print(k)
    print(f"Printing Designation of the Employee: {data['Designation']}")

#Modify Json
data["Designation"]="Manager"


#Updating in the same JSON file
with open("info.json","r+") as f1:
    f1.seek(0)
    json.dump(data, f1, indent=4)
    f1.truncate()

""" #Opening a new JSON file to write
with open("updated_info.json","w") as f1:
    json.dump(data, f1, indent=4)

#Read again to Verify
with open("updated_info.json") as f2:
    updated=json.load(f2)
    print(f"Printing the contents of json file after updating: {updated}")
"""
