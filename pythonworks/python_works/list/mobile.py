phones=[
    {
        "name":"m13","brand":"samsung","network":"5g","colors":["black","grey"],
        "varients":[
            {"name":"4gb+64gb","price":10000},
            {"name":"8gb+128gb","price":12000},
        
        ]
    }, 
    {
        "name":"m30","brand":"samsung","network":"4g","colors":["black","white"],
        "varients":[
            {"name":"4gb+64gb","price":20000},
            {"name":"8gb+128gb","price":14000},
        
        ]
    },
    {
        "name":"oneplusnort2t","brand":"oneplus","network":"5g","colors":["black","grey"],
        "varients":[
            {"name":"4gb+64gb","price":2700},
            {"name":"8gb+128gb","price":30000},
        
        ]
    },
    {
        "name":"mi11i","brand":"mi","network":"5g","colors":["black","green"],
        "varients":[
            {"name":"4gb+64gb","price":25000},
            {"name":"8gb+128gb","price":28000},
        
        ]
    },



]
#----------------black color mobile names
for p in phones:
        if "black" in p.get("colors"):
            print(p.get("name"))
print("---------------------------------")
#----------print all mobile names available under 20k
for p in phones:
    for i in p.get("varients"):
        if i.get("price")<20000:
            print(p.get("name"),i.get("name"))
print("----------------------")

#----------------8gb+128gb grey color
for p in phones:
     for v in p.get("varients"):
          if v.get("name")=="8gb+128gb" and "grey" in p.get("colors"):
               print(p.get("name"),v.get("name"))