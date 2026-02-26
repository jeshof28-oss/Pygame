set1=set([])
set2=set([])

a_loop=int(input("Enter number of values in set 1 - "))
b_loop=int(input("Enter number of values in set 2 - "))

for i in range(a_loop):
    set1.add(input("Enter value to be added to set 1 - "))

print("Set 1 - {}".format(set1))
for i in range(b_loop):
    set2.add(input("Enter value to add to set 2 - "))

print("Set 2 - {}".format(set2))

while True:
    print("What do you want to perform? \n 1. Union \n 2. Intersection \n 3. Difference \n 4. Symmetric Difference \n 5. Exit")
    ans=int(input("Select option to perform - "))

    if ans == 1:
        print(set1.union(set2))

    elif ans == 2:
        print(set1.intersection(set2))

    elif ans == 3:
        print(set1.difference(set2))

    elif ans == 4:
        print(set1^set2)
    
    elif ans == 5:
        break

    else:
        print("Enter a valid number.")