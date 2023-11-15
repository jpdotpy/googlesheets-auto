def myFunction() :
    return True 

if myFunction() :
    print("YES!")
else: 
    print("NO")    

x = 200 
print(isinstance(x,int))

print(5 + 4 - 7 + 3)

thislist = ["apple", "banana","cherry"]
print(thislist)
print(len(thislist))

mylist = ["apple", "banana","cherry"]
print(type(mylist))

jp = (100)
print(type(jp))

print('')

thislist = ["apple", "banana", "cherry", "kiwi","pinneapple","mango"]
print(thislist[4:])

print('')

thisotherlist = ['apple', 'banana', 'cherry']
thisotherlist[1] = 'blackcurrant'
print(thisotherlist)

print('')

thislist = ['apple', 'banana','cherry']
thislist[1:3] = ['blackcurrant', 'watermelon']
print(thislist)

print('')

thislist = ['apple', 'banana','cherry']
thislist[1:2] = ['blackcurrant', 'watermelon']
print(thislist)

# this one above (^) is lowkey a mindfuck lols

print('')

thislist = ['apple','banana','cherry']
thislist[1:3] = ['watermelon']
print(thislist)

print('')

thislist = ['apple', 'banana', 'bherry']
thislist.insert(2,'watermelon')
print(thislist)            

print('')

thislist = ['jordans', 'yeezys', 'nike\'s', 'adiddas']
thislist.append("margiela")
print(thislist)

print('')

thislist = ['apple', 'banana', 'cherry']
thislist.insert(1,'pear')
print(thislist)

print('')

thislist = ['apple', 'banana', 'cherry']
tropical = ['mango', 'pineapple', 'papaya']
thislist.extend(tropical)
print(thislist)

print('')

thislist = ['apple', 'banana', 'cherry']
thistuple = ('kiwi', 'orange')
thislist.extend(thistuple)
print(thislist)

print('')

thislist = ['apple','banana', 'cherry']
thislist.remove('banana')
print(thislist)

print('')

thislist = ['apple', 'banana', 'cherry','banana']
thislist.remove('banana')
print(thislist)

# peep how second occurance of banana still shows up ^^

print('')

thislist = ['apple', 'banana', 'cherry']
thislist.pop(1)
print(thislist)

print('')

thislist = ['apple', 'banana', 'cherry']
thislist.pop()
print(thislist)

print('')

thislist = ['apple', 'banana', 'cherry']
del thislist[0]
print(thislist)

print('')

thislist = ['apple','banana','cherry']
del thislist

print('')

thislist = ['apple', 'banana', 'cherry']
thislist.clear()
print(thislist)

print('')

thislist = ['apple', 'banana', 'cherry']
for x in thislist:
    print(x)

print('')

thislist = ['apple','banana','cherry']
for i in range(len(thislist)):
    print(thislist[i])

print('')

thislist = ['apple','banana','cherry']
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1

print('')

thislist = ['apple','banana','cherry']
[print(x) for x in thislist]

# this ^ is faster or "short hand" way to do what line 132-134

print('')

fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']
newlist = []
for x in fruits:
    if 'a' in x:
        newlist.append(x)

print(newlist)  

print('')

# old way ^ 

fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mangos']
newlist = [x for x in fruits if "a" in x]
print(newlist)

# less lines of code way for same result ^

# the syntax is newlist = [expression for item in iterable if condition == True]
# the condition is like a filter that only accepts items that valuate to True ""

newlist = [x for x in fruits if x!= 'apple']
print(newlist)

# "the condition" here is the if x!= 'apple' will return True for all elements 
# but apple making the new list contain all fruits EXCEPT apple 

print('')

newlist = [x for x in fruits]
print(newlist)

print('')

newlist = [x for x in range(10)]
print(newlist)

print('')

newlist = [x for x in range(10) if x < 5]
print(newlist)

newlist = [x.upper() for x in fruits]
print(newlist)

newlist = ["hello" for x in fruits]
print(newlist)

print('')

newlist = [x if x != 'banana' else 'orange' for x in fruits]
print(newlist)

print('')

thislist = ['orange', 'mango', 'kiwi', 'pineapple', 'banana']
thislist.sort()
print(thislist)

print('')

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

print('')
thislist = ['orange', 'apple', 'mango', 'banana', 'pineapple']
thislist.sort(reverse=True)
print(thislist)

print('')

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse=True)
print(thislist)

print('')

def myfunc(n):
    return abs(n- 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key=myfunc)
print(thislist)

# the above sorts the list based on how close the number is to 50 / customizable key = function

print('')

thislist = ['banana', 'Orange', 'Kiwi', 'cherry']
thislist.sort()
print(thislist)

print('')

thislist = ['banana', 'Orange', 'Kiwi,', 'cherry']
thislist.sort(key=str.lower)
print(thislist)
            
print('')

thislist = ['banana', 'Orange', 'Kiwi','cherry']
thislist.reverse()
print(thislist)

print('')

thislist = ['apple', 'banana', 'cherry']
mylist = thislist.copy()
print(mylist)

print()

thislist = ['apple', 'banna', 'cherry']
mylist = list(thislist)
print(mylist)

# that is how u copy a list ^^

print('')

list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

print('')

list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]

for x in list2:
    list1.append(x)

print(list1)


print('')

list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

print('')

thistuple = ('apple', 'banana', 'cherry')
print(thistuple)

print('')

thistuple = ('apple',)
print(type(thistuple))

#NOT A TUPLE UNLESS IT HAS COMMA AT THE END
thistuple = ('apple')
print(type(thistuple))

print('')

x = ('apple', 'banana', 'cherry')
y = list(x)
y[1] = 'kiwi'
x = tuple(y)
print(x)

print('')

thistuple = ("apple", 'banana', 'cherry')
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)

print('')

# you cant changw a tuple or add to it but u can add a tuple to another tuple

