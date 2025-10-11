print(pow(2,3))

b = abs(-10)
print(b)


"""

### 📘 Python Built-in Functions with Examples

| Function        | Description                                                  | Example                                      |
|----------------|--------------------------------------------------------------|----------------------------------------------|
| `abs()`         | Returns absolute value of a number                          | `abs(-5)` → `5`                              |
| `all()`         | True if all elements are true                               | `all([True, True])` → `True`                 |
| `any()`         | True if any element is true                                 | `any([False, True])` → `True`                |
| `ascii()`       | ASCII representation of object                              | `ascii('ñ')` → `'\\xf1'`                      |
| `bin()`         | Binary representation of integer                            | `bin(5)` → `'0b101'`                          |
| `bool()`        | Converts value to Boolean                                   | `bool(0)` → `False`                          |
| `bytearray()`   | Returns byte array                                          | `bytearray("abc", "utf-8")` → `b'abc'`       |
| `bytes()`       | Returns bytes object                                        | `bytes("abc", "utf-8")` → `b'abc'`           |
| `callable()`    | Checks if object is callable                                | `callable(print)` → `True`                   |
| `chr()`         | Unicode character from code                                 | `chr(97)` → `'a'`                             |
| `classmethod()` | Converts method to class method                             | `@classmethod` decorator                     |
| `compile()`     | Compiles source into code object                            | `compile('print(1)', '', 'exec')`            |
| `complex()`     | Creates complex number                                      | `complex(2, 3)` → `(2+3j)`                   |
| `delattr()`     | Deletes attribute from object                               | `delattr(obj, 'attr')`                       |
| `dict()`        | Creates dictionary                                          | `dict(a=1, b=2)` → `{'a': 1, 'b': 2}`         |
| `dir()`         | Lists attributes of object                                  | `dir([])` → `['__add__', '__class__', ...]`  |
| `divmod()`      | Returns quotient and remainder                              | `divmod(8, 3)` → `(2, 2)`                     |
| `enumerate()`   | Enumerates iterable                                         | `enumerate(['a','b'])` → `[(0, 'a'), (1, 'b')]` |
| `eval()`        | Evaluates expression                                        | `eval('2+3')` → `5`                           |
| `exec()`        | Executes Python code                                        | `exec('print("Hi")')` → `Hi`                 |
| `filter()`      | Filters iterable with function                              | `filter(lambda x: x>0, [-1,2])` → `[2]`       |
| `float()`       | Converts to float                                           | `float('3.14')` → `3.14`                      |
| `format()`      | Formats value                                               | `format(5.678, ".2f")` → `'5.68'`             |
| `frozenset()`   | Immutable set                                               | `frozenset([1,2])` → `frozenset({1, 2})`      |
| `getattr()`     | Gets attribute value                                        | `getattr(obj, 'attr')`                       |
| `globals()`     | Returns global symbol table                                 | `globals()` → dictionary of global vars      |
| `hasattr()`     | Checks if object has attribute                              | `hasattr(obj, 'attr')` → `True/False`        |
| `hash()`        | Returns hash value                                          | `hash("hello")` → integer                    |
| `help()`        | Launches help utility                                       | `help(str)` → shows string methods           |
| `hex()`         | Converts to hexadecimal                                     | `hex(255)` → `'0xff'`                         |
| `id()`          | Returns object ID                                           | `id(5)` → memory address                     |
| `input()`       | Gets user input                                             | `input("Name: ")`                            |
| `int()`         | Converts to integer                                         | `int("5")` → `5`                              |
| `isinstance()`  | Checks instance type                                        | `isinstance(5, int)` → `True`                |
| `issubclass()`  | Checks subclass relationship                                | `issubclass(bool, int)` → `True`             |
| `iter()`        | Returns iterator                                            | `iter([1,2])` → iterator object              |
| `len()`         | Returns length                                              | `len("abc")` → `3`                            |
| `list()`        | Creates list                                                | `list("abc")` → `['a','b','c']`              |
| `locals()`      | Returns local symbol table                                  | `locals()` → dictionary of local vars        |
| `map()`         | Applies function to iterable                                | `map(str.upper, ['a','b'])` → `['A','B']`    |
| `max()`         | Returns max value                                           | `max([1,2,3])` → `3`                          |
| `memoryview()`  | Returns memory view object                                  | `memoryview(b'abc')`                         |
| `min()`         | Returns min value                                           | `min([1,2,3])` → `1`                          |
| `next()`        | Gets next item from iterator                                | `next(iter([1,2]))` → `1`                     |
| `object()`      | Creates base object                                         | `object()`                                   |
| `oct()`         | Converts to octal                                           | `oct(8)` → `'0o10'`                           |
| `open()`        | Opens file                                                  | `open('file.txt')`                           |
| `ord()`         | Unicode code of character                                   | `ord('a')` → `97`                             |
| `pow()`         | Raises to power                                             | `pow(2, 3)` → `8`                             |
| `print()`       | Prints to console                                           | `print("Hello")`                             |
| `property()`    | Creates property                                            | `@property` decorator                        |
| `range()`       | Sequence of numbers                                         | `range(3)` → `0,1,2`                          |
| `repr()`        | String representation                                       | `repr(5)` → `'5'`                             |
| `reversed()`    | Reverses iterable                                           | `reversed([1,2])` → `[2,1]`                   |
| `round()`       | Rounds number                                               | `round(3.1415, 2)` → `3.14`                   |
| `set()`         | Creates set                                                 | `set([1,2,2])` → `{1,2}`                      |
| `setattr()`     | Sets attribute                                              | `setattr(obj, 'attr', val)`                  |
| `slice()`       | Creates slice object                                        | `slice(1,3)` → `[1:3]`                        |
| `sorted()`      | Sorts iterable                                              | `sorted([3,1])` → `[1,3]`                     |
| `staticmethod()`| Creates static method                                      | `@staticmethod` decorator                    |
| `str()`         | Converts to string                                          | `str(5)` → `'5'`                              |
| `sum()`         | Sums iterable                                               | `sum([1,2,3])` → `6`                          |
| `super()`       | Access parent class                                        | `super().method()`                           |
| `tuple()`       | Creates tuple                                               | `tuple([1,2])` → `(1,2)`                      |
| `type()`        | Returns type                                                | `type(5)` → `<class 'int'>`                  |
| `vars()`        | Returns `__dict__` of object                                | `vars(obj)`                                  |
| `zip()`         | Combines iterables                                          | `zip([1,2], ['a','b'])` → `[(1,'a'),(2,'b')]` |


"""