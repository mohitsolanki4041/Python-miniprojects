# Inventry System:
inventry={}
while True:
     action=input()
     if action=="add":
          item=input()
          quantity=int(input())
          if item in inventry:
               inventry[item]+=quantity
          else:
               inventry[item]=quantity
     elif action=="remove":
          item=input()
          quantity=int(input())
          if item in inventry and inventry[item]>=quantity:
               inventry[item]-=quantity
          elif item in inventry and inventry[item]<quantity:
               print(f"TThere are only {inventry[item]} {item}s left in the inventry.")
          else:
               print(f"There is no {item} in the inventry.")
     elif action=="display":
          print("Inventry")
          for key, value in inventry.items():
               print(f"{key} : {value}")
     elif action=="quit":
          break
     else:
          print("Invalid action. Please try again.")