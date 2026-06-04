# Python String Methods Quick Reference

## upper()

Converts all characters in a string to uppercase letters. It does not modify the original string because strings are immutable.

```python
text = "hello"
print(text.upper())
# Output: HELLO
```

## lower()

Converts all characters in a string to lowercase letters. This is useful for case-insensitive comparisons.

```python
text = "HELLO"
print(text.lower())
# Output: hello
```

## title()

Converts the first character of each word to uppercase. It is commonly used for formatting names and titles.

```python
text = "python crash course"
print(text.title())
# Output: Python Crash Course
```

## capitalize()

Converts the first character of the string to uppercase and the rest to lowercase. It affects only the first word.

```python
text = "python programming"
print(text.capitalize())
# Output: Python programming
```

## strip()

Removes whitespace from both the beginning and end of a string. It is useful when processing user input.

```python
text = "  hello  "
print(text.strip())
# Output: hello
```

## lstrip()

Removes whitespace from the left side of a string. The right side remains unchanged.

```python
text = "   hello"
print(text.lstrip())
# Output: hello
```

## rstrip()

Removes whitespace from the right side of a string. The left side remains unchanged.

```python
text = "hello   "
print(text.rstrip())
# Output: hello
```

## replace()

Replaces occurrences of a substring with another substring. A new string is returned.

```python
text = "I like Java"
print(text.replace("Java", "Python"))
# Output: I like Python
```

## split()

Splits a string into a list using a separator. The default separator is whitespace.

```python
text = "apple,banana,orange"
print(text.split(","))
# Output: ['apple', 'banana', 'orange']
```

## join()

Combines elements of an iterable into a single string. The string used to call `join()` acts as the separator.

```python
items = ["apple", "banana", "orange"]
print(", ".join(items))
# Output: apple, banana, orange
```

## find()

Returns the index of the first occurrence of a substring. It returns -1 if the substring is not found.

```python
text = "hello world"
print(text.find("world"))
# Output: 6
```

## index()

Returns the index of the first occurrence of a substring. Unlike `find()`, it raises an error if the substring is not found.

```python
text = "hello world"
print(text.index("world"))
# Output: 6
```

## startswith()

Checks whether a string starts with a specified value. It returns either `True` or `False`.

```python
text = "Python Programming"
print(text.startswith("Python"))
# Output: True
```

## endswith()

Checks whether a string ends with a specified value. It returns either `True` or `False`.

```python
text = "report.pdf"
print(text.endswith(".pdf"))
# Output: True
```

## count()

Counts the number of occurrences of a substring. It returns an integer value.

```python
text = "banana"
print(text.count("a"))
# Output: 3
```

## isalpha()

Checks if all characters are alphabetic. Spaces and numbers make it return `False`.

```python
text = "Python"
print(text.isalpha())
# Output: True
```

## isdigit()

Checks if all characters are digits. It is useful for validating numeric input.

```python
text = "12345"
print(text.isdigit())
# Output: True
```

## isalnum()

Checks if all characters are letters or digits. Special characters and spaces are not allowed.

```python
text = "Python123"
print(text.isalnum())
# Output: True
```

## islower()

Checks whether all alphabetic characters are lowercase. It returns a Boolean value.

```python
text = "python"
print(text.islower())
# Output: True
```

## isupper()

Checks whether all alphabetic characters are uppercase. It returns a Boolean value.

```python
text = "PYTHON"
print(text.isupper())
# Output: True
```

## center()

Centers a string within a specified width. Padding spaces are added on both sides.

```python
text = "Python"
print(text.center(12))
# Output: '   Python   '
```

## zfill()

Pads a string with leading zeros until it reaches the specified length. It is often used for formatting numbers.

```python
text = "42"
print(text.zfill(5))
# Output: 00042
```

## format()

Formats strings by inserting values into placeholders. It provides a clean way to build output strings.

```python
name = "Alice"
print("Hello, {}".format(name))
# Output: Hello, Alice
```

## f-strings

F-strings provide a modern and readable way to embed expressions inside strings. They are available in Python 3.6 and later.

```python
name = "Alice"
print(f"Hello, {name}")
# Output: Hello, Alice
```
