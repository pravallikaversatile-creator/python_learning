age=int(input("enter age of the person: "))
day=input("Enter the day of the week, ticket is brought: ")
if age<0:
    print("Entered invalid age")
else:
    
    if age<13:
      ticket_price=5
    elif age<65:
      ticket_price=10
    else:
      ticket_price=7
    if day.lower()=="wednesday":
      ticket_price-=2
    if ticket_price<3:
      ticket_price=3
    print("age is: ",age," day of the week is: ",day," and price of ticket is: ",ticket_price,".",sep="")
