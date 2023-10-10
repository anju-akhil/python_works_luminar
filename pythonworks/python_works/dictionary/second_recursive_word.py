text="AMBAHMBJ"
wc={}
lst=[]
for ch in text:
    if ch in wc:
        lst.append(ch)
    else:
        wc[ch]=1
print("second recursive characer",lst[1])