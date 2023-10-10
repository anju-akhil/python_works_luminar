#Print first recursive character
text="MABCDCFD"
wc={}
for ch in text:
    #print (ch)
    if ch in wc:
        #wc[ch]+=1
        print("first recursive character is",ch)
        break
    else:
        wc[ch]=1
       
       

