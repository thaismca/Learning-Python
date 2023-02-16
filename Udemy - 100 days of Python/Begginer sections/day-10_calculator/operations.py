# functions for operations
def add(n1, n2):
  '''Takes two numbers and returns the sum'''
  return n1 + n2

def subtract(n1, n2):
  '''Takes two numbers and returns the difference'''
  return n1 - n2

def multiply(n1, n2):
  '''Takes two numbers and returns the product'''
  return n1 * n2

def divide(n1, n2):
  '''Takes two numbers and returns the quotient'''
  try:
    return n1 / n2
  except:
    return "Cannot divide by zero"

# operations dictionary
operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

# note that it's possible to add more operations to this calculator,
# # as long as the function is defined and referenced with a symbol in the dictionary