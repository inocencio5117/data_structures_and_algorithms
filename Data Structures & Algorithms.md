# Data Structures & Algorithms

### Source:

[Algorithms and Data Structures Tutorial - Full Course for Beginners](https://www.youtube.com/watch?v=8hly31xKli0&list=PLK_H28cuKDv5AyIl1ZgslA8a0Hk6o4afd&index=47&t=3056s)

# Algorithms:

## Concept:

- A set of steps or instructions to complete e task
- Examples:
    - Recipe
    - Mourning routine

## Why learn?

- To solve a certain problem properly and quicker
- To make the code scalable
- To save memory (that is quite expensive)

## How It should be?

- The steps need to be in a specific order of steps
- The steps need to be distinctive
- Should produce a result
- Should have a clearly defined problem statement, input and output
- Should complete in a finite amount of time

## How to choose a good algorithm

- Correctness
- Efficiency
    - Measure by time and space

- Binary search
    - The numbers must be sorted for the right use of this algorithm
    - Steps:
    1. Define the middle position of the list
    2. Compare the element found in step one with the target element
    3. If it don’t match in step two, verify if the target element is higher or lower than the middle element on the list
        1. If is greater, get the half to the end of the list and get back to step two
        2. If is smaller, get the half to the beginning of the list and get back to step two
    
- Linear search
    - It sequentially checks each element of the list until a match is found or the whole list has been searched

- Time complexity sheet cheat:

![https://he-s3.s3.amazonaws.com/media/uploads/c950295.png](https://he-s3.s3.amazonaws.com/media/uploads/c950295.png)

![https://res.cloudinary.com/practicaldev/image/fetch/s--ark_FZG1--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/1omv0tmikzeaj24z8ps2.jpeg](https://res.cloudinary.com/practicaldev/image/fetch/s--ark_FZG1--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/1omv0tmikzeaj24z8ps2.jpeg)

## Principles of Big O:

### Concept:

- Theoretical definition of the complexity of an algorithm as a function of the size
- As well defined as the upper bounds of the algorithm
- O → Order of magnitude of complexity
- ($n$) → A function of the size
- Examples:
    - Linear search: O($n$)
    - Binary search O($log_n$)

### Notations:

### Time complexity:

- O($1$) → Constant time
- O($log_n$) or O($ln_n$) → logarithmic time
- O($n$) → Linear time
- O($n²$) → Quadratic time (or runtime)
- O($n³$) → Cubic runtime
- O($n.log_n$) → Quasi-linear runtime
    - Lies between a linear and a quadratic runtime
    - Example: Merge sort
- O($n^k$) → Polynomial runtime
    - Quadratic and cubic are polynomial
- O($x^n$) → Exponential runtime
    - Considered not efficient
    - Example: Brute force
- O($n!$) → Factorial runtime

### Defining algorithm efficiency:

- The efficiency is defined by the worst case scenario runtime

### Space complexity:

- Iterate implementation → O($n$)
- Recursive implementation → O($log_n$)
    - Consumes more half memory for each recursion (n + n/2 + n/4 ...)
    - Depends on how the programming language works
    - Python “don’t like” recursive implementation
    - Swift → tail call optimization
    

## Merge Sort:

> Concept:
> 
> 
> Conceptually, a merge sort works as follows:
> 
> 1. Divide the unsorted list into *n* sublists, each containing one element (a list of one element is considered sorted).
> 2. Repeatedly merge sublists to produce new sorted sublists until there is only one sublist remaining. This will be the sorted list.

[Merge sort - Wikipedia](https://en.wikipedia.org/wiki/Merge_sort)

- In this algorithm is used the strategy of d*ivide and conquer*
- Steps:
    - *`Divide: Find the midpoint of the list and divide into sublists`*
    - *`Conquer: Recursively sort the sublists in previous step`*
    - *`Combine: Merge the sorted sublists created in previous step`*

---

# Data Structures:

## Concept:

> “Data Structures are **a specialized means of organizing and storing data in computers** in such a way that we can perform operations on the stored data more efficiently [...]”
> 

[](https://towardsdatascience.com/8-common-data-structures-every-programmer-must-know-171acf6a1a42)

### Operations on Data Structures:

- Access and read values
    - Index
- Search for an arbitrary value
- Insert values at any point into the structure
- Delete values in the structure

## Arrays:

### Concept:

- Collection of values
- Can be heterogeneous or homogeneous
    - Heterogeneous → Store different types of data
    - Homogeneous → only store the same type of data
- Index
    - Position of an specific value inside an array

- How Python do it’s Lists
    - Some programming languages (such Java and Swift) store homogeneous data in an array, and it’s values are in memory
    - But Python, in order to do heterogeneous arrays, use pointers to reference a value instead of the value itself
    

### Types of insert operation in arrays:

- True insert:
    - A value is added in any place in the list
    - It iterates with every index in the list, thus the runtime is O($n$) (linear time)
- Append:
    - Add the item to the end of the list
    - The runtime depends on the programming language used
    - Simplified: O(1)(constant time)
    
- List growth space in Python:
    - 0, 4, 8, 16, 25, 35, 46 ...
    - When the length of the list reach certain number it grows to the next number
    - Amortized Constant Space Complexity
    - The extend() method does a series of append calls until all the elements passed are appended in the list
    
- Delete:
    - As the true insert, this take a move for every single item in the list
    - So the runtime of this operation is O($n$)

## Linked lists:

### Concept:

- Linear data structure that each element in the list is contained in a separated object called a Node
- A Node carries two pieces of information:
    - A value it’s store
    - A reference to the next Node
- The first Node is called Head, and the last the Tail
    - Are special nodes
    - The tail doesn’t point to anything, marking the end of the list
- Nodes are Self Referential Objects
- Doubly Linked List
    - Stores a reference for the next and the previous Node
- Prepend → Add an item to the head
- Append → Add an item to the tail

---