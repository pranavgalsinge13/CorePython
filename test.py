# create student.txt and write Welcome to Python

'''f=open("student.txt","w")
f.write("Welcome to Python")
f.close()

# create data.txt and write name,age and city

f=open("data.txt","w")

f.write("Name:Pranav\n")
f.write("Age:20\n")
f.write("City:Pune")

f.close()

# open student.txt in read mode and display complete content

f=open("student.txt","r")
data=f.read()
print(data)
f.close()


# count the no of character in student.txt

f=open("student.txt","r")

data=f.read()
count=len(data)
print("Number of characters:",count)
f.close()

# Append Python File Handling to student.txt

f=open("student.txt","a")
f.write("\nPython File Handling")
f.close()


# create marks.txt and write the given marks

f=open("marks.txt","w")
f.write("Python:80\n")
f.write("Java:75\n")
f.write("Mern Stack:85")

f.close()

# read marks.txt and display each line separately

f=open("marks.txt","r")
for line in f:
    print(line)

f.close()


# create message.txt using x mode

f=open("message.txt","x")
f.write("Hello students")
f.close()

# check whether "python" is present in student.txt

f=open("student.txt","r")
data=f.read()

if "Python" in data:
    print("Python is present in the file")
else:
    print("Python is not present in the file")

f.close()'''


# Write numbers 1 to 10 on new lines then read and display them

f=open("numbers.txt","w")

for i in range(1,11):
    f.write(str(i)+"\n")

f.close()

f=open("numbers.txt","r")

for line in f:
    print(line.strip())

f.close()