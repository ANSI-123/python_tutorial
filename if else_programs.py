# a =int(input("enter the number: "))
# if a>0:
#     print("the number is positive ")
# else:
#     print("the number is negative ")     enter the number: 5
#                                         the number is positive





# a =int(input("enter the number: "))
# if a>0:
#     print("the number is positive ")
# elif a<0:
#     print("the number is negative ")
# else:
#     print("the number is zero")





#     Prompt the user to input their marks
# If the marks are 90 or above, print "Grade is A".
# If the marks are 80 or above but less than 90, print "Grade is B".
# If the marks are 70 or above but less than 80, print "Grade is C".
# If the marks are below 70, print "Failed".


# a=int(input("enter the marks : "))
# if a>=90:
#     print("Grade is A")
# elif a>=80:
#     print("Grade is B")
# elif a>=70:
#     print("Grade is c") 
# else:
#     print("Failed")
            



# a=int(input("enter first number : "))
# b=int(input("enter second number : "))
# c=int(input("enter third number : "))
# d=a+b+c/3
# e=a+b+c//3
# print(f"the average of three number is : {d}")
# print(f"the average of three number is : {e}")



# Question:
# Write a program to compare two numbers and print whether they are equal, or which one is greater.


# a=int(input("enter first number : "))
# b=int(input("enter second number : "))
# if a==b:
#     print("they are equal")
# elif a>b:
#     print(f"the greater one is :{a}") 
# else:
#     print(f"the greater one is :{b}")    



# To check a number even or not


# a=int(input("enter a number : "))
# if a%2==0:
#     print("the number is even")  
# else:
#     print("the number is odd")



#  Create a calculator by using python 

# a=float(input("enter first number: "))
# b=float(input("enter second number: "))
# operator=input("enter the operator (+,-,*,/) :")
# if operator=="+":
#     print("result a+b =",a+b)
# if operator=="-":
#     print("result a-b =",a-b)
# if operator=="*":
#     print("result a*b =",a*b)
# if operator=="/":    
#     print("result a/b =",a/b)




# Write a program to check if a number is divisible by both 3 and 7

# a=int(input("enter a number :"))
# if a%3==0 and a%7==0:
#     print("the number is divisible by both 3 and 7 ")
# else:
#     print("the number is not divisible by both 3 and 7 ")
   




# Take Three numbers and check which numbers is gratest

# a=int(input("enter first number :"))
# b=int(input("enter second number : "))
# c=int(input("enter third number : "))
# if a>b and a>c:
#     print("a is greater")
# elif b>a and b>c:
#     print("b is greater")    
# else:
#     print("c is greater")



# To interchange two lists


# a=[1,2,3,4,5]
# b=[6,7,8,9,10]
# c=[]
# c=a
# a=b
# b=c
# print("result : a=",a)
# print("result : b=",b)




# a=int(input("enter a number :"))
# b=a
# print("the result b",b)


# To print an integer value as list
# # a=int(input("enter a number : "))
# # b=[]
# # b.append(a)
# # print("Integer value of input:", b)



# Take a number from user
# if number is 0 add it into list  a
# even add to list b
# odd add to list c


# a=[]
# b=[]
# c=[]
# d=int(input("enter a number :"))
# if d==0:
#     a.append(d)
#     print("the number is zero:",a)
# elif d%2==0:
#     b.append(d) 
#     print("the number is even:",b)   
# else:
#     c.append(d)
#     print("the number is odd",c)    





# Take two numbers as input. Append the small number to list a and the large number to list b.


# a = []
# b = []  

# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))

# if num1 < num2:
#     a.append(num1)
#     b.append(num2)

# elif num1 > num2:
#     a.append(num2)
#     b.append(num1)
# else:
#     print("Both numbers are equal.")

# print("List of small number is (a):", a)
# print("List of large number is (b):", b)



# a=(input("enter a number: "))
# if a[0]==a[-1]:
#     print(f"{a} is palindrome ")
# else:
#     print("It is not palindrome")




# anagram/(common letters in two wors)
# "listen" → "silent"
# An anagram is a word or phrase formed by rearranging the letters of another 
# word or phrase, using all the original letters exactly once.



# word1 = input("enter the first word : ")
# word2 =  input("enter the second word : ")

# # Step 1: Remove spaces and convert both strings to lowercase
# word1 = word1.lower()
# word2 = word2.lower()

# # Step 2: Check if the sorted versions of the strings are the same
# if sorted(word1) == sorted(word2):
#     print(f'"{word1}" and "{word2}" are anagrams.')
# else:
#     print(f'"{word1}" and "{word2}" are not anagrams.')







# What is the capital of india?


# print("Simple Quiz:")
# print("1. Delhi")
# print("2. Mumbai")
# print("3. Chennai")
# print("4. Ernakulam")

# choice = int(input("Enter the number of your choice: "))

# if choice == 1:  
#     print("Correct! You selected Delhi.")
# elif choice == 2: 
#     print("Incorrect. You selected Mumbai.")
# elif choice == 3:  
#     print("Incorrect. You selected Chennai.")
# elif choice == 4: 
#     print("Incorrect. You selected Ernakulam.")
# else:
#     print("Invalid choice. Please select a number between 1 and 4.")


# Simple Quiz:
# 1. Delhi
# 2. Mumbai
# 3. Chennai
# 4. Ernakulam
# Enter the number of your choice: 1
# Correct! You selected Delhi.






# Write a Python program for a simple food ordering system. The program should display a menu with the following options:

# Pizza
# Burger
# Pasta
# Exit
# The user should enter the number corresponding to their choice.
# If the user selects Pizza, prompt them to enter the number of pieces they want and display a confirmation message.
# If the user selects Burger, prompt them to specify the size of the burger (Small/Medium/Large) and display a confirmation message.
# If the user selects Pasta, prompt them to specify the type of sauce they want and display a confirmation message.
# If the user selects Exit, display a message and terminate the program.
# If the user enters an invalid choice, display an error message.



# sample 

# Menu:
# 1. Pizza
# 2. Burger
# 3. Pasta
# 4. Exit

# Enter the number of your choice: 1
# Enter number of pieces you need: 3
# You ordered 3 pieces Pizza successfully.


# print("Menu:")
# print("1. Pizza")
# print("2. Burger")
# print("3. Pasta")
# print("4. Exit")

# choice = int(input("Enter the number of your choice: "))

# if choice == 1:  # Pizza
#     pieces = int(input("Enter number of pieces you need: "))
#     print(f"You ordered {pieces} pieces Pizza successfully.")

# elif choice == 2:  # Burger
#     size = input("Enter the size of the burger (Small/Medium/Large): ").capitalize()
#     if size in ["Small", "Medium", "Large"]:
#         print(f"You ordered a {size} Burger successfully.")
#     else:
#         print("Invalid size. Please choose between Small, Medium, or Large.")

# elif choice == 3:  # Pasta
#     sauce = input("Enter the type of sauce you want (Tomato/Alfredo/Pesto): ").capitalize()
#     if sauce in ["Tomato", "Alfredo", "Pesto"]:
#         print(f"You ordered Pasta with {sauce} sauce successfully.")
#     else:
#         print("Invalid sauce type. Please choose between Tomato, Alfredo, or Pesto.")

# elif choice == 4:  # Exit
#     print("Thank you for using the Food Ordering System. Goodbye!")

# else:
#     print("Invalid choice. Please select a number between 1 and 4.")



















