# numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

        #   0,  1,   2,  3,  4,  5,  6,  7,  8,   9 

# list[start:end:step]



# print(numbers[1:3])    [20, 30]
# print(numbers[4:9])     [50, 60, 70, 80, 90]  



# print(numbers[5:])    [60, 70, 80, 90, 100]    


# print(numbers[:4])    [10, 20, 30, 40] 


# List=[1,2,3,4,5,6,7,8,9,10]

    #   0,1,2,3,4,5,6,7,8,9  

# print(List[:])    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(List[::2])
# print(List[::-2])
# print(List[::-1])   [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]   :(to reverse)




# List=[1,2,3,4,5,6,7,8,9,10]
# b=[]
# c=sum(List)
# b.append(c)
# print(b)    [55]

# List=[1,2,3,4,5,6,7,8,9,10]
# b=[]
# c=max(List)
# b.append(c)
# print(b)      [10]


# c=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35]
# a=[]
# b=[]


# for i in range(1,11,2):
#     print(i)

# 1
# 3
# 5
# 7
# 9



# for i in range(1,11):
#     print(i)
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10    



# c=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35]

# for i in c:
#     print(i)


# for i in range(1,151):
#     print(i)

# for i in range(1,2):
#     print(f"3 * {i} = {3 * i}")   

# 3 * 1 = 3






# for i in range(1,11):
#     print(f"3 * {i} = {3 * i}")

# 3 * 1 = 3
# 3 * 2 = 6 
# 3 * 3 = 9 
# 3 * 4 = 12
# 3 * 5 = 15
# 3 * 6 = 18
# 3 * 7 = 21
# 3 * 8 = 24
# 3 * 9 = 27
# 3 * 10 = 30


# To append all numbers which are divisible by 5
# c=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35]

# b=[]
# for i in c:
#     if i%5==0:
#         b.append(i)
# print(b)               [5, 10, 15, 20, 25, 30, 35]
        



# c=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35]
# a=[]
# b=[]
# for i in c:
#         if i%7==0:
#             a.append(i)
# print(a)
# for j in c:
#         if j%8==0:
#              b.append(j)

# print(b)    
              





# # a=["apple","orange","cherry","mango"]
# # for i in a:
# #     print(f"i like {i}")

# i like apple
# i like orange
# i like cherry
# i like mango

        




# x=input("enter a value: ")
# reverse=x[::-1]
# print(reverse)
# if (x==reverse):
#     print("the value is palindrome")
# else:
#     print("not a palindrome")    












# Define the list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Slicing to pick every second element from the start to the end
print(numbers[::2])  # [start:end:step]
# Explanation:
# - start: not provided, so it starts from index 0 (beginning of the list).
# - end: not provided, so it goes until the end of the list.
# - step: 2, so it skips one element and picks every second element.
# Steps:
#   numbers[0] = 1
#   numbers[2] = 3
#   numbers[4] = 5
#   numbers[6] = 7
#   numbers[8] = 9
# Output: [1, 3, 5, 7, 9]

# Slicing to pick every second element, but in reverse order
print(numbers[::-2])  # [start:end:step]
# Explanation:
# - start: not provided, so it starts from the last element of the list.
# - end: not provided, so it goes until the first element of the list.
# - step: -2, so it moves backward and picks every second element.
# Steps:
#   numbers[9] = 10
#   numbers[7] = 8
#   numbers[5] = 6
#   numbers[3] = 4
#   numbers[1] = 2
# Output: [10, 8, 6, 4, 2]

















































