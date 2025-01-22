units= int(input("Please enter the amount of Units you consumed: "))

if (units<50):
    amount= units*2.60
    surcharge= 25

elif(units<=100):
    amount= 130-((units-50)*5.62)
    surcharge= 35

elif (units<=200):
    amount= 130+162.50-((units-100)*5.62)
    surcharge=45
else:
    print("invalid option")
total= amount+ surcharge
print("\n Electrical bill= %2f" %total)