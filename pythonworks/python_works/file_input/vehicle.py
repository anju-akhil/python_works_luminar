f=open("C:\\Users\\HP\\Desktop\\pythonworks\\file_input\\numbers.txt","r")
num=[line.rstrip("\n")for line in f]
kl_num=[n for n in num if n.startswith("kl")]
print("Kerala numbers=",kl_num)