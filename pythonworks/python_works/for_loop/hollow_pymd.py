for row in range(1,7):
    for col in range(1,12):
        if row==6 or row+col==7 or col-row==5:
            print("*",end="")
        else:
            print(end=" ")
    print()