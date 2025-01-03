 # 1. Print even numbers from 1 to 20.

# for i in range(1,21):
#     if(i%2==0):
#         print(i)

# 2. Print numbers from 1 to 20, but say "Odd" or "Even" next to each number.

# for i in range(1,21):
#     if(i%2==0):
#         print(f"{i} is even")
#     else:
#         print(f"{i} is odd")    




# a=[]
# b=[]
# for i in range(1,51):
#     if(i%2==0):
#         a.append(i)   
#     else:
#         b.append(i)
# print(a)
# print(b)    


# print 1 to 10 and skip 3

# for i in range(1,11):
#     if(i==3):
#         continue
#     print(i)


# *[continue-skip iteration]


# print 1 to 20,to stop when iteration is 15

# for i in range(1,21):
#     if (i==15):
#         break
#     print(i)


# *To break a Iteration    


# 7. Count how many numbers between 1 and 20 are divisible by 4.


# count=0
# for i in range(1,21):
#     if(i%4==0):
#         count+=1
# print(count)


# 14.Reverse a string using a loop

# string = "hello"
# reversed_string = ""
# for char in string:
#     reversed_string = char + reversed_string
# print(f"Reversed string: {reversed_string}")





# first Iteration: char = "h"
# reversed_string = "h" + "" = "h"

# Second Iteration: char = "e"
# reversed_string = "e" + "h" = "eh"

# Third Iteration: char = "l"
# reversed_string = "l" + "eh" = "leh"

# Fourth Iteration: char = "l"
# reversed_string = "l" + "leh" = "lleh"

# Fifth Iteration: char = "o"
# reversed_string = "o" + "lleh" = "olleh"





# string = input("enter the word : ")
# vowels = "aeiouAEIOU"  
# count = 0 


# for char in string:
#     if char in vowels:  
#         count += 1  

# print("Number of vowels:", count)





# string = input("enter the word : ")
# vowels = "aeiouAEIOU"  
# c=[]


# for char in string:
#     if char in vowels:  
#       c.append(char)  

# print(" vowels:",c )



# enter the word : as
#  vowels: ['a']






# to print the word in capital &small

# string = input("enter the word : ")

# a=string.lower()
# b=string.upper()

# print(f"lower the string : {a}")
# print(f"upper the string : {b}")