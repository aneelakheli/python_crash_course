# Python Data Types - Complete Crash Course Notes

# 1. Lists

A list is an ordered, mutable collection that can store multiple items of different data types. Lists are created using square brackets `[]`.

```python
fruits = ["apple", "banana", "orange"]
```

## Key Characteristics

- Ordered
- Mutable (can be changed)
- Allows duplicates
- Supports indexing and slicing

```python
fruits[0]      # apple
fruits[-1]     # orange
```

## Common Methods

### append()

Adds an item to the end of the list.

```python
fruits.append("grape")
```

### insert()

Adds an item at a specified position.

```python
fruits.insert(1, "mango")
```

### remove()

Removes the first matching item.

```python
fruits.remove("banana")
```

### pop()

Removes and returns an item.

```python
fruits.pop()
```

### sort()

Sorts the list permanently.

```python
numbers = [4, 2, 8, 1]
numbers.sort()
```

### reverse()

Reverses the order of the list.

```python
numbers.reverse()
```

### len()

Returns the number of items.

```python
len(fruits)
```

## List Slicing

```python
numbers = [1,2,3,4,5]

numbers[1:4]
# [2,3,4]

numbers[:3]
# [1,2,3]

numbers[::2]
# [1,3,5]
```

## List Comprehension

Creates lists efficiently.

```python
squares = [x*x for x in range(5)]

# [0,1,4,9,16]
```

---

# 2. Tuples

A tuple is an ordered, immutable collection. Once created, it cannot be modified.

```python
coordinates = (10, 20)
```

## Key Characteristics

- Ordered
- Immutable
- Allows duplicates
- Faster than lists
- Useful for fixed data

## Accessing Elements

```python
coordinates[0]
```

## Tuple Unpacking

```python
x, y = coordinates

print(x)
print(y)
```

## Single Element Tuple

```python
item = (5,)
```

Without the comma, Python treats it as an integer.

## Common Functions

```python
len(coordinates)

max((1,2,3))

min((1,2,3))
```

## Why Use Tuples?

Use tuples when data should not change.

Examples:

```python
days = (
    "Monday",
    "Tuesday",
    "Wednesday"
)
```

---

# 3. Sets

A set is an unordered collection of unique items.

```python
numbers = {1,2,3,4}
```

## Key Characteristics

- Unordered
- Mutable
- No duplicates
- Very fast membership testing

## Creating Sets

```python
names = {"John", "Alice", "Bob"}
```

Or:

```python
names = set()
```

## Adding Items

```python
names.add("Mike")
```

## Removing Items

```python
names.remove("John")
```

Safe removal:

```python
names.discard("John")
```

## Membership Testing

```python
"Alice" in names
```

## Set Operations

### Union

Combines sets.

```python
a = {1,2,3}
b = {3,4,5}

a | b
```

Output:

```python
{1,2,3,4,5}
```

### Intersection

Common elements.

```python
a & b
```

Output:

```python
{3}
```

### Difference

Items only in first set.

```python
a - b
```

Output:

```python
{1,2}
```

### Symmetric Difference

Items not shared.

```python
a ^ b
```

Output:

```python
{1,2,4,5}
```

## Remove Duplicates

```python
numbers = [1,1,2,2,3,3]

unique = list(set(numbers))
```

---

# 4. Dictionaries

A dictionary stores data as key-value pairs.

```python
student = {
    "name": "Alice",
    "age": 20,
    "grade": "A"
}
```

## Key Characteristics

- Mutable
- Fast lookups
- Keys must be unique
- Keys are immutable types

## Access Values

```python
student["name"]
```

Safer approach:

```python
student.get("name")
```

## Add New Values

```python
student["city"] = "Kathmandu"
```

## Update Values

```python
student["age"] = 21
```

## Remove Values

```python
del student["grade"]
```

Or:

```python
student.pop("grade")
```

## Dictionary Methods

### keys()

Returns all keys.

```python
student.keys()
```

### values()

Returns all values.

```python
student.values()
```

### items()

Returns key-value pairs.

```python
student.items()
```

## Looping Through Dictionaries

```python
for key, value in student.items():
    print(key, value)
```

## Nested Dictionaries

```python
students = {
    "student1": {
        "name": "Alice",
        "age": 20
    },
    "student2": {
        "name": "Bob",
        "age": 21
    }
}
```

---

# Choosing the Right Data Type

| Type       | Ordered | Mutable | Duplicates | Use Case            |
| ---------- | ------- | ------- | ---------- | ------------------- |
| List       | Yes     | Yes     | Yes        | Dynamic collections |
| Tuple      | Yes     | No      | Yes        | Fixed data          |
| Set        | No      | Yes     | No         | Unique items        |
| Dictionary | Yes\*   | Yes     | Keys No    | Key-value mapping   |

\*Dictionaries preserve insertion order in Python 3.7+.

---

# Quick Memory Tricks

### List

Think: Shopping List

```python
["milk", "bread", "eggs"]
```

### Tuple

Think: GPS Coordinates

```python
(27.7172, 85.3240)
```

### Set

Think: Unique Student IDs

```python
{101,102,103}
```

### Dictionary

Think: Contact Book

```python
{
    "John": "555-1234",
    "Alice": "555-5678"
}
```

---

# Golden Rule

Use:

- **List** → Ordered data that changes.
- **Tuple** → Ordered data that should never change.
- **Set** → Unique values and fast lookups.
- **Dictionary** → Related information stored as key-value pairs.

Master these four data types and you'll understand about 80% of everyday Python programming.
