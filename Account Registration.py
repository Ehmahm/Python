print("What is your first name :")
f_name =input(())
print("What is your last name :")
l_name =input(())
print("What is your email address :")
e_address =input(())
print("What is your new password :")
n_password =input(())

print("Your account has been successfully created !!!!!")
print("Please enter your account details to login ")

print("Please enter your email address :")
address =input(())
print("Please enter your password :")
password =input(())

if (password == n_password) and (address == e_address):
    print("You have successfully logged into your account")

if (password != n_password) and (address != e_address):
    print("Wrong email address or password. Please check your details and try again")
