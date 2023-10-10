f_read=open("C:\\Users\\HP\\Desktop\\pythonworks\\file_input\\year.txt")
fwrite=open("C:\\Users\\HP\\Desktop\\pythonworks\\file_input\\lyear.txt","w")
for line in f_read:
    year=int(line.rstrip("\n"))
    if(year%100==0 and year %400==0):
        fwrite.write(str(year)+"\n")
    elif(year %100!=0 and year%4==0):
        fwrite.write(str(year)+"\n")
    