thistuple = ('apple', 'bsnna', 'cherry')
y = ('orange',)
thistuple += y

print(thistuple)

# tuples are unchangeable so cant remove items from em but can use the same workaround

thistuple = ('apple', 'banana', 'cherry')
y = (list(thistuple))
y.remove('apple')
thistuple = tuple(y)

print(thistuple)

print('')

# the "del" keyword will delete the tuple completly 

#thistuple = ('apple', 'banana', 'cherry')
#del thistuple
#print(thistuple) || turns up as an error

fruits = ('apple', 'banana', 'cherrry')

print(fruits)

print('')

#packing a tuple ^

fruits = ('apple', 'banana', 'cherry')
(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

print('')

fruits = ('apple', 'banana', 'cherry', 'strawberry', 'rasberry')
(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

# if the number of variables if less than the number of values, adding the * will assign the values assigned to he variables as a list

print('')

fruits = ('apple', 'mango', 'papya', 'pineapple', 'cherry')
(green, *tropic ,red) = fruits
print(green)
print(tropic)
print(red)

print('')

thistuple = ('apple', 'banana', 'cherry')
for x in thistuple:
    print(x)

print('')

thistuple = ('apple', 'banana', 'cherry')
for i in range(len(thistuple)):
    print(thistuple)

print('')

thistuple = ('apple', 'banana', 'cherry')
i = 0 
while i < len(thistuple):
    print(thistuple[i])
    i = i + 1

# this one above didnt come out the way it was intented in the course, look int that further (i did, i put [1] instead of [i] to loop thru

print('')

tuple1 = ('a', 'b', 'c')
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

print('')

fruits = ('apple', 'banana', 'cherry')
mytuple = fruits * 2
print(mytuple)
print('')

tuple = ('9mm', '12guage', 'ak-47',"ak-47",'draco')
print(tuple.index('9mm'))
print(tuple.count("ak-47"))

# tuple methods ^

print(tuple[2:5])

# a "set" is one of the 4 built in data types in python
# data types are used to store collections of data
# there are the 4 built in data types are Lists, Tuples, Sets, Dicts
# lists = [] tuples = () sets = {} dicts = {}

print('')

thisset = {'apple', 'banana', 'cherry'}
print(thisset)

# sets are unordered, unchangable, & dont allow for dupes / they will be ignored

print('')

thisset = {'apple', 'banana', 'cherry','apple'}
print(thisset)

# "True" & 1 are considered the same in sets & will be treated as dupes
#same with "False" & 0

print('')

thisset ={'apple', 'banana','cherry', True, 1, 2}
print(thisset)

print('')

thisset = {'apple', 'banana', 'cherry', False, True, 0}
print(thisset)

print('')

thisset = {'apple','banana', 'cherry'}
print(len(thisset))

print('')

myset = {'apple','banana', 'cherry'}
print(type(myset))

print('')
 # can also be used as "set() with double round-brackets"

thisset = set(('apple', 'banana', 'cherry'))
print(thisset)

#4 collections (arrays) data types in python
#list - ordered, changable, allow dupes
#tuple - ordered, unchangable, allow dupes
#set - unordered, unchangale*(can remove or add), unindexed, no dupes allowed
#dict - ordered (python 3.7+, - unordered), and changable, no dupes allowed

print('')
#no index in sets so cant access by referring to an index or key
# gotta use "for" to loop thru and ask for if a value is present with "in"

thiset = {'apple', 'banana', 'cherry'}
for x in thisset:
    print(x)

print('')

thisset = {'apple', 'banana', 'cherry'}
print('banana' in thiset)

#you can add to a set but cant change its items

print('')

thisset = {'apple', 'banana', 'cherry'}
thisset.add('orange')
print(thisset)

print('')

thisset = {'apple', 'banana','cherry'}
tropical = {'pineapple', 'mango','papaya'}
thisset.update(tropical)
print(thisset)

print('')

#update doesnt have to be another set, could be any iterable object (tuples, dicts, lits, etc)

thisset = {'kiwi', 'banana', 'apple'}
mylist = ["cherry", "orange"]
thisset.update(mylist)
print(thisset)

print('')

thisset = {'apple', 'banana', 'cherry'}
thisset.remove('banana')
print(thisset)

print('')

thisset = {'apple', 'banana', 'cherry'}
thisset.discard('banana')
print(thisset)

print('')

thisset = {'apple', 'banana', 'cherry'}
x = thisset.pop()
print(x)
print(thisset)

print('')

thisset = {'apple', 'banana', 'cherry'}
thisset.clear()
print(thisset)

print('')

#thisset = {'apple', 'banana', 'cherry'}
#del thisset
#print(thisset)

thisset = {'apple', 'banana', 'cherry'}
for x in thisset:
    print(x)

print('')

set1 = {'a', 'b', 'c'}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

print('')

set1 = {'a', 'b', 'c'}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

print('')

#union() and update() do the same thing for sets, inserts all from one to another / both exclude dupes

#intersection_update method will keep only the items present in both sets (ONLY DUPES)

x = {'apple', 'banana', 'cherry'}
y = {'google', 'microsoft', 'apple'}
x.intersection_update(y)
print(x)

print('')

#intersection() returns a new set that only contains the items present in BOTH sets

x = {'apple', 'banana', 'cherry'}
y = {'google', 'microsoft', 'apple'}
z = x.intersection(y)

print(z)

print('')
#symmetric_difference_update() method keeps only the elements NOT present in both sets

x = {'apple', 'banana', 'cherry'}
y = {'google', 'microsoft', 'apple'}
x.symmetric_difference_update(y)
print(x)

print('')

#symmetric_difference() method will return a new set that containts only the elemens NOT present in both sets

x = {'apple', 'banana', 'cherry'}
y = {'google', 'microsoft', 'apple'}
z = x.symmetric_difference(y)
print(z)

print('')

#True & 1 are considered the same value in sets and treated as dupes

x = {'apple', 'bamama', 'cherry', True}
y = {'google', 1, 'apple', 2}                                                                       
z = x.symmetric_difference(y)
print(z)
#dicts are ordered (as of 3.7 and up) changeable and dont allow dupes 
#dicts have curly brakcets & keys:values

print('')

thisdict = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
print(thisdict)

print('')

thisdict = {
    'brand': 'Ford',
    "model": 'Mustang',
    'year': 1964
}
print(thisdict)

print('')

#dicts cannot have two items with the same key
#one will overrite the other

thisdict = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964,

}
print(thisdict)

print('')

print(len(thisdict))

print('')

#the values in dict can be of any data type
#str, bool, int, and list types

thisdict = {
    'brand': 'Ford',
    'electric':'False',
    'year': 1964,
    'colors': ['red', 'white','blue']
}

print(thisdict)

print('')

thisdict = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
    }
