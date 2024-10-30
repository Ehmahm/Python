print("Welcome to Bobics Restaurant")

#Print the Menu
print("Menu")
print("1. Chicken Biryani")
print("2. Mutton Biryani")
print("3. Veg Biryani")
print("4. Chicken Fried Rice")
print("5. Rolex")
print("6. Lusaniya")

#Get the order from the user
order = input("What would you like to order? Enter your choice (1-6): ")

#Print the order and show the bill in UGX
if order == "1":
    print("You ordered Chicken Biryani. Your bill is UGX 20,000")
elif order == "2":
    print("You ordered Mutton Biryani. Your bill is UGX 25,000")
elif order == "3":
    print("You ordered Veg Biryani. Your bill is UGX 15,000")
elif order == "4":
    print("You ordered Chicken Fried Rice. Your bill is UGX 18,000")
elif order == "5":
    print("You ordered Rolex. Your bill is UGX 5,000")
elif order == "6":
    print("You ordered Lusaniya. Your bill is UGX 10,000")
else:
    print("Invalid choice. Please enter a number between 1 and 6")

