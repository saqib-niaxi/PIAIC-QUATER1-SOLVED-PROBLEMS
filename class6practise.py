# Write a program that accepts a sentence and calculate the number of letters and digits.

# Suppose the following input is supplied to the program:

# hello world! 123

# Then, the output should be:

# LETTERS 10

# DIGITS 3
inp = input("Enter a sentence: ")
letters = 0
digits = 0
for i in inp:
    if i.isalpha():
        letters += 1
    elif i.isdigit():
        digits += 1
    else:
        pass
print("LETTERS", letters)
print("DIGITS", digits)