print(type(thisdict))

print('')

# dict() constructor to make a dict

thisdict = dict(name = 'Jon', age = 36, country = 'Haiti')
print(thisdict)

print('')

thisdict = {
    'brand': 'Ford',
    'model': 'Mustamg',
    'year': 1964
}
x = thisdict['model']
print(x)

print('')

#get does the same thing as above

x = thisdict.get('model')
print(x)

print('')


#keys() will return a list of all the keys in the dict

x = thisdict.keys()
print(x)

print('')

#the list of keys is a "view of the dict" meaning any changes done to the dict will be reflected in the keys list

car = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
x = car.keys()

print(x) #before the change
car['color'] = 'white'

print(x) #after the change

print('')

x = thisdict.values()
print(x)

print('')

car = {
    'brand': "Ford",
    'model': "Mustang",
    'year': 1964
}

x = car.values()
print(x) #before the change
car['year'] = 2020
print(x) #after the change

print('')

car = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
x = car.values()
print(x) #before the change
car['year'] = 2020
print(x)

print('')

car = {
    'brand':'Ford',
    'model':'Mustang',
    'year': 1964
    }
x = car.values()
print(x) #before the change
car['color'] = 'red'
print(x) #after the change

print('')

x = thisdict.items()
print(x)

#items() method will return each item in a dict as tuples in a list

print('')
print('jp')

car = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}

x = car.items()
print(x) #before the change
print('')
car['color'] = 'red'
print(x) #after the change

print('')


thisdict = {
    'brand':'Ford',
    'model':'Mustang',
    'year': 1964
}
if 'model' in thisdict:
    print("Yes, 'model' is one of the keys in this dict")
          
print('')

#change values of an item in a dict by referring to its key name

thisdict = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
thisdict['year'] = 2018
print(thisdict)

print('')

#update() method will update the dictionary with the items for the given argument
#argument must be a dict or iterable objext with key:value pairs

thisdict = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
thisdict.update({'year':2020})
print(thisdict)

print('')

#add items to a dict by using a new index key and assigning a value to it

thisdict = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
thisdict['color'] = 'red'
print(thisdict)

print('')

#update() method will update the dict with the items from 
#a given argument if the item does not exist the item will be added

thisdict = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
thisdict.update({'color': 'red'})
print(thisdict)

print('')

#remove items with the specified key name using pop() method 
thisdict = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
} 
thisdict.pop('model')
print(thisdict)

print('')

#the popitem() method removes the lasrt inserted item (in versions pre 2/7 a random item is remove)

thisdict = {
    'brand': 'Ford',
    'model':'Mustang',
    'year': 1964
}
thisdict.popitem()
print(thisdict)

print('')

#the del keyword removes the item with the specified key name

thisdict = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
del thisdict['model']
print(thisdict)

print('')

#the del keyword can also delete the dict completly 

#thisdict = {
   # 'brand':'Ford',
  #  'model':'Mustang',
  #  'year': 1964
#}
#print(thisdict)

#above results in error bc thisdict is del'd

#the clear() method empties the dict & prints just "{}"

thisdict = {
    'brand': 'Ford',
    'model':'Mustang',
    'year': 1964
}
thisdict.clear()
print(thisdict)

print('')
#when looping through a dictionary the return value are the keys of the dictionary
#but there are methods to return the values as well

thisdict = {
    'Name': 'JP',
    'DOB': "June 13",
    'Age': 24
}

for x in thisdict:
    print(x)

print('')
#print all the values in the ditionary one by one

for x in thisdict:
    print(thisdict[x])

print('')

#or you can use values() method to return values of a dict
#the syntax below makes the most sense to me

for x in thisdict.values():
    print(x)

print('')
#you can use #keys() method to return the keys of a dict 
#like the original way in lines 928-929

for x in thisdict.keys():
    print(x)

print('')

#loop through both keys and values by using the items() method:

for x,y in thisdict.items():
    print(x,y)

print('')

#make a copy of a dict with the copy() method

thisdict = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
mydict = thisdict.copy()
print(mydict)

print('')

# you can also copy a dict with the dict() function

thisdict = {
    'brand': 'Ford',
    'Model': 'Mustang',
    'year': 1964
}
mydict = dict(thisdict)
print(mydict)

print('')

#a dict can contain a dict, its called a nested dictionary
#pee below

myfamily = {
    'child1' :{
        'name':'Emil',
        'year': 2004
    },
    'child2': {
        'name': 'Tobias',
        'year': 2007
    },
    'child3': {
        'name': 'Linus',
        'year': 2011
    }
}
print(myfamily)

print('')

#create 3 dicts then create one dictionary that will contain 3 others
# pretty much add dicts into new dict

child1 = {
    'name': 'Emil',
    'year': 2004
}
child2 = {
    'name': 'Tobias',
    'year': 2007
}
child3 = {
    'name': 'Linus',
    'year': 2011
}

