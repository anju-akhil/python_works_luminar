from re import *
text="ababababc"

pattern="a?" #
matcher=finditer(pattern,text)

for m in matcher:
    print(m.start(),m.group())