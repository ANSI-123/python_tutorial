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


# 3. Check if numbers from 1 to 20 are divisible by 3.

# for i in range(1, 21):
#     if i % 3 == 0:
#         print(f"{i} is divisible by 3")
#     else:
#         print(f"{i} is not divisible by 3")



# 4. Print the square of each number from 1 to 10.

# for i in range(1,11):
#     i**=2
#     print(i)



# 5. Print "Fizz" for multiples of 3, "Buzz" for multiples of 5, and "FizzBuzz" for both, up to 15.

# for i in range(1,16):
#     if i%3==0 and i%5==0:
#         print("FizzBuzz")
#     elif(i%3==0):
#         print("Fizz")
#     elif(i%5==0):
#         print("Buzz")
       
       


# 6. Print numbers from 1 to 10, but skip 5.


# for i in range(1,11):
#     if(i==5):
#         continue
#     print(i)



# 7. Count how many numbers between 1 and 20 are divisible by 4.


# count=0
# for i in range(1,21):
#     if(i%4==0):
#         count+=1
# print(count)



# 8. Find the sum of even numbers from 1 to 20.
# sum=0
# for i in range(1,21):
#     if (i%2==0):
#         sum+=i
# print(sum)
  


# 10. Print numbers from 1 to 10 and stop when you reach 7.


# for i in range(1,11):
#     if (i==7):
#         break
#     print(i)



# 11. Check if each number in a list is positive, negative, or zero.



# a=[1,2,3,4,5,0,-1,-2,-3,-4,-5]
# for list in a:
#     if list>0:
#         print("a is positive")
#     elif list<0:
#         print("a is negative")
#     else:
#         print("a is zero")        

     

# 12. Print numbers from 1 to 15, replacing multiples of 4 with "Four".


# for i in range(1,16):
#     if(i%4==0):
#         print("Four")
#     else:
#         print(i)    




# 13. Find the sum of all odd numbers from 1 to 15.

# sum=0
# for i in range(1,16):
#     if(i%2!=0):
#         sum+=i
# print(sum)        




# 14.Reverse a string using a loop


# string="HELLO WORLD"
# reverse_string=""
# for char in string:
#     reverse_string=char+reverse_string
# print(reverse_string)




# 15.Find the average of a list of numbers.

# numbers = [10, 20, 30, 40, 50]
# total = 0
# for num in numbers:
#     total += num
# average = total / len(numbers)
# print(f"Average: {average}")

      


# 16.Print all numbers divisible by 3 and 5 between 1 and 30.


# for i in range (1,31):
#     if(i%3==0) and (i%5==0):
#         print(i)



# 17.Check if numbers from 1 to 10 are odd and divisible by 3.

# for i in range(1, 11):
#     if i % 2 != 0 and i % 3 == 0:
#         print(f"{i} is odd and divisible by 3")




       
# s=['abc','bce','adbc','ccde','bcd']
# c=[]
# for i in s:
#     if len(i) == 3:
#         c.append(i)
# print(f"where length i=3 is {c}")
##
# where length i=3 is ['abc', 'bce', 'bcd']