myfamily = {
    'child1': child1,
    'child2': child2,
    'child3': child3
}
print(myfamily)

print('')

#access items in nested dicts just use the name of the dict
# starting with the outer dict#

print(myfamily["child1"]["name"])

print('')

a = 33
b = 200
if b > a:
    print('b is greater than a')

 #python relies on indentation to define scope in the code (other languages use curly brackets for this)
 # if no indentation in an if statement, will return an error

print('')

#the "elif" keyword is pythons way of saying "if the previous conditions were not true, then try this contdition"

a = 33
b = 33
if b > a:
    print('b is greater than a')
elif a == b:
    print('a and b are equal')

print('')

#else keyword catches anything that isnt caught by the preceeding conditions

a = 200
b = 33
if b > a:
    print('b is greater than a')
elif a == b:
    print('a and b are equal')
else:
    print('a is greater than b')

print('')

#you can have else without the elif

a = 200
b = 33

if b > a:
    print('b is greater than a')
else:
    print('b is not greater than a')

print('')

#if you only have one statement to execture you can put it on the same line as the if statement
#aka short hand if

a = 200
b = 33
if a > b: print('a is greater than b')

print('')

#if only one statement to execute, one for if, one for else, you can put it all on the same line
# one line if else statement

#this technique is known as "Ternary Operators" or "Conditonal Expresions"

a = 2
b = 330
print('A') if a > b else print('B')

print('')

#you can have multiple else statements on the same line

a = 330
b = 330
print('A') if a > b else print('=') if a == b else print('B')

print('')

#and keyword is a logical operator used to combine conditonal statements

a = 200
b = 33
c = 500
if a > b and c > a:
    print('bOTH CONDITONS ARE TRUESKII')

print('')

#or keyword is a logical operator used to combine conditonal statements

a = 200
b = 33
c = 500
if a > b or a > c:
    print("Atleast one of the conditions is TRUE")

print('')

#not keyword is a logical operator used to reverse the result of the conditional statement

a = 33
b = 200
if not a > b:
    print('a is NOT greater than b')

print('')

#nested if statements are if statements inside if statements 

x = 41
if x > 10:
    print("Above ten,")
    if x > 20:
        print('and also above 20!')
    else:
        print('but not above 20')

print('')

#if statements cannot be emty, if by chance 
# you have an if statement with no content put 
# in the "pass" statement to avoice an error

a = 33
b = 200
if b > a:
    pass

#returns nothing lols ^

#python has two primitive loop commands 
# while loops and for loops
# with while loops we can execture a set of statements as long as a condition is true

i = 1
while i < 6:
    print(i)
    i += 1

print('')

#while loop requires relevant vzriables, we define an indexing variable (i) which we set to 1

#with break statement we can stop the loop even if the while conditon is true

i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

print('')

#with the continue statement we can stop the current iteration and continue with the next

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

#note that number 3 is missing in the result ^

print('')

#with the else statement we can run a block of code once when the condition is no longer true

i = 1
while i < 6:
    print(i)
    i += 1
else:
    print('i is no longer less than 6')

print('')

#a for loop is useed for iterating over a sequence (either a list, tuple, dict,set, or string)
#with the for loop we can execute a set of statements, once for each item in a list, tuple, set, etc

fruits = ['apple', 'banana', 'cherry']
for x in fruits:
    print(x)

print('')
#for loop does not require an indexing variable to set beforehand

for x in "banana":
    print(x)

print('')

#with the break statement we can stop the loop before it has looped
#through all the items

fruits = ['apple', 'banana','cherry']
for x in fruits:
    print(x)
    if x == 'banana':
        break

print('')

fruits = ['apple', 'banana', 'cheerry']
for x in fruits:
    print(x)
    if x == 'banana':
        break
    print(x)

print('')

#with continue statment we can stop the current iteration of the loop and conitinue to next

fruits = ['apple', 'banana', 'cherry']
for x in fruits:
    if x == "banana":
        continue
    print(x)

print('')

#we use the range() function to loop through a set of code a specified # of times
# the range function returns a sequence of numbers starting from 0 by defauly and increments by 1 (by defauly) 
# and ends at a specified number

for x in range(6):
    print(x)

#range(6) is not the values of 0-6 but the values 0-5

print('')

#its possible to specify the starting value by adding a paramter: range(2,6) which means 2-6 but not including 6

for x in range(2,6):
    print(x)

print('')

#the range() function defaults to increment the sequence by1 but its possible to specify the increment value by adding 3rd parameter 
#range(2,30,3)

for x in range(2, 30,3):
    print(x)

print('')

#the else keyword in a for loop specifies a block of code to be executed when the loop is finished

for x in range(6):
    print(x)
else:
    print("FINALLY FINISHED!")

print('')

#the else block will NOT be executed if the loop is stopped by a break statememnt

for x in range(6):
    if x ==3: break
    print(x)
else:
    print("FINALLY FINISHED")

print('')

#a nested loop is a loop inside a loop, the inner loop will be executed one time for each iteration of the "outter loop"

adj = ['red','big','tasty']
fruits = ['apple', 'banana','cherry']

for x in adj:
    for y in fruits:
        print(x,y)

print('')

#for loops cannoy be empty but if you for some reason have a for loop
# with no content you can put in a pass statement to avoid error

for x in [0, 1, 2]:
    pass

# a function is a block of code which only runs when its called
# you can pass data known as parameters into a function
# a function can return data as a result

def my_function():
    print("Hello from a function")
my_function()

print('')
#information can be passed into functions as arguments
#arguments are specified after the function name inside the parentheses
#add as many arguments as you want just seperate them with a comma

#def my_funciton(fname):
    #print(fname + " Refsnes")

#my_funciton('Emil')
#my_funciton('Tobias')
#my_funciton('Linus')

print('')

#Arguments are often shortened to args in Python documentations

