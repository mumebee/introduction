# 1: Built-in Module Practice
from random import randint

numbers = [randint(10, 50) for i in range(5)]
print(numbers)
print(max(numbers))
print(sum(numbers)/len(numbers))

# 2. Different Import Styles
"""
Using the math module:
Write a program that:
1. Imports the whole module (import math)
2. Calculates:
• √144
• π × 5
• sin(π/2)
3. Prints results
Then rewrite the same program using:
from math import sqrt, pi, sin
Explain the difference in usage"""

import math
print(math.sqrt(144))
print(math.pi * 5)
print(math.sin(math.pi/2))

from math import sqrt, pi, sin
print(sqrt(144))
print(pi * 5)
print(sin(pi/2))

"""The difference in usage is that when we import the whole module using "import math", we need to prefix the functions and constants
with "math." in order to access them. However, when we use "from math import sqrt, pi, sin", we can directly use the functions and 
constants without the "math." prefix since we imported them specifically. This makes the code cleaner and more concise."""