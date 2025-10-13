# Arrays and Hashing

## Problems

1. Contains Duplicate

## Prerequisites

- [Copies](#copies)
- [Dynamic Arrays](#dynamic-arrays)
- [Hashmaps](#hashmaps)

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
