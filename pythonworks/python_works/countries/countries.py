from json import load
path="C:\\Users\\HP\\Desktop\\pythonworks\\countries\\countries.json"
with open(path,encoding="utf-8")as f:
    countries=load(f)

#----------total number of countries-----------------------------
#print(len(countries))

#--------------countries names-----------------------------------
c_name=[c.get("name")for c in countries]
#print(c_name)

#------------name startwith --------------------------------------
start_name=[c.get("name")for c in countries if c.get("name").startswith("C")]
#print(start_name)

#--------------------------------------captital of countries------
cap=[[c.get("name"),c.get("capital")]for c in countries]
#print(cap)

#---------------------------population----------------------------
popu=[c.get("population") for c in countries if c.get("name")=="Åland Islands"]
#print(popu)

#------------------highest border---------------------------------
c_border=[c for c in countries if "borders" in c]
max_border=max(c_border,key=lambda c:len(c.get("borders")))
#print(max_border.get("name"))

#-------------- border share of india------------------------------
india_border=[c.get("borders")for c in countries if c.get("name")=="India"][0]
india_border_name=[c.get("name")for c in countries if c.get("alpha3Code")in india_border]
#print(india_border_name)

#--------------------------regions----------------------------------
all_regions={c.get("region")for c in countries }
#print(all_regions)

#-------------------------depended_country---------------------------
depended_cntry=[c.get("name")for c in countries if c.get("independent")==False]
#print(depended_cntry)

#------------------------population <400000---------------------------
popl_filter=[c.get("name")for c in countries if c.get("population")<400000]
#print(popl_filter)

#------------------regionwise count-----------------------------------
