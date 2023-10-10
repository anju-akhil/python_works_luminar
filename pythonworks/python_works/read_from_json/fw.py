from json import load
path="C:\\Users\\HP\\Desktop\\pythonworks\\read_from_json\\data.json"
with open(path) as f:
    records=load(f) 
#print(records)

#-------------name printing-----------
fw_names=[f.get("name")for f in records]
print(fw_names)

#-----------top rated framework--------
top_framework=max(records,key=lambda d:d.get("rating"))
print("top rating=",top_framework)

#---------frontend framework names-----------
frontend_fr={f.get("name") for f in records if f.get("side")=="frontend"}
print("frontend=",frontend_fr)

#-----------python framework names------------
fr_name={f.get("name")for f in records}
print("framework=",fr_name)