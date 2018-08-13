def grid(row,col):
    for i in range(row):
        for j in range(col):
            if i==0 or i==int(row/2) or i==row-1:
                if j==0 or j==int(col/2) or j==col-1:
                    print("+", end=' ')
                else:
                    print("-", end=' ')
            elif j==int(col/2) or j==0 or j==col-1:
                print("|", end=' ')
            else:
                print(" ", end=' ')
        print()
m=int(input("Enter number of rows:"))
n=int(input("Enter number of coulumns:"))
grid(m,n)
