#  Declare two variables, one storing an integer and the other a string ,Print their values

# a=460
# b="chandu"
# print(a,b)
# print(type(a),type(b))

#  Convert a float to an integer and print the result
# a=97.5
# b=65.6
# print(int(a),int(b))

#  Convert an integer to a string and display the output.
# a=5
# print(str(a))

# Take the user's age as input and print a message using that input.
# user_1=input("enter the age:")
# user_2=input("enter the age:")
# print(user_1,user_2)

# Develop a script that swaps the values of two variables without using a temporary variable.
# a = 5
# b = 10
# a, b = b, a
# print("a:", a)
# print("b:", b)

#  Create a program that takes user input for their age, converts it to an integer, adds 5, and then prints the result
# age=input("enter the age:")
# age_int=(int(age))
# new_age=(age_int +5)
# print("In 5 years, you will be:", new_age)

#  Build a calculator program that takes two numbers as input and performs the arithmetic operation.
# num_1=int(input("enter the number:"))
# num_2=int(input("enter the number:"))
# print(num_1 + num_2)#addition operaton
# print(num_1-num_2)#substraction operation
# print(num_1*num_2)#multiplication operation
# print(num_1/num_2)#division operation

#  Create a program that takes user input for their name and age. Use formatted strings (f-strings) to print a message welcoming the user and
# user_name=input("Enter the Name:")
# user_age=int(input("Enter the Age:"))
# print(f"name of the user is {user_name} and age of the user is{user_age}")

'''
Write a Python script that defines a dictionary with information 
about a product (e.g., name, price, quantity). Use formatted strings to display 
the information in a readable format.

'''
# my_dict={
#     "product_name":"cricket bats",
#     "product price": "15000",
#     "product quntity":3
# }
# print(my_dict)
# print(f"product details")
# print(f"name of the product is{my_dict["product_name"]},price of the product is{my_dict["product price"]},quantity of the product is{my_dict["product quntity"]}")


'''
Create a list called numbers that contains integers from 1 to 10.
 Check if the number 5 is in the list.
 Check if the number 15 is not in the list.
'''

# Create a list called numbers that contains integers from 1 to 10
# numbers = list(range(1, 11))

# Check if the number 5 is in the list
# is_five_in_list = 5 in numbers

# Check if the number 15 is not in the list
# is_fifteen_not_in_list = 15 not in numbers

# Print the results
# print("Is 5 in the list?", is_five_in_list)
# print("Is 15 not in the list?", is_fifteen_not_in_list)


#Write a Python program to calculate the simple interest given the principalamount, rate, and time (in years).

# principal_amount = int(input("Enter the prinical_amount"))
# rate = float(input("Enter the rate of interest %"))
# time =int(input("Enter the amount of time"))
# print(f"The simple interest amount  is {(principal_amount*rate*time)//100}")

# ---------------concatenation -----------------
# msg_01=input("enter the string value:")
# msg_02=input("enter the string value :")
# conc=msg_01+msg_02
# print(conc)

# --------celcius to fareinheit-----------------

# celsius=int(input("enter the celsius value:"))
# fahrenheit=(celsius*(9/5))+32
# print(f"celsius after conversion fahrenheit,the temparture in fahrenheit is {fahrenheit}")


#----------- to caluculate area of rectangle-----------
 
# length=int(input("enter the length of rectangles:"))
# breadth=int(input("enter the breadth of rectangles:"))
# area=length*breadth
# print(f"the length of rectangle is {length} and the width of rectangle is {breadth},the the area of rectangle is {area}")

#-------------convert distance from kilometers to miles---------

kilometers = float(input("Enter the distance in kilometers:"))
miles= kilometers *0.62137119
print(f"{kilometers} km is equal to {miles} miles")