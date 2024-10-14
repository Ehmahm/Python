print("Please enter your final marks to receive your grading.")
firstR=int(input("What were your final marks in Structured programming:"))
secondR=int(input("What were your final marks in Local Area Networking:"))
thirdR=int(input("What were your final marks in New Testament:"))

if firstR >= 90:
    print("You have an A in Structured programming.")
elif firstR >= 75:
    print("You have a B in Structured programming.")
elif firstR >=60:
    print("You have a C in Structured programming.")
elif firstR >= 50:
    print("You have a pass in Structured programming.")
else :
    print("You have a retake in Structured programming.")


if secondR >= 90:
    print("You have an A in Local Area Networking.")
elif secondR >= 75:
    print("You have a B in Local Area Networking.")
elif secondR >=60:
    print("You have a C in Local Area Networking.")
elif secondR >= 50:
    print("You have a pass in Local Area Networking.")
else :
    print("You have a retake in Local Area Networking.")
    

if thirdR >= 90:
    print("You have an A in New Testament.")
elif thirdR >= 75:
    print("You have a B in New Testament.")
elif thirdR >=60:
    print("You have a C in New Testament.")
elif thirdR >= 50:
    print("You have a pass in New Testament.")
else :
    print("You have a retake in New Testament.")
