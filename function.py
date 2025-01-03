# def items_add(list,item):
#     list.append(item)

# my_list=[1,2,3,4] 
# items_add(my_list,5)
# print(my_list) 

# [1, 2, 3, 4, 5]
    

# def items_remove(list,item):
#     list.remove(item)
# my_list=[1,2,3,4,5]
# items_remove(my_list,5)
# print(my_list)
    
# [1, 2, 3, 4]



# def add_numbers(a, b):
#     return a + b

# result = add_numbers(5, 10)
# print(result)

# 15

# def sub_numbers(a,b):
#     return a-b
# result=sub_numbers(10,5)
# print(result)



# def check_even_odd(num):
#     if num%2==0:
#         return "even"
#     else:
#         return "odd"
    
# result=check_even_odd(4)
# print(result)
# ##
# even


# def find_largest(a, b, c):
#     return max(a, b, c)

# largest = find_largest(10, 20, 15)
# print(largest)




# def reverse_string(s):
#     return s[::-1]

# reversed_str = reverse_string("hello")
# print(reversed_str)

##
# olleh



# def is_positive(num):
#     return num > 0

# print(is_positive(5))  # True
# print(is_positive(-3))  # False



# def sum_list(numbers):
#     return sum(numbers)

# my_numbers = [1, 2, 3, 4, 5]
# print(sum_list(my_numbers))  # 15



# check palindrome 



# def is_palindrome(a):
#     return a==a[::-1]

# print(is_palindrome("madam"))  # True
# print(is_palindrome("hello"))  # False







# def is_anagram(str1, str2):
#     return sorted(str1) == sorted(str2)

# # Example
# print(is_anagram("listen", "silent"))  # Output: True
# print(is_anagram("hello", "world"))    # Output: False





# def is_anagram(str1, str2):
#     return sorted(str1.lower()) == sorted(str2.lower())

# # Taking user input
# str1 = input("Enter the first string: ")
# str2 = input("Enter the second string: ")


# if is_anagram(str1, str2):
#     print(f'"{str1}" and "{str2}" are anagrams!')
# else:
#     print(f'"{str1}" and "{str2}" are not anagrams.')