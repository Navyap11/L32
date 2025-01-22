print ("select ur ride: ")
print("1) bus")
print("2) train")
print("3) car")

select= int(input("Emter you ride: "))

if (select==1):
    print("What bus route?")
    print("1) 67")
    print("2) 600")
   

    choice2=int(input("which bus: "))
    if (choice2==1):
        print("you have selected 67 bus route")
    else:
        print("You have selected 600 bus route")

elif (select==2):
    print("Which train?")
    print("1) train 1")
    print("2) train 2")
    choice3=int(input("Enter your train: "))
    if (choice3==1):
        print("You have selected train 1")
    else:
        print("you have selected train 2")

elif (select==3):
    print("What type of car?")
    print("1)Tesla")
    print("2)Leaf")
    choice4=int(input("Enter ur car:"))
    if (choice4==1):
        print("You have selected Tesla")
    else: 
        print("you have selected leaf") 

else:
    print("Wrong choice!")