#the terms parameter and argument can be used for the same thing: information that are passed into a function
#from a fucntions POV a parameter is the variable listed inside the parentheses in the function definiton
#and an argument is the value that is sent to the functnion when its called

#a function must be called with the corrext number of arguments 
#meaning if your function expects 2 arguments you have to call the funcitons with 2 arguments, not more, and not less

def my_function(fname,lname):
    print(fname + "  " + lname)

my_function("Emil", "Refsnes")

print('')

#if you do not know how many arguments that will be passed into your function
#add a * before the parameter name in the function defintion
#this way the function will receive a tuple of arguments, and can access the items accordingly
#call arbitray arg or *args

def my_function(*kids):
    print('the youngest child is ' + kids[2])
my_function('Emil', 'Tobias','Linus')

print('')

#can send arguments with key = value syntax
#this way the order of the arguments does not matter

def my_function(child3,child2,child1):
    print('The youngest child is ' + child3)

my_function(child1 = 'Emil', child2 = 'Tobias', child3 = 'Linus')

print('')
#the phrase keyword arrguments are often shortened to kwargs in python docs

#if you dont know how many kwargs that will be passed into your function
#add two asterisk ** before the patameter name in the function defintion
#youll receive a dictionary of arrguments and can access items accordingly

def my_function(**kid):
    print("His last name is " + kid["lname"])
my_function(fname = 'Tobias', lname = 'Refsnes')

print('')
#keyword aeguments are often shorted to **kwargs in python docs

#defauly parameter value (below)

def my_function(country = 'norway'):
    print('i am from ' + country)

my_function("Haiti")
my_function("Sweden")
my_function('India')
my_function()
my_function('Brazil')

print('')

#you can send any data type of arg to a function (string, number, list, dictionary)
#and it will be treated as an argument, it will still be a list when it reaches the function

def my_function(food):
    for x in food:
        print(x)
fruits = ['apple', 'banana', 'cherry']
my_function(fruits)

print('')

#to let a function return a value use the return statement

def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(5))
print(my_function(9))

print('')

#the function defintions cannot be empty but if you for some reason
#have a function definiton with no content, put in the pass statement to avoid an error

def myfunction():
    pass
#returns nothing lols ^

#recursion means a defined function can call itself
#recursion is a common math and programming concept
#it means that a fucntion can call itself. with this you can loop through data to reach a result
#be careful with recursion it can be easy to slip into writing a function that never terminates
#or one that uses excess amounts of mem or processor power
#however, when written correcntly, recursion can be very efficent and mathematically elegant
#tri_recursion() is a function that we have defined to call itself (recurse)
#we use the "k" variable as the data which decrements (-1) every time we recurse.
#the recursion ends when the conditon is not greaer than 0 (aka when it is 0)

def tri_recursion(k):
    if (k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result
print('\n\nRecursion example results')
tri_recursion(6)

print('')

#lambda can take any number of arguments
#the syntax is lambda arguments : expression
#the expression is executres and result is returned

x = lambda  a : a + 10
print(x(5))

print('')

#lambda functions can take any number of arguments
# here we'll multiply argument a with argument b and return the result back

x = lambda a, b : a * b
print(x(5,6))

print('')

#or here we'll summarize argument a,b, and c and return the result 

x = lambda a, b, c: a + b + c
print(x(5,6,2))

print('')

#the power of lambda is better shown when you use them as an anonymous function
#inside another function
#say you have a function defition that takes one argument and that argument will be multiplied
#with an unkown number

#ex:
def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)
print(mydoubler(11))

print('')

def myfunc(n):
    return lambda a : a * n
my_tripler = myfunc(3)
print(my_tripler(11))

#use function defition to make a doubler and tripler in the same
#program

print('')

def myfunc(n):
    return lambda a : a * n
mydoubler = myfunc(2)
my_tripler = myfunc(3)

print(mydoubler(11))
print(my_tripler(11))



print(lambda a,b : a + b)

print('')

#python does not have built in support for arays but python lists can be used instead

#this shows me how to use LISTS as ARRAYS but to work with arrays in python
# you need to import a library like the NumPy library

#arrays are used to store multiple values in one single variable 

cars = ["Mercedes", 'BMW','Porsche']
print(cars)

print('')

#an array is a special variable which can hold more than one value at a time
#if you have a list of items (like a list of car names)
#storing the cars in single variables looks like
#car1 = "Mercedes"
#car2 = "BMW"
#car3 = "Porsche"

#if you want to loop thoguh the cars and find a specific one, if u had 300 instead of 3 the soliutions is an array
#an arraay can hold many values under a single name, you can access the values by referring to an index number

x = cars[0]
print(x)

print('')

#modify the value of an array

cars[0] = "Ford"
print(cars)

print('')

x = len(cars)
print(x)

print('')

for x in cars:
    print(x)

cars.append('Toyota')
print(cars)

print('')

cars.pop(3)
print(cars)

print('')

cars.remove('Ford')
print(cars)

#"remove()" onlt removes the firs occurance of the specified value
#not the second when dupes are present

print('')

#python is an object oriented programming language
#almost everything in python is an object, with it properties and methods
#A class is like an object contructor or "blueprint" for creating objects

class MyClass:
    x = 5
print(MyClass)

print('')

#we can now use the class named MyClass to create objects
#we're going to create an object named p1 and print the value of x
 
p1 = MyClass()
print(p1.x)

print('')

#all classes have a function called __init__() which is always executed when the class is being 
#initiated. 
#Use the __init__() function to assing values to object properties, or other operations that are
#neccesary to do when an object is being created

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
p1 = Person('John', 36)
print(p1.name)
print(p1.age)

print('')

#the __init__() function is called automaticaly everytime the class is being used to create a new object

class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age
    
    def __str__(self):
        return f"{self.name}({self.age})"
        
p1 = Person('John',36)

