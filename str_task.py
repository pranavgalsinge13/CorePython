'''str=(input("Enter the string:"))
if(str==str[::-1]):
    print("String is Palindrome")
else:
    print("String is not palindrome")


# using Function palindrome or not

def palindrome(s):
    if s==s[::-1]:
        return True
    else:
        return False

string=(input("Enter the string:"))

if palindrome(string):
    print("string is Palindrome")
else:
    print("string is not palindrome")

# count the number of vowels in string

str=(input("Enter the string:"))
count=0

for ch in str:
    if ch in "aeiouAEIOU":
        count=count+1

print("Number of vowels is:",count)

# print the vowels

str=(input("Enter a String:"))

for ch in str:
    if ch in "aeiouAEIOU":
        print(ch)'''


# Posititve,negative and character

str=(input("Enter a string:"))

for i in range(len(str)):
    print(str[i],"Positive index:",i,"Negative index:",i-len(str))


# count the frequency

str=(input("Enter a string:"))

for ch in str:
    print(ch,"=",str.count(ch))



# count the whitespace in string

str=(input("Enter a string:"))

count=0

for ch in str:
    if ch==" ":
        count=count+1

print("Number of spaces:",count)


# 