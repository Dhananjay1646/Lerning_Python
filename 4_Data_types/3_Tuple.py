"""
Created by:- Dhananjay D. Magdum
On 22/07/2020 at 23:46

Python Tuples
"""
print("\n********************************************************************************************************************************")

### Python Tuples ###
print("\n### Python Tuples ###\n")

# Tuple is a collection of Python objects much like a list. The sequence of values stored in a tuple can
# be of any type, and they are indexed by integers.
# Values of a tuple are syntactically separated by 'commas'. Although it is not necessary, it is more common
# to define a tuple by closing the sequence of values in parentheses. This helps in understanding the Python
# tuples more easily.

# Creating a Tuple
print("# Creating a Tuple:-\n")

# In Python, tuples are created by placing sequence of values separated by 'comma' with or without the use of
# parentheses for grouping of data sequence.

# Note - Creation of Python tuple without the use of parentheses is known as Tuple Packing.
# Python program to demonstrate addition of elements in a Tuple.

#Creating an empty Tuple 
Tuple1 = () 
print("Initial empty Tuple: ") 
print (Tuple1) 

#Creating a Tuple with the use of string 
Tuple1 = ('Dhe', 'For', 'Dhananjay') 
print("\nTuple with the use of String: ") 
print(Tuple1) 

# Creating a Tuple with the use of list 
list1 = [1, 2, 4, 5, 6]
print("\nTuple using List: ") 
print(tuple(list1))

#Creating a Tuple with the use of built-in function 
Tuple1 = tuple('Dhe says Yes! to himself.') 
print("\nTuple with the use of function: ") 
print(Tuple1) 

print("\n********************************************************************************************************************************")

# Creating a Tuple with Mixed Datatypes.
print("\n# Creating a Tuple with Mixed Datatypes:-\n")

# Tuples can contain any number of elements and of any datatype (like strings, integers, list, etc.). Tuples
# can also be created with a single element, but it is a bit tricky. Having one element in the parentheses is
# not sufficient, there must be a trailing 'comma' to make it a tuple.

#Creating a Tuple with Mixed Datatype 
Tuple1 = (4, 'Welcome', 6.54, 'Dhe') 
print("\nTuple with Mixed Datatypes: ") 
print("Tuple1:- ", Tuple1)
print("\nTuple1[1]:- ", Tuple1[1])

#Creating a Tuple with nested tuples
Tuple1 = (0, 1, 2, 3) 
Tuple2 = ('python', 'language') 
Tuple3 = (Tuple1, Tuple2) 
print("\nTuple with nested tuples: ") 
print("Tuple3:- ", Tuple3)
print("\nTuple3[1]:- ", Tuple3[1])
print("\nTuple3[1][1]:- ", Tuple3[1][1])
print("\nTuple3[0]:- ", Tuple3[0])
print("\nTuple3[0][1]:- ", Tuple3[0][1])
print("\nTuple3[0][2]:- ", Tuple3[0][2])

#Creating a Tuple with repetition 
Tuple1 = ('Dhe',) * 3
print("\nTuple with repetition: ") 
print(Tuple1) 

#Creating a Tuple with the use of loop 
Tuple1 = ('Dhe') 
n = 5
print("\nTuple with a loop") 
for i in range(int(n)): 
	Tuple1 = (Tuple1,) 
	print(Tuple1)
	
print("\nTuple1[0]:- ", Tuple1[0])
# print("\nTuple1[0]:- ", Tuple1[0])

print("\n********************************************************************************************************************************")

# Accessing of Tuples
print("\n# Accessing of Tuples\n")

# Tuples are immutable, and usually, they contain a sequence of heterogeneous elements that are accessed via
# unpacking or indexing (or even by attribute in the case of named tuples).
# Lists are mutable, and their elements are usually homogeneous and are accessed by iterating over the list.

# NOTE : In unpacking of tuple number of variables on left hand side should be equal to number of values in given tuple a.

#Accessing Tuple with Indexing 
Tuple1 = tuple("Dhe") 
print("Second element of Tuple: ", Tuple1[1])
print("First element of Tuple: ", Tuple1[0])
print("Third element of Tuple: ", Tuple1[2])

#Tuple unpacking 
Tuple1 = ("Dhe", "For", "Dhananjay") 

#This line unpack values of Tuple1 
a, b, c = Tuple1 
print("\nValues after unpacking: ") 
print("a:- ", a)
print("b:- ", b)
print("c:- ", c)

print("\n********************************************************************************************************************************")

# Concatenation of Tuples
print("\n# Concatenation of Tuples\n")

# Concatenation of tuple is the process of joining of two or more Tuples. Concatenation is done by the use
# of '+' operator. Concatenation of tuples is done always from the end of the original tuple. Other arithmetic
# operations do not apply on Tuples.
# Note - Only same datatypes can be combined with concatenation, an error arises if a list and a tuple are combined.

# Concatenaton of tuples 
Tuple1 = (0, 1, 2, 3) 
Tuple2 = ('Dhe', 'For', 'Dhananjay') 

Tuple3 = Tuple1 + Tuple2 

# Printing first Tuple 
print("Tuple 1: ")
print(Tuple1) 

# Printing Second Tuple 
print("\nTuple2: ") 
print(Tuple2) 

# Printing Final Tuple 
print("\nTuples after Concatenaton: ") 
print(Tuple3) 

print("\n********************************************************************************************************************************")

# Slicing of Tuple
print("\n# Slicing of Tuple:-\n")

# Slicing of a Tuple is done to fetch a specific range or slice of sub-elements from a Tuple. Slicing can
# also be done to lists and arrays. Indexing in a list results to fetching a single element whereas Slicing
# allows to fetch a set of elements.
# Note - Negative Increment values can also be used to reverse the sequence of Tuples


# Slicing of a Tuple with Numbers
Tuple1 = tuple('DheforDhananjay') 

# Removing First element 
print("Removal of First Element: ") 
print(Tuple1[1:]) 

# Reversing the Tuple 
print("\nTuple after sequence of Element is reversed: ") 
print(Tuple1[::-1]) 

# Printing elements of a Range 
print("\nPrinting elements between Range 4-9: ") 
print(Tuple1[4:9]) 

print("\n********************************************************************************************************************************")

# Deleting a Tuple
print("\n# Deleting a Tuple:-\n")

# Tuples are immutable and hence they do not allow deletion of a part of it. Entire tuple gets deleted by the
# use of del() method.
# Note - Printing of Tuple after deletion results to an Error.


Tuple1 = (0, 1, 2, 3, 4) 
del Tuple1

print("After use of 'del Tuple1' the entire tuple get deleted and so after that if you try to access this tuple, then the error will be displayed." + 
'''

print(Tuple1)

Error:-
NameError: name 'Tuple1' is not defined
''')

print("\n********************************************************************************************************************************")

print('''
\t\t\t# Built-In Methods

# Built-in Function					Description

# all()						Returns true if all element are true or if tuple is empty
# any()						return true if any element of the tuple is true. if tuple is empty, return false
# len()						Returns length of the tuple or size of the tuple
# enumerate()					Returns enumerate object of tuple
# max()						return maximum element of given tuple
# min()						return minimum element of given tuple
# sum()						Sums up the numbers in the tuple
# sorted()					input elements in the tuple and return a new sorted list
# tuple()					Convert an iterable to a tuple.
''')
print("\n********************************************************************************************************************************")