#asking for input
print("Welcome to Ehmah's calculator .")
print("Ready to help in addition,subtraction ,division and multiplication.")
first =int(input("What is the first number ?"))

print("1.+")
print("2.-")
print("3.*")
print("4./")

print("What is the desired computation ?")
operator = int(input())

second =int(input("What is the second number ?"))

#initializing variable to store input
right_answer = 0

#performing addition

if operator ==1:
    print("What is ",first,"+",second)
    right_answer = first+second

#performing subtraction
if operator ==2:
    print("What is",first,"-",second)
    right_answer = first-second

#performing multiplication
if operator ==3:
    print("What is",first,"*",second)
    right_answer = first*second

#performing division
if operator ==4:
    print("What is",first,"/",second)
    right_answer = first/second

#picking answer from user
ans=int(input())

#comparing

if right_answer == ans :
     print("You are correct")
else:
     print("Wrong answer,The correct answer is ,{right_answer}")
