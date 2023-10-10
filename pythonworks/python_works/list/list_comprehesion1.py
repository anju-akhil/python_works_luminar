#2000 -2025
years=[y for y in range(2000,2026)]
print("years=",years)

#century years
century_years=[y for y in years if y%100==0 ]
print("century_years=",century_years)

#non century years
non_century=[y for y in years if y%100!=0]
print("non century year=",non_century)