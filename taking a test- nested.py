medical_cause= input("Enter YES if you have medical cause. Otherwise, enter NO: ")
attendance= int(input("enetr your attendance scores: "))

if medical_cause=="YES":
    print("you are allowed")
else:
    if attendance>=75:
        print("You are allowed")
    else:
        print("you are not allowed")