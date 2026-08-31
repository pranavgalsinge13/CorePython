# print even number from 1 to 10 

'''i=1
while (i<=10):
    if i%2==0;
        print(i)
    i=i+1

# Find odd numbers from 1 to 10

i=1
while (i<=10):
    if i%2!=0:
        print(i)
    i=i+1

# Sum of Even number

i=1
sum=0

while (i<=10):
    if i%2==0:
        sum=sum+i
    i=i+1
print("Even sum=",sum)

# Sum of odd numbers

i=1
sum=0

while(i<=10):
    if i%2!=0:
        sum=sum+i
    i=i+1

print("Odd sum=",sum)

# Check whether the sum is even or odd

i=1
sum=0

while(i<=10):
    if i%2!==0:
        sum=sum+i
    i=i+1

if (sum % 2==0):
    print("Sum is even")
else:
    print("Sum is odd")

# find square of 1 to 10

i=1

while (i<=10):
    print(i**2)
    i=i+1


# find cube of 1 to 10

i=1

while (i<=10):
    print(i**3)
    i=i+1

# Even no square and odd no cube

i=1

while(i<=10):
    if i%2==0:
        print(i,"square=",i**2)
    else:
        print(i,"cube=",i**3)

    i=i+1


# Particular number table

num=5
i=1

while(i<=10):
    print(num*i)
    i=i+1

# digit:246

num=int(input("Enter a number:"))
mul=1

while (num>0):
    digit=num%10
    mul=mul*digit
    num=num//10

print("Multiplication is:",mul)'''

# digit:64

num=int(input("Enter a number:"))
sum=0

while (num>0):
    digit=num%10
    sum=sum+digit
    num=num//10

print("sum is:",sum)