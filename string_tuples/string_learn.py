# string
# core string , index , slicing , encoding-decoding

name = "sachin"
profession = "coder"

# indexing
print(name[0])

# slicing
print(name[0:3])  # from 0 to 2
print(name[2:])   # from 2 to end
print(name[:3])   # from start to 2

print(name[-1])  # last character
print(name[-2:])  # last two characters

# reversing a string
print(name[::-1])  # reverse the string

# concatenation
print(name + " " + profession)  # using + operator

# f-string formatting
print(f"{name} is a {profession}")  # using f-string

# encoding and decoding
encoded_name = name.encode('utf-8')  # encoding to bytes
print(encoded_name)  # prints bytes representation
decoded_name = encoded_name.decode('utf-8')  # decoding back to string
print(decoded_name)  # prints original string

# string methods
print(name.upper())  # convert to uppercase
print(name.lower())  # convert to lowercase
print(name.title())  # convert to title case
print(name.replace('a', 'o'))  # replace 'a' with 'o'
print(name.find('c'))  # find index of 'c'
print(name.count('a'))  # count occurrences of 'a'

# checking if string starts or ends with a substring
print(name.startswith('sa'))  # check if starts with 'sa'
print(name.endswith('in'))  # check if ends with 'in'

# splitting and joining strings
print(name.split('a'))  # split by 'a'
print(', '.join(['sachin', 'coder']))  # join list with ', '

# stripping whitespace
print("  sachin  ".strip())  # remove leading and trailing whitespace

# checking if string is alphanumeric
print(name.isalnum())  # check if all characters are alphanumeric


