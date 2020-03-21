
# 1. List concatenation & join

colors = ['red', 'blue', 'green', 'yellow']

result = ', '.join(colors)
print(result)

# 2. Enumerations

items = ['zero', 'one', 'two', 'three']

print(list(enumerate(items)))

# 3. List comprehension

new_list = [fn(item) for item in a_list if condition(item)]

# 4. Generator expressions

total = sum([num * num for num in range(1, 101)])

total = sum(num * num for num in xrange(1, 101))