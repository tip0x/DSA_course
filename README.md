# DATA STRUCTURES & ALGORITHM

By **Pasan Premaratne**

[Note to self: "There is one quality which one must possess to win, and that is definiteness of purpose, the knowledge of what one wants, and a burning desire to possess it.]

- **Napoleon Hill, Writer**

## Introduction:

CONSTANT RUNTIME:

POLYNOMIAL RUNTIME: In any given amount of n, its worst case scenario is O(n^k). They are considered efficient if the O value is polynomial and likely used in a system.

EXPONENTIAL RUNTIME: is an algorithm with O value of x number raised to n power. O(x^n)
Examples of use case is a Brute Force; each character added increases the number of combination by an exponential.

Log2 8 = 3

- Logarithmic runtime is defined as O(ln n) suitable for binary search
- Linear runtime O(n)

* Quadratic runtime is defined as O(n^2)

* Cubic runtime is defined as O(n^3)

Sorting Algorithm: Merge sort

- Quasilinear runtime is defined as O(n log n)
- Combinatorial runtime is defined as n!; which is a factorial in a worst case scenario for solving a coordinate problem O(n!)

Two ways of measuring the efficiency of an algorithm;

1.  Time Complexity: How the runtime of algorithm grows as (n) grows larger.
2.  Space Complexity: is the measure of how much working storage is needed as a particular algorithm grows.

Steps to define an algorithm

1.  It need to be in a specific order
2.  The steps need to be distinct
3.  The algorithm should produce a result
4.  It should complete in a finite amount of time.

**Note:**
_The number of times a recursive function calls itself is called a recursive depth._

Tail call Optimization:

## Exploring Arrays

1. How arrays work
2. What are the common operations on an array
3. What are the runtime associated on those operations

Structures of operation:

1.  Accessing and read the value
2.  Searching for an arbitrary value
3.  Inserting a value at any point of the structure
4.  Deleting a value in the structure

**Data Structure**
A data structure is a way of storing data when programming, it is not just the collection of values and the format they are stored in but the relationship between the values in the collection as well as the operations applied on the data stored in the structure.

An **array** is a:

- Contiguous data structure when the values are stored in blocks of memories that are next to each other with no gap, the advantage is that retrieving value is very easy.

* Non-contiguous data structure when the values are stored with a reference to where the next value is. To retrieve that next value the language has to follow that reference also called a pointer to the next block of memory.
  The array can either be homogenous containing same kind of values or heterogenous, meaning it contains any kind of values mixed. These choices also affect the memory relapses of the array.

In python it is mainly referred to as list were as in other programming languages it is called an array.

When an array is stored, a base amount of contiguous memory is allocated as the array stores sometimes referred to as an address.

in an array, assuming the adddress is M, and the sum of elements in an array is N, then the space or allocation required to store that array is; Space = N \* M
to access value in an array, we use the index pointed to the address (M)

{The index value multiply by the amount of storage per element}

3 types of operation considered in an array;

1.  Insert
2.  Append
3.  Extend

    Python does not allocate memory to just one element it wants to add. Instead it allocates four blocks of memory to increase the size to a total contiguous four blocks of memory so it does not resize the list every single time an element is inserted. The growth pattern is 0,4,8,16,25,35,46...
    Some operations do not require space while some do, on an average Append operation takes constant space which is said to be "Ammortized Constant Space Complexity". same is applicable to Insert operation.

# LINKED LIST

This is a linear data structure that each element contain a separate object called a node; which models 2 pieces of information:

1.  An individual item of the data stored
2.  A reference to the next node in the list.
    Nodes are what are called self referential objects.
    Linked list are classified in two;
    a. Singly linked list
    b. Doubly linked list

The (-i) argument;

runs the python repl (Re-evaluate
print loop) in the console to load the content of our file into it for use.

A data is prepend when added to the head of a list, and append when added to the tail, a true insert is when you can insert the data at any point in the list.
