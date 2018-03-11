# OOPS-and-FP-exercies
Week 3

Exercise 1. Rewrite the code below using map, reduce and filter. Filter takes a function and a collection. It returns a collection of every item for which the function returned True.


''' people = [{'name': 'Mary', 'height': 160},
          {'name': 'Isla', 'height': 80},
          {'name': 'Sam'}]

height_total = 0
height_count = 0
for person in people:
    if 'height' in person:
        height_total += person['height']
        height_count += 1

if height_count > 0:
    average_height = height_total / height_count

    print (average_height) '''
Exercise 2. Write a generator that creates an endless stream of numbers starting from a value given as argument
with a step size of 5

Exercise 3. Itertools is a python module that helps easily create iterators and generators. Rewrite the following code snippets using itertools.

x = 0
while True:
 x += 1
[1, 2, 3, 4, 5][2:]
[1, 2, 3, 4, 5][:4]
[1, 2, 3] + [4, 5, 6]
zip('abc', [1, 2, 3])

Exercise 4. Rewrite the Sieve challenge in Byte Dev using functional programming tools. 
