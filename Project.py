print("Mirroried triangles you want?:")
row=int(input("Enter a number of rows:"))
count=0
for i in range(row):
    for j in range(i + 1):
        count=count + 1
        print(count, end=" ")
    print()