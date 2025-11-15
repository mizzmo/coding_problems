# Python Basics

## Contents

1. [Classes](#classes)

## Classes

A class is a way of constructing an object in python.

## Implementation

A class can be created by simply referencing it.

``` python
    # Creating a class
    class MyClass:
        x = 5

    # Creating an object of type MyClass
    obj = MyClass()

    # Accessing a class variable
    class_var = p1.x
```

### Init Method

 All classes have this built in method, which is always executed when the class is initiated.

 __init__() is used to assign values to object properties or to perform operations needed at class creation.

 This solution removes the need to manually set values for each object, instead doing automatically on creation.

 ``` python
    class Person:
        # You can set default values by using x = y
        # This value is used if none is set on object creation.
        def __init__(self, name, age = 18):
            self.name = name
            self.age = age

    p1 = Person("Toby", 21)
    p2 = Person("John")
 ```

### Self

Self is a parameter that references the current instance of the class. (*The class is referencing itself*)

It is used to access class properties such as variables and mehtods.

``` python
    class Person:
        def __init__(self, name):
            self.name = name
    
        def greet(self):
            print("Hello ", self.name)

        def say_hello(self):
            self.greet(self)
```

*While you don't have to use 'self' as the name for this variable, it is convention and makes code more readable to do so.*

### Class Properties

Just like in other OO Languages, you can access properties of a class by using the dot notation 'class.property'.

This is also used to modify the value of properties.

Class properties are shared by all objects of a class.

__When you modify a Class property, it affects all object instances of that class.__

### Instance Properties

These are properties that belong to the specific object.
__When you modify a Instance property, it affects only that object__

``` python
    class Person:
        # Define a class property
        species = "Human"

        def __init__(self, name):
            # Define an Instance property
            self.name = name

    # Modify a instance property
    p1.name = "Greg"
    print(p1.name)

    # Add a new property to the specific object
    p1.gender = "male"
```

*You can add properties to existing classes, but this only applies to the specific object, not all objects, and its probably just best to hardcode them for readability.*

### Class Methods

Methods defined within a class belong to that class and can be called using dot notation (*class.method()*)
__All class methods must have self as their first parameter__

Class methods can modify class properties by using self.

``` python
    class Person:
        def __init__(self, name):
            self.name = name

        # Implement a method to change the instance property 'name'
        def change_name(self, new_name):
            self.name = new_name

    # Use the class method to change the name of P1
    p1.change_name("Jimmy")
```

### __str__

__str__() is a method that is called when an object is printed.
By implementing __str__, we can control what is printed.

``` python
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def __str__(self):
            return f"{self.name} ({self.age})"
```

### Inheritance in Python

Like Java, you can have Parent and Child classes in Python.
To define a Child class, define a class as usual, adding the Parent class as the first parameter.

You can then use all the properties of the Parent class when using the Child class.

Similarly, you can either define a new __init__() for the new Child class, or you can call the __init__() method of the Parent class.

You may also add additional properties while still using the parent __init__ by just putting them below the parent init.

``` python
    # Define a class 'Student' that is a child of 'Person'
    class Student(Person):
        # Use the Parents init method
        def __init__(self, name, last_name):
            Person.__init__(self, name)
            # Add an additional property
            self.last_name = last_name
```

The Super method is used to inherit all the methods and properties from the Parent, without having to directly reference the parent class.
*The below shows the difference when compared to the previous code snippet*

``` python
     # Define a class 'Student' that is a child of 'Person'
    class Student(Person):
        # Use the Parents init method using Super
        def __init__(self, name):
            super().__init__(self, name)
```
