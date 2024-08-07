def infix_to_postfix(infix):

  precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
  output = ''
  stack = []

  for char in infix:
    if char.isalnum():
      output += char
    elif char == '(':
      stack.append(char)
    elif char == ')':
      while stack and stack[-1] != '(':
        output += stack.pop()
      stack.pop() 
    else:
      while stack and precedence[char] <= precedence.get(stack[-1], 0):
        output += stack.pop()
      stack.append(char)

  while stack:
    output += stack.pop()

  return output

def evaluate_postfix(postfix_expr, numbers):
  stack = []
  num_index = 0
  for char in postfix_expr:
    if char.isalpha():
      stack.append(numbers[char])
    elif char.isdigit():
      stack.append(int(char))
    else:
      operand2 = stack.pop()
      operand1 = stack.pop()
      if char == '+':
        result = operand1 + operand2
      elif char == '-':
        result = operand1 - operand2
      elif char == '*':
        result = operand1 * operand2
      elif char == '/':
        if operand2 == 0:
          raise ZeroDivisionError("Cannot divide by zero")
        result = operand1 / operand2
      elif char == '^':
        result = operand1 ** operand2
      stack.append(result)
  return stack[0]

infix_expr = input("Enter the infix expression: ")
numbers = {}
for char in infix_expr:
  if char.isalpha():
    if char not in numbers:
      numbers[char] = int(input(f"Enter the value of {char}: "))

postfix_expr = infix_to_postfix(infix_expr)
print("Infix: ", infix_expr)
print("Postfix: ", postfix_expr)
result = evaluate_postfix(postfix_expr, numbers)
print("Result: ", result)