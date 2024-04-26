name = input("Enter ur name: ")
id = int(input("Enter your aadhar number: "))
age = int(input("Enter ur age: "))
if age >= 18:
    print("You can vote.")
    print("1 for BJP, 2 for ICP, 3 for SPA, 4 for TMC, 5 for NONE.")
    vote = input("Enter your vote: ")
    if vote == 1:
        print("BJP")
    elif vote == 2:
        print("ICP")
    elif vote == 3:
        print("SPA")
    elif vote == 4:
        print("TMC")
    elif vote == 5:
        print("None")
    else:
        print("You entered wrong vote.")
else:
    print("You can't vote.")