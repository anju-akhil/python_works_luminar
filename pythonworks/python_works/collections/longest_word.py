text="hello good hello goodmorning"
words=text.split(" ")

#for w in words:
 #   if(len(w)>1):
  #      large=w
large=sorted(words,key=lambda w:len(w),reverse=True)        
print(large)
