# 1.number is even or odd without using the modulo operator.
#-----------------------------------------------------------
a =int(input("Enter the value :"))
if a & 1 == 0:
 print("it is evennumber")
else:
 print("it is odd number")
# 2. Calculate the square root of a given number
#-----------------------------------------------
b =int(input("ENter the value: "))
print(b ** 0.5)
# 3.Given a list of strings,concatenate them into a single string.
# -----------------------------------------------------------------
c = int(input("c ="))
d = []
for i in range(c):
 e=input()
 d.append(e)
f=' '
for i in d:
 f+=i
f=f.rstrip()
print(f)
# 4. Reverse the order of words in a given sentence.
# ------------------------------------------------------
g = input("ENter sentenc: ")
a= g[::-1]
print(a)
# 6.Remove all vowels from a given string.
# ------------------------------------------------
h = input("Enter the string:")
for i in h:
 if i not in 'aeiou':
    print(i,end='')

# 7.find the sum of all positive numbers and the sum of all negative numbers.
# ---------------
j=[1,2,3,-9,-7,-6,5]
k=0
l=0
for i in j:
 if i>=0:
    k+=i
 else:
    l+=i
print(f"pos : {k}, neg: {l}")
# 8.Find the length of the longest word in a sentence
# ---------------------------------------------------
m = 'manojh kumar tan mass'
n= m.split()
o=0
for i in n:
 p = len(i)
 if p>o:
    o=p
    q=i
print(f"longest word : '{q}' and the len is : '{o}'")
# 9.find the sum of all even numbers and the sum of all odd numbers.
# ----------------------------------------------------------------
r = [7,3,2,8,9,6,5]
s =0
t = 0
for i in r:
 if i % 2==0:
    s+=i
 else:
    t+=i
print(f"even num : '{s}' and odd num : '{t}'")
# 11.Swap two variables without using a third variable.
# ----------------------------------------------------
u =2
v = 3
u=u+v
v=u-v
u=u-v
print(u)
print(v)
# 12.Print the ASCII value of a given character.
# ----------------------------------------------
x=ord('a')
print(x)

# 13.Find the largest number in a list of floating-point numbers.
# --------------------------------------------------------------

list1 =[2.5,5.1,6.9,8.6,8.7]
lar = max(list1)
print(lar)
# 14.Count the number of words in a sentence.
# ------------------------------------------
words = " Vetri is topper"
words = words.split()
count = 0
for i in words:
 print(i)
 count =count+1
print(count)
# 15.Check if a given century year is a leap year.
# ------------------------------------------------
year = int(input("Enter the year:"))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
 print("Leapyaer")
else:
 print("Its not a leap year ")







