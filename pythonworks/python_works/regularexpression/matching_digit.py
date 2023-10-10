from re import *
text="ab5cdABCDe79f_k"
pattern="[0-9]"
matcher=finditer(pattern,text)
for m in matcher:
    print(m.start(),m.group())