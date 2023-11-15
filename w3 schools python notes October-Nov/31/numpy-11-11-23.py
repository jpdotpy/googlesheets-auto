#f = open("myfile.txt", "x")
#f.open()

#to create a file ^^

print('')

#import os
#os.remove("myfile.txt")

#to delete a file, import the os module and run its os.remove() function ^^


import numpy 
arr = numpy.array([1, 2, 3, 4, 5])
print(arr)

print('')

import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6])
print(arr)

print('')

import numpy as np
print(np.__version__)

print('')

import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))

#Numpy is used to work with arrays
#the array object in numpy is called "ndarray"
#we can create a Numpy ndarray object using the array() function

#to create an ndarray we can pass a list, tuple, or any array like
#object into the array() method and it will converted intoan ndarray

#nested array are arrays that have arrays as their elements

#0-D arrays or scalars are the elements in an array
#each value in an array is a 0-D array

print('')

#create a 0-D array
import numpy as np
arr = np.array(42)
print(arr)

print('')

#an array that has 0-D arrays as its elements is called uuni-dimensional or 1-D array
#these are the most common and basicc arrays

#create a 1-D array containing the values 1,2,3,4,5

import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print('')

#an array that has 1-d arrays as its elements is called a 2-D array
#these are often used to represent matrix or 2nd order tensors

#numpy has a whole sub module dedicated towards matrix operations called numpy.may

#create a 2-D array containing two arrays with the values 123 and 456

import numpy as np 
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)

print('')

#an array that has 2-D arrays (matrices) as its elements is called a 3-D array
#these are often used to represent a 3rd order tensor

#create a 3-D array with two 2-D arrays, both containing two arrays with the values 1,2,3 and 4,5,6

import numpy as np
arr = np.array([[[1, 2, 3],[4, 5, 6]],[[1, 2, 3], [4, 5, 6]]])
print(arr)

print('')

#Numpy arrays provides the ndim attribute that returns an integer that tells us how mnay dimensions the array have

import numpy as np 

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

print('')

#an array can have any number of dimensions 
#when the array is created, you can define the number of dimensions by using the ndmin argument

#create an array with 5 dimensions and verify that is has 5 dimensions 

import numpy as np
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print("number of dimensions :", arr.ndim)

print('')

#array indexing is the same as accessing an array element
#you can access an array element by reffering to its index number
#the indexes in Numpy arrays start with 0

import numpy as np 
arr = np.array([1, 2, 3, 4])
print(arr[0])

print('')

#get third and fourt elements from the following array and add them

import numpy as np
arr = np.array([1, 2, 3, 4])
print(arr[2] + arr[3])

print('')

#to access elements from 2-D arrays we can use coma seperated integers
#representing the dimention and the index of the element
#Think of 2-D arrays like a table with row and colums where the dimension represents the row and the index represents the colum

#access the element on the first row, second column

import numpy as np
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('2nd element on the 1st row: ', arr[0,1])

print('')


#Acess the element on the 2nd row, 5th comumn
import numpy as np
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('2nd element on 1st row: ', arr[1, 4])

print('')

#to access elements from 3-D arrays we can use comma sepeerated integers representing the dimensions and the index of the lement

#access the 3rd element of the second array of the first array

import numpy as np
arr = np.array([[[1,2,3], [4,5,6]], [[7,8,9],[10,11,12]]])
print(arr[0, 1,2])

#the reason it's [0,1,2] instea of [2,1,0] is
#the first number represents the first dimention whih contains two arrays and since we selected 0 we are left with the first array
#the second numnber represents the second dimension which also contains two arrays
#since we selected 1, we are left with the second array
#the 3rd number represents the third dimensiion which ontains 3 valued
#since we slected '2' we ended up with the 3rd value

print('')
#use negative indexing to access an array from the end
#print the last element from the second dimension
import numpy as np
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('Last element from 2nd dim: ', arr[1, -1])

print('')

#Slicing in python means taking elements from one given index to another given index
#we pass slicd instead of index like this: [start:end]
#we can also define the step like this: [start:end:step]
#if we dont pass start its considered 0
#if we dont pass end its considered length of array in that dimension
#if we dont pass step its considered 1

#slice elements from index 1 to index 5 from the following array

import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])

print('')

#slice elements from index 4 to the end of the array
import numpy as np3
arr = np.array([1,2,3,4,5,6,7])
print(arr[4:])

print('')

#slice eleents from the beginning to index 4(not included)
import numpy as np
arr = ([1,2,3,4,5,6,7])
print(arr[:4])

print('')

#use the minus operator to refer to an index from the end
#slice from the index 3 from the end to index 1 from the end
import numpy as np
arr = ([1,2,3,4,5,6,7])
print(arr[-3:-1])

print('')

#use the step value to determine the step of the slicing
import numpy as np
arr = np.array([1,2,3,4,5,6,7])
print(arr[1:5:2])

print('')

#return every other element from the entire array
import numpy as np
arr = ([1,2,3,4,5,6,7])
print(arr[::2])

print('')

#from the second element, slice element from index 1 to index 4
import numpy as np 
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(arr[1,1:4])


print('')

#from  both elements return index 2
import numpy as np
arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr[0:2,2])

print('')

#from both elements, slice index 1 to index 4, this will return a 2-D awaay

import numpy as np
arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr[0:2,1:4])

print('')

#numpy has some extra data types with one character like i for integers and u for unsigned integers etc
#Below is a list of all data types in Numpy and the characters used to represent them
#i - integer
#b - boolean
#u - unsigned integer
#f - float 
#c - complext float
#m - timedelta
#M - datetime
#O - object 
#S - string
#U - unicode string
#V - fixed chink of memory for other type (avoid)

#the Numpy array object has a property called "dtype" that returns the data type of the array
#Get the data type of an array object 

import numpy as np
arr = np.array([1,2,3,4])
print(arr.dtype)

print('')

import numpy as np
arr = np.array(['apple', 'banana', 'cherry'])
print(arr.dtype)

print('')

#we can use the array() function to create arrays, this function can take an optional argument: dtype
#that allows us to define the expected data type of the arra leements

#create an array with data type string
import numpy as np
arr = np.array([1,2,3,4], dtype='S')
print(arr)
print(arr.dtype)

print('')

#for i, u, f, S, and U we can define sizr as well
#create an array with data type 4 bytes integer
import numpy as np
arr = np.array([1,2,3,4], dtype='i4')

print(arr)
print(arr.dtype)

print('')

#if a type is given in which elements cant be casted then NumPy will raise a ValueError
#In python ValueError is raised when the type of passed argument to a function is unexpected/incorrect

#a non integer string like 'a' can not be converted to integer (will raise an error)
#import numpy as np
#arr = np.array(['a', '2', '3'], dtype='i')
#print(arr)
#will return an error ^

#the best way to change the data type of an existing array is to make a copy of the array with the "astype()" method
#the astype() function created a copy of the array and allows you to specify the data type as a parameter
#the data type can be specified using a string like 'f' for float, 'i' for integer, etc
#or you can use the data type dieectly like float for float and int for intefer

#change the data type from float ot integer  by using 'i' as parameter value
import numpy as np
arr = np.array([1.1,2.1,3.1])
newarr = arr.astype('i')
print(newarr)
print(newarr.dtype)

print('')


import numpy as np
arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype(int)
print(newarr)
print(newarr.dtype) 

print('')

import numpy as np
arr = np.array([1, 0, 3])
newarr = arr.astype(bool)
print(newarr)
print(newarr.dtype)