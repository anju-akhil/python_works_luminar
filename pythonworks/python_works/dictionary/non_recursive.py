text="ABABBCDCEF"
wc={}
for ch in text:
    if ch in wc:
        wc[ch]+=1
    else:
        wc[ch]=1
#print(wc)
for k,v in wc.items():
    if v==1:
        print(k)
        