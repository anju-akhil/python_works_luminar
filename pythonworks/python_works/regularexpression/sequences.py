from re import *
text="ab5cd12kgd*7^h"
#pattern="\d" #[0-9]
#pattern="\D" #[^0-9]
#pattern="\w" #[a-zA-Z0-9]
pattern="\W" #special characters

matcher=finditer(pattern,text)

for m in matcher:
    print(m.start(),m.group())