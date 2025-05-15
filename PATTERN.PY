print("Half pyramid pattern of stars (*):")
n = int(input("Enter the number of rows:"))
for i in range (n):
    for j in range(i+1):
        print("* ", end= "")
    print()
    
    # fluids triangle
    
rows = int(input("Please enter the total number of rows:"))
number = 1 
    
print("Floyds triangle")
for i in range (1, rows + 1):
    for j in range(1, i +1):
        print(number , end = ' ')
        number = number + 1 
    print()
    
    
    
rowsize = int(input("enter the number of rows :"))
if rowsize%2==0:
    halfDiamrow = int(rowsize/2)
else:
    halfDiamrow = int (rowsize/2)+1
space = halfDiamrow-1
for i in range (1, halfDiamrow+1):
    for j in range(1,space+1):
            print(end=" ")
    space = space-1
    num = 1
    for j in range (2*i-1):
        print(end=str(num))
        num = num+1
    print()
space = 1
# loop for lower part


for i in range (1, halfDiamrow):
    for j in range (1, space+1):
        print(end= " ")
    space = space+ 1
    num = 1
    for j in range (1, 2*(halfDiamrow-i)):
        print(end=str(num))
        num = num+1
    print()
       