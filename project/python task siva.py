# convert snake case string to camel case string

snake_case = input('Enter the words in snake case:')
print(snake_case.replace("_"," ").title().replace(" ",""))

# Remove lowercase substrings from a given string
import re

string = input("Enter the string :")
a = re.findall('[a-z]+',string)

for i in a:
    print(i,end=' ')

# program that reads a given expression 

expression = input("Enter an expression: ")

result = eval(expression)
print(result,"\n") 

# spaces between words starting with capital letters.

def spaces(text):
    text1 = ""
    for char in text:
        if char.isupper() and text1:
            text1 += " " + char
        else:
            text1 += char
    return text1

input_text = "HelloSivaThisIsManojh"
text = spaces(input_text)

print(input_text)
print(text,"\n")


# split a string with multiple delimiters

def split_pananum(text, delimiters):
    for i in delimiters:
        text = text.replace(i, ' ')
    return text.split()
text = "Hello, siva; this|is manojh"
delimiters = [',', ';', '|', '-']
split_text = split_pananum( text, delimiters)

print( text)
print( split_text,"\n")

# split a string at uppercase letters

def split_uppercase(text):
    split_text = []
    current_word = ""

    for char in text:
        if char.isupper() and current_word:
            split_text.append(current_word)
            current_word = char
        else:
            current_word += char

    split_text.append(current_word)
    return split_text

text = "SplitAStringAtUppercaseLetters"
split_text = split_uppercase(text)

print(text)
print( split_text,"\n")

# alphanumeric characters from a string.
def remove_alphanumeric(text):
    return ''.join(filter(str.isalnum, text))

text = "Hello, Maha! This is an manoj."
text1 = remove_alphanumeric(text)

print( text)
print( text1,"\n")

# remove white spaces

def remove_white_spaces(text):
    return text.replace(" ", "")

text = "Hello,    siva! This  is  manojh."
text1 = remove_white_spaces(text)

print( text)
print( text1,"\n")

# a given year is a leap year.

def leapyear(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

year = int(input("Enter a year: "))
if leapyear(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.") 

# print even numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
        if num % 2 == 0:
            print(num,"\n")

# reversed string
def reverse_words(string):
    words = string.split()
    string1 = ' '.join(words[::-1])
    return string1

string = "Hello maha! This is manojh."
result = reverse_words(string)

print( string)
print( result,"\n")












