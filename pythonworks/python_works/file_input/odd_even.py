f_read=open("C:\\Users\\HP\\Desktop\\pythonworks\\file_input\\data.txt","r")
odd_write=open("C:\\Users\\HP\\Desktop\\pythonworks\\file_input\\odd.txt","w")
even_write=open("C:\\Users\\HP\\Desktop\\pythonworks\\file_input\\even.txt","w")
for line in f_read:
    num=int(line.rstrip("\n"))
    if num %2==0:
        even_write.write(str(num)+"\n")
    else:
        odd_write.write(str(num)+"\n")