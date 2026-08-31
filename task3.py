'''def palindrome(n):
    original=n
    rev=0

    while(n>0):
        digit=n%10
        rev=rev*10+digit
        n=n//10

    if original==rev:
        print("palindrome")
    else:
        print("Not Palindrome")

num=int(input("Enter a number:"))
palindrome(num)
'''



# Armstrong or not Armstrong

def armstrong(n):
    original=n
    sum=0

    while(n>0):
        digit=n%10
        sum=sum+digit**3
        n=n//10

    if original==sum:
        print("Armstrong")
    else:
        print("Not Armstrong")

num=int(input("Enter a number:"))
armstrong(num)