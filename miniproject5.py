# Calculator
first = int(input())
second = int(input())
print("1 for add, 2 for sub, 3 for mul, 4 for divide, 5 for power, 6 for float division")
inp = int(input())
if inp == 1:
     print(first+second)
elif inp == 2:
     print(first-second)
elif inp == 3:
     print(first*second)
elif inp == 4:
     print(first/second)
elif inp == 5:
     print(first**second)
elif inp == 6:
     print(first//second)
else:
     print("You entered wrong option.")