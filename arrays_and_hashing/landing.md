# Arrays and Hashing

## Problems

1. [Contains Duplicate](/arrays_and_hashing/contains_duplicate.py)
2. [Valid Anagram](/arrays_and_hashing/valid_anagram.py)
3. [Two Sum](/arrays_and_hashing/two_sum.py)
4. [Group Anagrams](/arrays_and_hashing/group_anagrams.py)
5. [Top K Elements](/arrays_and_hashing/top_K_elements.py)
6. [Encode and Decode Strings](/arrays_and_hashing/encode_decode_strings.py)
7. [Product of Array Except Self](/arrays_and_hashing/product_of_array_except_self.py)
8. [Valid Sudoku](/arrays_and_hashing/valid_sudoku.py)

## Prerequisites

- [Copies](#copies)
- [Dynamic Arrays](#dynamic-arrays)
- [Hashmaps](#hashmaps)
- [Sets](#sets)
- [Prefix Sum](#prefix-sum)
- [Postfix Sum](#postfix-sum)
- [Pre/Post-fix Product](#pre--post-fix-product)

### Copies

Shallow Copy:
A Shallow Copy creates a new container object in which is stored references to the original objects in the original data structure.
**Changes to objects in the new data structure appear in the objects in the original data structure and vice versa**

```python
   import copy
   shallow_copy = copy.copy(original)
```

Deep Copy:
A Deep Copy creates a new container object and then recursively inserts copies of the items from the original.
**Changes made to the copy do not reflect in the original**

```python
   import copy
   deep_copy = copy.deepcopy(original)
```

### Dynamic Arrays

Dynamic Array: An array that automatically grows when it is at capacity and we try to add a new item. Elements in a Dynamic Array are **stored contiguously** from the start of the array.

Elements can be added to the end of the reserved space of an initial array, **A1**, in constant time until this space is consumed. At this point, a new array, **A2**, is created with a larger size, *(size dependent on the use case but usually doubled)*, and all the elements from A1 are copied to A2.

Performance:
Worst Case: O(n) where n is the number of elements in A1.
Best Case: O(1) where the element can be added directly to A1 in its initial reserved space.

Removing elements from a dynamic array:
To remove an element from the end of a dynamic array, store '0' at the last index occupied by a value.
To remove from a specific index, replace the element at index i with 0 and shift all elements to the right of i left one space.

Resizing a Dynamic Array:
When an array has null or zero data at the right side of the reserved space, the array size can be reduced by freeing the extra memory.
When all the space in a Dynamic Array, A1, is consumed and a new item needs to be added, allocate a larger array, A2, and copy over all the data from A1 to A2, then add the new item.

Dynamic Arrays are implemented in Python by default as Lists.
Operations:

Declare a List:

```python
    list = ["item1", "item2"]
    # Alternatively you can use the Constructor to declare a list.
    list = list(("item1", "item2"))
```

Adding an item to a list:

```python
    list.append("item3")
```

Removing an item from the list using position.

```python
    list.pop()
    # To remove a specific position, specify the index in pop
    list.pop(1)
```

Removing an item from the list using the item.

```python
    # Removes the first appearance of "item1" in the list
    list.remove("item1")
```

Other useful commands:

```python
    # Reverse the list
    list.reverse()
    # Insert an item at a specific position
    list.insert(index, "item")
    # Remove all items from the list.
    list.clear()
    # Count the number of times an item appears in the list.
    list.count("item")
    # Shallow copy the list
    list_copy = list.copy()
```

### Hashmaps

Hashmaps are indexed data structures that make use of a Hash Function to compute keys into corresponding buckets. The Hash Function takes a Key and translates it to the index of a bucket in the bucket list. If a Collision occurs, where different keys correspond to the same bucket index, a list is used in that bucket to store multiple items. The index then also refers to a position in that list. There can only be one of each key in a Hashmap.
*In Python, Dictionaries are HashMaps.*

Declaring a Dictionary:

```python
    # Use curly brackets
    dictionary = {}
    # Can add items to initial dictionary
    dictionary = {"key" : "value"}
```

Access an item in a Dictionary:

```python
    # Get a specific item at a given key
    dictionary.get("key")
    # Get a list of all keys
    keys = dictionary.keys()
    # Get a list of all values
    values = dictionary.values()
    # Get a list of tuples of each Key, Value pair
    items = dictionary.items()
    # Check if a key is in a dictionary
    if "key" in dictionary#
        print("True")
```

Adding an item to a Dictionary:

```python
    # Add directly
    dictionary["key"] = "value"
    # Using update (adds if not in dict, update if is)
    dictionary.update({"key", "value"})
```

Removing items from a dictionary:

```python
    # Remove a specific item
    dictionary.pop("key")
    # Remove the last inserted item
    dictionary.popitem()
    # Remove using del
    del dictionary["key"]
    # Remove the entire dictionary object
    del dictionary
    # Empty the dictionary of all items
    dictionary.clear()
```

### Sets

A type of data structure that stores distinct elements (Unique), i.e, only one of each element can be stored in a set.
Sets can be ordered and unordered.

In Python, sets are **Unchangeable**, meaning once an item is added, it **cannot be changed, only removed**.
*You can still add and remove items from a Set in Python*

Declaring a set:

```python
    # Uses curly brackets
    my_set = {"item", "item2"}
    # Set items can be of any datatype as long as they are unique
    my_set = {"item", 0, True}

    # Arrays can be converted to sets by using the Constructor
    # In this case, duplicates are removed in the set.
    my_array = [1,2,3,3,4]
    my_set = set(my_array)
    # This is useful for finding duplicates in arrays, as the length of the array and set will be different if there is a duplicate present
```

Accessing set items:
*You cannot access specific set items by Index or Key, but you can loop through items and do certain operations.*

```python
    # Loop through set items
    for x in my_set:
        print(x) 
    # Check if an item is in a set
    if "item" in my_set:
        print("In Set")
```

Adding items to a set:

```python
    # Add items to a set using the add function
    my_set.add("item")
    # You can add entire iterables (Lists, Tuples, Dictionaries, Sets...) to a set using update.
    my_set.update(my_other_set)
```

Removing items for a set:

```python
    # Removing using remove (this will raise an error if the item does not exist)
    my_set.remove("item")

    # Removing using Discard (this will NOT raise an error if the item does not exist)
    my_set.discard("item")

    # You can empty a set using clear
    my_set.clear()
```

Union and Intersection and Difference:
*You can use special Union and Intersection commands for manipulating multiple sets in Python*

Union:

```python
    # Union returns a new set that contains all items from the given sets.
    my_union = my_set.union(my_other_set, my_different_set)

    # You can alternatively use the "|" operator to do the same thing
    my_union = my_set | my_other_set | my_different_set

    # This also works with different iterables like Lists and Tuples etc, but only with the ".union" version.
    my_union = my_set.union(my_list)
```

Intersection:

```python
    # Intersection keeps only the duplicates of the given sets. (The items that appear in both sets exclusively)
    my_intersection = my_set.intersection(my_other_set)
    # Again, this works with the "&" operator.
    my_intersection = my_set & my_other_set

    # This also works with different iterables like Lists and Tuples etc, but only with the ".intersection" version.
    my_union = my_set.intersection(my_list)
```

Difference:

```python
    # Difference returns a new set that only contains the items from the FIRST set that are not present in the other sets.
    my_difference = my_set.difference(my_other_set)

    # Like the other two, you can alternatively use the "-" operator.
    my_difference = my_set - my_other_set

    # This also works with different iterables like Lists and Tuples etc, but only with the ".difference" version.
    my_union = my_set.difference(my_list)

    # The symmetric_difference() method will keep only the elements that are NOT present in both sets.
    my_s_difference = my_set.symmetric_difference(my_other_set)
```

This can be explained visually by the following diagram:

![Diagram](https://www.learnbyexample.org/wp-content/uploads/python/Python-Set-Operatioons.png)

### Prefix Sum

What is a Prefix Sum?

A prefix sum at index i is the sum of all elements of the array from the start up to index i, inclusive.
A Prefix Sum Array is an array representation of the Prefix Sum at **every index in a list**.
For example:
*Let A1 = [10, 20, 10, 5, 15]*
The Prefix Sum Array would be:
*A2 = [10, 10+20, 10+20+10, 10+20+10+5, 10+20+10+5+15] = [10, 30, 40, 45, 60]*

We can calculate the prefix sum at a specific index by adding all the items in a list leading up to and including the item at the desired index *as follows*:
prefixSum[0] = 10
prefixSum[1] = 10 + 20 = 30
prefixSum[2] = 10 + 20 + 10 = 40
prefixSum[3] = 10 + 20 + 10 + 5 = 45
prefixSum[4] = 10 + 20 + 10 + 5 + 15 = 60

#### Prefix Sum Array Algorithm

*Time Complexity = O(n)*
*Space Complexity = O(n)*

```python
    input_array = [10, 20, 10, 5, 15]

    # Declare an array of identical size to that of the input array
    prefix_array = [0] * len(input_array)

    # Initialise the first element of the prefix array
    prefix_array[0] = input_array[0]

    # Loop through the remaining elements
    for i in range(1, len(input_array)):
        prefix_array[i] = prefix_array[i - 1] + input_array[i]

    print(prefix_array)  # Output: [10, 30, 40, 45, 60]
```

Visualised:

```utf-8
    For i = 1:
        prefix_array[1 - 1] is prefix_array[0] which is 10.
        input_array[1] is 20.
        10 + 20 = 30.

    prefix_array[1] = 30.

    In one line: 
        prefix_array[1] = 10+20.
    Is the same as:
        prefix_array[i] = prefix_array[i - 1] + input_array[i]
```

### Postfix Sum

This is the same idea as Prefix Sum, but simply reversed. So for every item i, the Postfix Sum is the Sum of all items that proceed it (*Come after it*).

```python
    input_array = [10, 20, 10, 5, 15]

    # Declare an array of identical size to that of the input array
    prefix_array = [0] * len(input_array)

    # Initialise the first element of the prefix array
    prefix_array[len(input_array) -1] = input_array[len(input_array) -1]

    # Loop through the remaining elements
    for i in range(len(input_array)-2, -1, -1):
        prefix_array[i] = prefix_array[i + 1] + input_array[i]

    print(prefix_array)  # Output: [60, 50, 30, 20, 15]
```

### Pre / Post-fix Product

This is exactly the same as Pre / Post-fix sum, but instead of summing the values, we multiply the items to get the product.
