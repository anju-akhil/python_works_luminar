f=open("C:\\Users\\HP\\Desktop\\pythonworks\\file_input\\data.txt","r")
#lst=[]
#for line in f:
 #   lst.append(line.rstrip("\n"))
#print(lst)
#longest_word=max(lst,key=lambda w:len(w))
#print("longest_word=",longest_word)

#------------------simplify above code--------------
words=[line.rstrip("\n") for line in f]
longest_word=max(words,key=lambda w:len(w))
print("longest_word=",longest_word)