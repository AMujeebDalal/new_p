#Calculator
from replit import clear
from art import calc_logo

print(logo)
def add(n1, n2):
  return n1 + n2

def mul(n1, n2):
  return n1 * n2

def sub(n1,n2):
  return n1 - n2

def div(n1, n2):
  return n1 / n2

operations = {'+': add,
              '*': mul, 
              '-': sub, 
              '/': div }
ops = {}
flag = True
num1 = float(input("Enter the first number: "))
n1 = num1
while flag:
  flag = False
  for symbol in operations:
    print(symbol, end = ' ')
  o_symbol = input("\nPick one of the operations from above.")
  num2 = float(input("Enter the next number: "))
  ops[o_symbol] = num2
  result = operations[o_symbol](num1,num2)
  new = input("Do you want perform more operations? Enter Y to continue: ").lower()
  if new == 'y':
    flag = True
    num1 = result
    clear()
print(n1, end=' ')
for i in ops:
  print(f"{i} {ops[i]} -->", end= ' ')
print(f"= {result}", end = ' ')

