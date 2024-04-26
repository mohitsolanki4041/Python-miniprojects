## Make a mini project for student report card with %age and grades.
# name = input("Enter ur name: ")
# mark1 = int(input("Enter ur 1st marks: "))
# mark2 = int(input("Enter ur 2nd marks: "))
# mark3 = int(input("Enter ur 3rd marks: "))
# mark4 = int(input("Enter ur 4th marks: "))
# mark5 = int(input("Enter ur 5th marks: "))
# per = ((mark1+mark2+mark3+mark4+mark5)/5)
# if (mark1, mark2, mark3, mark4, mark5 > 100):
#     print("Invalid Marks.")
# else:
#     if 90<per<=100:
#         print("A")
#         print(per, "%")
#     elif 80<per<=90:
#         print("B")
#         print(per, "%")
#     elif 70<per<=80:
#         print("C")
#         print(per, "%")
#     elif 60<per<=70:
#         print("D")
#         print(per, "%")
#     elif 50<per<=60:
#         print("E")
#         print(per, "%")
#     else:
#         print("You fail.")
# if per > 100:
#     print("Invalid Percentage.")

# WAP to check number is even or odd
num = int(input("Enter the number: "))
if(num % 2 == 0):
    print("Number is even.")
else:
    print("Number is odd.")

# WAP to check even without %
num = int(input("Enter the number: "))
if ((num & 2) == 0):
    print("Number is EVEN.")
else:
    print("Number is ODD.")