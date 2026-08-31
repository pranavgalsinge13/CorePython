# While loop
# 1to10
'''i=1
while(i<=10):
    print(i)
    i+=1

# 10to1
i=10
while(i>=1):
    print(i)
    i-=1

# to take input from the user & print reverse no.
# print 234 in reverse

num=int(input("Enter any Number:"))
rev=0
while(num>0):
    rem=num%10
    rev=rev*10+rem
    num=num//10
print("Reversed Number is:",rev)

# pallindrome  number

num=int(input("Enter any Number:"))
rev=0
temp=num
while(num>0):
    rem=num%10
    rev=rev*10+rem
    num=num//10
print("Reverse Number is:",rev)
if(temp==rev):
    print("Given Number is pallindrome number")
else:
    print("Given Number is not pallindrome number")'''

# Armstrong Number

num=int(input("Enter any Number:"))
sum=0
temp=num
while(num>0):
    rem=num%10
    sum=sum+rem**3
    num=num//10
if(temp==sum):
    print("Given Number is Armstrong")
else:
    print("Given Number is not Armstrong")