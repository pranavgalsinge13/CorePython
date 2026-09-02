# File Handling

# Read Mode

'''f=open("ABC.txt","r")
print(f.read())
f.close()

f=open("ABC.txt","r")
print(f.read(11))
f.close()

f=open("ABC.txt","r")
print(f.readlines())
f.close()

# Using loop
f=open("ABC.txt","r")

for x in f:
    print(x)


# Write mode

f=open("demo.txt","w")
f.write("This File Is for Demo Purpose Only\n")
f.write("Hello Good Morning")
f.close()

# append mode

f=open("demo.txt","a")
f.write("\nNow the file has more content")
f.close()

# Create mode

f=open("write.txt","x")'''

# Delete file
import os
os.remove("ABC.txt")

# checks if file exists, then delete it

import os
if os.path.exists("write.txt"):
    os.remove("write.txt")
else:
    print("The file does not exist")

    

# with statement
with open("demo.txt","r") as f:
    content=f.read();
print(content)