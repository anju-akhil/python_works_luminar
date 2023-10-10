#remove duplicates
lst=[10,20,30,70]

st=set(lst)
#print(st)
st1={10,20,30}
st2={11,12,20,24,30}

#------union()
un=st1.union(st2)
print("union",un)
#-----intersection
intersection_st=st1.intersection(st2)
print("intersection",intersection_st)
#---------difference()
diff=st1.difference(st2)
print("difference",diff)