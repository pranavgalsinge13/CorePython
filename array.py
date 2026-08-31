# array in python

from array import*
a=array('i',[2,4,6,8])
print(a)

import array as arr
a=arr.array('i',[2,4,6,8])
print(a)

# vector-1d array
# scalar-0d array
# tenser-3d array
# matrix-2d array

# add elements

import array as arr
num=arr.array('i',[1,2,3,4,5])
num[0]=0
print(num)

import array as arr
num=arr.array('i',[1,2,3,4,5])
num[2:5]=arr.array('i',[4,6,8])
print(num)

# delete elements

import array as arr
num=arr.array('i',[1,2,3,4,5])
del num[2]
print(num)