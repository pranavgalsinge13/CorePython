'''d=dict()
print(type(d))   #empty dictionary


s=set()
print(type(s))   #empty set


d={1:'ABC',2:'LMN',3:'XYZ'}

print(d)
print("1st name is "+d[1])
print("2nd name is "+d[3])
print(d.keys())
print(d.values())'''


n=int(input("Enter number of students:"))
students={}

for i in range(n):
    name=input("Enter student name:")
    marks=int(input("Enter marks:"))

    students[name]=marks

print("Student Dictionary:")
print(students)
