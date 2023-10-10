#print words starting with vowels
text="Sunil Gavaskar had a no-holds-barred remark on overseas commentators"
words=text.split(" ")
##print(words)
#m='a','e','i','o','u'
#for w in words:
#    if w.casefold().startswith(m):
 #       print(w)

 #----------other method----------
v=['a','e','i','o','u']
for w in words:
    if w[0].casefold() in v:
        print(w)