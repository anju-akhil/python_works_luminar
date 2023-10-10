#position value matrix

arr=[
    [2,0,1],
    [1,1,0],
    [2,0,3]
]

for row in range(0,3):
    for col in range(0,3):
        value=row+col-arr[row][col] # row+col-element
        print(value,end="\t")
    print()