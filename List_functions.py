
# a=[1,2,3,4,5]
# index number of list a
# index = 0,1,2,3,4

# b=a.append(6)
# print(a)    [1, 2, 3, 4, 5, 6]


# b=a.insert(2,10)
# print(a)  [1, 2, 10, 3, 4, 5]

# b=a.remove(3)
# print(a)     [1, 2, 4, 5]

# b=a.pop()
# print(a)    [1, 2, 3, 4]

# a=[1,4,5,8,9,2,3]
# b=a.sort()
# print(a)    [1, 2, 3, 4, 5, 8, 9]

# a=[1,2,3,4,5,6,7,8,9,10]
# b=a.reverse()
# print(a)     [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


# a=[1,2,3,4,5]
# print(len(a))    5

# a=[1,2,3,4,5]
# print(max(a))  5
# print(min(a))  1
# print(sum(a))  15


# a=[1,2,3,4]
# a.extend([5,6,7,8,9,10])
# print(a)           [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# a=(1,2,3,4)
# b=list(a)
# b.append(5)
# print(tuple(b))   (1, 2, 3, 4, 5)



#* to compare two list as a pair.....
# name=["ansi","car","apple"]
# numbers=[1,2,3]
# result=list(zip(name,numbers))
# print(result)   #  [('ansi', 1), ('car', 2), ('apple', 3)]




# pairs = [("red", 1), ("blue", 2), ("green", 3)]

# # Solution
# colors, numbers = zip(*pairs)      # The * operator is used to unpack iterable objects (like lists or tuples) into individual elements
# print(list(colors))  # Output: ['red', 'blue', 'green']
# print(list(numbers))  # Output: [1, 2, 3]




# sentence = "This is a bad idea. Bad weather and bad mood."

# new_sentence = sentence.replace("bad","good")
# print(new_sentence)

# This is a good idea. Bad weather and good mood.



# text = "The secret code is 12345."
# new_text=text.replace("12345","*****")
# print(new_text)

# The secret code is *****.






# sentence = "This is a bad idea. Bad weather and bad mood."

# Invert into

# This is a good idea. Beautiful weather and good mood.


# sentence = "This is a bad idea. Bad weather and bad mood."
# new_sentence=sentence.replace("bad","good").replace("Bad","Beautiful")
# print(new_sentence)

# This is a good idea. Beautiful weather and good mood.




# word = ["car","bus","jeep"]

# a = " ".join(word)
# print(a)

# b = " , ".join(word)
# print(b)

# c=" / ".join(word)
# print(c)
###################
# car bus jeep
# car , bus , jeep
# car / bus / jeep





# # sentence = "This is a bad idea. Bad weather and bad mood."

# # Printing the sentence with newlines
# print("This is a bad idea.\nBad weather and bad mood.")


# This is a bad idea.      
# Bad weather and bad mood.



# sentence = "This is a bad idea. Bad weather and bad mood."

# # Printing the contents of 'sentence' with a newline
# print(sentence.replace(".", ".\n"))

# ####
# This is a bad idea.
#  Bad weather and bad mood.


# sentence = "This is a bad idea. Bad weather and bad mood."

# # Printing the contents of 'sentence' with a newline
# print(sentence.replace(".", ",\n"))

#######
# This is a bad idea,
#  Bad weather and bad mood,





