source_word="devilish"
target_word="evil"
wc={}
is_kangaroo=True
for ch in source_word:
    if ch in wc:
        wc[ch]+=1
    else:
        wc[ch]=1
#print(wc)

for ch in target_word:
    if ch in wc and wc.get(ch)>0:
            wc[ch]-=1
           
    else:
         is_kangaroo=False
         break
print(is_kangaroo)       
        