print(p1)

print('')

#objects can also contain methods
#methods in objects are functions that belong to the object

#we're inserting a function that prints a greeting and executes it on the p1 object

class Person: 
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

#the self parameter is a refrence to the current instance of the class and is used to access variables that belong to the class
#it does not have to be named "self" you can call it whatever you like but it has to be the first parameter of any function in the class
print('')


class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myfunc(abc):
        print('Hello my name is  ' + abc.name)

p1 = Person('John', 36)
p1.myfunc()

print('')

#modify the properties on ojects like this

p1.age = 40
print(p1.age)

#delete properties on objects by using the del keyword

#del p1.age
#print(p1.age)

#delete entire objects with
#del p1

#use "pass" statement if for some reaosn you have a class definition with no content

class Person:
    pass

print('')

#inheritance allows us to define a class that inherits all the methods and properties from another class
#Parent class is the class beinf inherited from, also base class
#Child class is the class that inherits from another class, also called derived class

#Any class can be a parent class so the syntax is the same as creating any other class

class Person: 
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    
    def printname(self):
        print(self.firstname, self.lastname)
#use the personn class to create an object and then execute the printname method
x = Person('John', 'Doe')
x.printname()

print('')

#to create a class that inherits the functionality from another class,
#send the parent class as a parameter when creating the child class

#create a class named Student which will inherit the properties and methods from the Person class

class Student(Person):
    pass

#use the pass keyword when you do not want to add any other properties or methods to the class ^^

#use Student class to create an object and then execute the printname method

x = Student('Mike', 'Olsen')
x.printname()

print('')

#now we have a child class that inherits the properties and methods from its parent
#We want to add the __init__() function to the child classs (instead of the pass keyword)

class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self,fname,lname)
#the childs __init__() function overrides the inheritance of the parents __init__() function
x = Student('Mike', 'Olsen')
x.printname()

#Python also has a super() function that will make the child class inherit all the methods and properties from its parent

class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)

#by using the super() function you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent
print('')


#Below we will ADD a property called graduationyear to the Student class

class Person: 
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.graduationyear = 2019

x = Student('Mike','Olsen')
print(x.graduationyear)

print('')

#in the eample below, the year 2019 should be a variable, and passed into the Student class when creating student objects
#To do so add another parameter in the __init__() function

#add a year parameter and pass the correct year when creating objects


class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

 
x = Student('Mike', "Olsen", 2019)
print(x.graduationyear)

print('')

#add methods / if you add a method in the child class with the same name as a function in the parent class, the inheritence of the parent
#method will be overridden

#add a method called welcome

