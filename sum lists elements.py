def sum_iterative(data):
  """Sums the elements of a list using iteration.

  Args:
      data: A list of numbers.

  Returns:
      The sum of all elements in the list.
  """
  total = 0
  for num in data:
    total += num
  return total

# Example usage
my_list = [1, 2, 3, 4, 5]
sum_result = sum_iterative(my_list)
print("Sum with iteration:", sum_result)


from functools import reduce

def sum_reduce(data):
  """Sums the elements of a list using reduce and an anonymous function.

  Args:
      data: A list of numbers.

  Returns:
      The sum of all elements in the list.
  """
  return reduce(lambda a, b: a + b, data)

# Example usage
my_list = [1, 2, 3, 4, 5]
sum_result = sum_reduce(my_list)
print("Sum with reduce:", sum_result)
