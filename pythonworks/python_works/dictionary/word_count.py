#print words count from given string
text="good morning good evening"
words=text.split(" ")
print(words)
wc={}

for w in words:
    if w in wc:
        wc[w]+=1
    else:
        wc[w]=1
print(wc)