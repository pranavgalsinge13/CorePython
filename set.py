'''s={1,2,3,4,5,6,6,5,4,2,3,1,7}
print(s)

# unordered collection of uniique elements
# sets are mutable
# it may returned the changed sequence of the element.
# the set is created by using the built in function named as set()

# creating Empty set
set1=set()
set2={'Abc',2,3,'Xyz'}

# printing set value
print(set2)

# Adding Element to the set
set2.add(1)
print(set2)

# Removing element from the set
set2.remove(2)
print(set2)'''

x={"a","b","c"}
y={"c","d","e"}
z={"f","g","c"}
x.intersection_update(y,z)
print(x)


set3={1,1,1,2,3,4,5,5,3,4,7,6}
