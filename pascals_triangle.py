
#Take in the number of rows the triangle should have and store it in a separate variable 'n'.
n = int(input("Enter number of rows: "))
#create an empty list
lst=[]
#Using a for loop which ranges from 0 to n-1, append the sub-lists into the list.
for i in range(n):
    lst.append([])
#Then append 1 into the sub-lists.
    lst[i].append(1)
#Then use a for loop to determine the value of the number inside the triangle.
    for j in range(1,i):
        lst[i].append(lst[i-1][j-1] + lst[i-1][j])
    if(n!= 0):
        lst[i].append(1)
for i in range(n):
#Print the Pascal’s triangle according to the format.
    print("   "*(n-i),end=" ",sep=" ")
    for j in range(0,i+1):
        print('{0:6}'.format(lst[i][j]),end=" ",sep=" ")
    print()
