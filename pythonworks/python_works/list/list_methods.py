colors=["red","green","blue"]
lst=[100,51,87]
#------append()
colors.append("yellow")
print(colors)

#------pop()
colors.pop(-1)
print(colors)

#------sort()
colors.sort()
lst.sort()
print(lst)
print(colors)

#--------descending order sort
colors.sort(reverse=True)
print(colors)

#-------count()
print(colors.count("red"))

#-------clear()
colors.clear()
print(colors)