class Student(Person):
    def __init__ (self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
x = Student('Mike', 'Olsen', 2019)
x.welcome()

print('')

#an iterator is an object that contans a countable number of values
#it can be iterated upoin, meaning you can traverse through all the values
#in Python, an iterator is an object which implements the iterator protocol
#the iterator protocol consists of the methods __iter__() and __next__()

#lists tuples dicts and sets are all iterable objects, they are iterable containers which you can get an iterator from
#all these objects have a iter() method which is used to get an iterator

#return an iterator from a tuple and print each value

mytuple = ('apple', 'banana', 'cherry')
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

print('')

#strings are iterable objects

mystr = 'banana'
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

print('')

#we can use a "for" loop to iterate through an iterable object

mytuple = ('apple', 'banana', 'cherry')
for x in mytuple:
    print(x)

print('')

#iterate the characters of a string

mystr = 'banana'
for x in mystr:
    print(x)

print('')

#the "for" loop actually creates an iterator object and executes the next() method for each loop

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        x = self.a
        self.a += 1
        return x
myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print('')


#the above would continue forever if you had enough next() statments or if it was used in a for loop
#the prevent the iteration from going on forever, we can use StopIteration statememnt
#in the __next__() method you can add a terminating condigtion to raise an error if the iteration is don a specific # of times

#class MyNumbers:
 #  def __iter__(self):
    #    self.a = 1
    #    return self

   # def __next__(self):
       # if self.a <= 20:
        #    x = self.a
        #    self.a += 1
      #      return x
     #   else:
    #        raise StopIteration
    #
   # myclass = MyNumbers()
   # myiter = iter(myclass)

   #for x in myiter:
    #    print(x)

#the above code conitnues on forever ^^


#Polymorphism means many forms and refers to the methods/functions/operators with the same name that can be executed on many objects or classes

#an example of a python function that can be used on different objects is the len() function

x = 'Hey Jp!'
print(len(x))

print('')

mytuple = ('jp', 'jonathan', 'glorious')
print(len(mytuple))

print('')

thisdict = {
    'brand': 'Ford',
    'model': "Mustang",
    'year' : 1979
}

print(len(thisdict))

#Class polymorphism is where we have multiple classes with the same method name

#or example we have 3 classes car, boat, and plane, and they all have  a method called move()

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive")

class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print('Sail!')

class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def move(self):
        print("fly!")

car1 = Car('Ford', 'Muatang') #creating a car classs
boat2 = Boat('Ibiza', 'Touring 20') #creating a boat class
plane1 = Plane('Boeing', '747') #creating a plane class

for x in (car1, boat2, plane1):
    x.move()


print('')


class Vehicle: 
    def __init__(self, brand, model):
        self.brand = brand 
        self.model = model 

    def move(self):
        print('Move!')

class Car(Vehicle):
    pass

class Boat(Vehicle):
    def move(self):
        print("Sail!")

class Plan(Vehicle):
    def move(self):
        print('Fly!')

car1 = Car("Ford", 'Mustang') #Create a Car object
boat1 = Boat('Ibiza', 'Touring 20') #Create a Boat object
plane1 = Plane('Boeing', '737') #Create a Plane object

for x in (car1, boat1, plane1):
    print(x.brand)

#child classes inherit the properties and methods from the parent class
#in the example above you can see the Car class is empty but it inherits brand, model, and move from Vehicle


print('')

#A varibale is only avaialble from inside the region it is created, this is called "scope"

#a variable created inside a function belongs to the "loval scope" of that function, and can only be used inside that function

def myfunc():
    x = 300
    print(x)

myfunc()

print('')

#x is not availble outside the function but it is avaialble for any function inside the function

#The local variable can be accessed from a function within the function

def myfunc():
    x = 300
    def myinnerfunc():
        print(x)
    myinnerfunc()

print('')

#a global scope is a varibale created in the main body of the python code
#a global variable and belongs to the global scope
#global variables are available from within any scope, global, and local

#A varaible created outside of a function is global and can be used by anyone:

x = 250 

def myfunc():
    print(x)

myfunc() #used by function
print(x) #used outside of function

print('')

#if you operate with the same variable name inside and outside of a function, Python will treat them as two seperate variables
#one aviaalble in the global scope (outside the function) and one available in the local scope (inside the function)

#The function will print the local x and then the code will print the global x 

x = 444

def myfunc():
    x = 444
    print(x)

myfunc()

print(x)

print('')

#if you need to create a global variable but are stuck in the local scope you can use the global keywork
#the globa keyword makes the variable global

def myfunc():
    global x
    x = 404

myfunc()

print(x)

print('')

#can use the global keyword if you want to make a change to a global variable inside a function

#to change the value of a global variable inside a funciton, refer to the variable by using the global keyword

x = 300

def myfunc():
    global x 
    x = 200

myfunc()

print(x)

print('')

import jpModule 
jpModule.greeting('jonathan Pierre')

#my module can contain functions and also variables of all types (arrays, disctionaires, objects, etc)

print('')

import jpModule
from importlib import reload 
reload(jpModule)

import jpModule
a = jpModule.person1['name']
print(a)

print('')

print(jpModule.sosa)

print('')

#make sure to "run" it in the orginal module first then  run it in this
#was giving me errors until i ran it in the other terminal

#you can name a module file whatever you like but it must have the file extension .py

#you can create an alias when you import a module by using the as keyword

import jpModule as jpx 

c = jpx.person1['age']
print(c)

print('')

#built in modules like the "platform" module

import platform
x = platform.system()
print(x)

print('')

#a built in function to list all the function names (or variable names) in a module. the dir() function

#import platform
#x = dir(platform)
#print(x)

#the dir() function can be used on all module, includng the ones you create yourself

#you can choose to import only parts from a module by using the from keyword

from jpModule import person1
print(person1['city'])
#when importing using the 'from' keyword, do NOT use the module name when referring to elements in the module
#For eample its person1['age'] NOT mymodule.person1['age'] 

#a date in python is not a data type of its own, but we can import a module named "datetime" to work with dates as date objects

print('')


import datetime
x  = datetime.datetime.now()
print(x)

print('')

import datetime
x = datetime.datetime.now()
print(x.year)
print(x.strftime('%A'))

print('')

#to create a date, we can use the datetime() class (contrsuctor) of the datetime module
#the datetime() class requires three parameters to create a date: year,month,day

import datetime
x = datetime.datetime(2020, 5, 17)
print(x)

#the datetime() class also takes parameters for time and timezone (hour, minute, second, microsecond, tzone) but theyre optional
#and have a default value of 0, (None for timezone)

print('')

#the datetime object has a method for formatting date objects into readable strings
#the method is called strftime and takes one parameter "format" to specify the format of the returned string

import datetime
x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B"))

print('')

#python has a set of built in math functions, including an etensive math module that allows you to perform mathematical tasks on numbers

#the min() and max() functions can be used to find the lowest or highest value in an iterable

x = min(5, 10, 25)
y = max(5, 10, 25)
print(x)
print(y)

print('')

#the abs ffunction returns the absolute (positive) value of the specified number

x = abs(-7.25)
print(x)

print('')

#the pow(x,y) function returns the value of x to the power of y 
x = pow(4,3)
print(x)

#when you have imported the math module you can start using the methods and constants of the module
#the math.sqrt() method for example returns the square root of a number
print('')


import math 
x = math.sqrt(69)
print(x)

print('')

#the math.ceil() method rounds a number upwards to its nearest interger and the math.floor() method rounds a number down

import math 
x = math.ceil(1.4)
y = math.floor(1.4)
print(x) #returns 2
print(y) #returnd 1


print('')

#The math.pi constant

import math 
x = math.pi
print(x)

print('')

#Python has a built in package called json which can be used to work with JSON data

#import json to import module

#"parse json - convert from json to python" if you have a JSON string you can parse it by using the json.loads() method
#the result will be a python dictionary

import json 
#some JSON
x = '{"name":"John", "age":30, "city":"New York"}'
# parse x 
y = json.loads(x)
#the result is a Python dictionary:
print(y["age"])

print('')

#if you have a python object you can convert it into a JSON string by using the json.dumps() method

import json
# a python object (dict):
x = {
    "name": "John",
    "age":30,
    "city": "New York"
}
#convert to json
y = json.dumps(x)
#result is a a JSON string
print(y)

print('')
# you can convert the following into JSON strings
#dict -> Object
#list -> Array
#tuple -> Array
#string -> String
#int -> Number
#float -> Number
#True -> true
#False -> false
#None -> null

import json
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

print('')

#convert a python object containing all the legal data types

import json 
x = {
    'name': 'John',
    'age': 30,
    'married': True,
    'divorded': False,
    'cildren': ('Ann','Billy'),
    'pets': None,
    'cars': [
        {'model':'BMW 230', 'MPG': 27.5},
        {'mmodel': "Ford Edge", 'MPG': 24.1}
    ]
}
print(json.dumps(x))
print('')

#the example above prints a JSON string but its hard to read, no line breaks or indentations
#use indent parameter to define the number of indents
json.dumps(x, indent=4)
print(json.dumps(x))

print('')

#the json.dumps() method has parameters to order the keys in the result

#use sort_keys parameter to specify if the result should be ordered or not

json.dumps(x, indent=4, sort_keys=True)
print(json.dumps(x))

print('')

#A RegEx or Regular Expression is a sequence of characters that forms a search pattern
#RegEx can be used to check if a string contains the specified search pattern

#Python has a built in package called "re" which can be used to work with reagular expressions
#Import the "re" module
#when you have imported the re module you can start using regular expressions

import re
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
if x:
    print('YES! We have a match!')
else:
    print('Fuck no')

#findall() function returns a list containing all matches
#print a list of all matched

import re
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

#if no matches are found, an empty list returns

import re
txt = "The rain in Spain"
x = re.findall('Portugal', txt)
print(x)

print('')

#the search() function searches the string for a match and returns a match object if theres a match
#if theres more than one match only the first occurance of the match will be returned

#ssearch for the first white space character in the string

import re
txt = "The rain in Spain"
x = re.search("\s", txt)
print("The first white-space character is located in position:", x.start())

#if no matches are found, the value None is returned

print('')

import re 
txt = "The rain in Spain"
x = re.search('Portugal', txt)
print(x)

print('')

#the split function returns a list where the string has been split at each match

import re
txt = "The rain in SoCcal"
x = re.split("\s", txt)
print(x)

print('')

#The sub() function replaces the matches with the text of your choice
import re 
#txt = "The rain in Spain"
#x = re.sub("\s", "9", txt)
#print(x)

#print('')

#you can control the number of replacements by specifying the counr @

#import re
#txt = "The rain in spain"
#x = re.sub("\s","9", txt, 2)
#print(x)


#a match objext is an objext containing information about the search and the result
#if there is no match the value None will be retrn instaed of the match objext

#do a search that will return a match object

#import re
#txt = "The rain in Spain"
#x = re.search("ai", txt)
#print(x) #this will print an objext

print('')

#the match objext has properties and methods used to retrieve info ab the search and the reult:
#.span() returns a tuple containing start-, and the end positions of the match
#.string()returns the string passed into the function
#.group() returns the part of thr string where there was a match

#print the position (start - end positon) of the first match occurance
#the reg ex looks for any words that start with uppercase S
#import re
#txt = "The rain in Spain"
#x = re.search(r"\bS\w+", txt)
#print(x.span())

#print('')

#import re

#txt = "The rain in Spain"
#x = re.search(r"\bS\w+", txt)
#print(x.string)

print('')

#import re 
#txt = "The rain in Spain"
#x = re.search(r"\bS\w+", txt)
#print(x.group())

print('')


print('')

#if there is no match the value None will be returned instead of the match object

import camelcase
c = camelcase.CamelCase()
txt = "hello world"
print(c.hump(txt))

print('')

#the "try" block lets you test a block of code for errors
#the "except" block lets you handle the error
#the "else" block lets you execute the code, regardless of the result of the try and except blocks

#when an erro occurs "exceptions" as we call it, python will normally stop and generate an error message

#these exceptions can be handled using the "try" statement

#the try block will generate an exceptions, because x is not defined
try:
    print(x)
except:
    print('An error occured')

 #you can define as many blocks as you want, if you want to execute a specxial block of code for a special kind of error
 #print one messsage if the try block raises a NameError

print('')

try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")

print('')

try:
    print('Hello')
except:
    print('something else went wrong')
else:
    print('Nothing went wrong')

print('')

#the "finally" block, if specified will be executed reagardless if the try block raises an error or not

try:
    print(x)
except:
    print('Something went wrong')
finally:
    print('The "try except" is finished')


print('')

#this can be useful to close objects and clean up resources
#try to open and write to a file that is not writable

try:
    f = open('demofile.txt')
    try:
        f.write('Lorum Iposum')
    except:
        print("Something went wrong when writing to the file")
    finally:
        f.close()
except:
        print('Something went wrong when opening the file')
    

print("")

#as a python develloper you can choose to throw an exception if a condition occurs
#to throw (or raise) an exception use the "raise" keyword

#x = -1 

#if x < 0:
#    raise Exception("Sorry, no numbers below zero")

#the raise keyword is used to raise an exception
#you can define what kind of error to raise and then the text to print to the user


#if not type(x) is int:
 #   raise TypeError("Only integers are allowed")

#print(x)

print('')

#Python allows for user input
#that means we are able to ask the user for input
#input() method in python 3.6+ or raw_input() in python 2.7-

#username = input("Enter Username")
#print('Username is ' + username)

#python stops executing when it comes to the input() fubction and continues when the user has given some input

print('')

#to make sure a string will display as expected, we can fromat the result with the format() method

#the format() method allows you to format the selected parts of a string
#sometimes there are parts of a text that you do not control, maybe they come from a database or user input
#to control such values, add placeholders (curly brackets {}) in the text, and run the values through the format() method

#add a placeholder where you want to display the price:

price = 49
txt = "The price is {} dollars"
print(txt.format(price))

print('')

price = 49
txt = "the price os {:.2f} dollars"
print(txt.format(price))

#if you want to use mmore values, just add more vsalues to the format() method:


quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno,price))

print('')

#you can use index numbers (a number inside the curly brackets {0}) to be sure the values are placed in the corret placeholders
quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} or {2:.2f}"
print(myorder.format(quantity, itemno, price))

print('')

#also if you want to refer to the same value more than once use the index number

age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old"
print(txt.format(age,name))

#you can also used named indexes by entering a name inside the curly brackets {carname} but then you muse use names when yoe pass the parameter values
#txt.format(carname = "Ford")

print('')

myorder = "I have a {carname}, its a {model}"
print(myorder.format(carname = "Ford", model = "Mustang"))












