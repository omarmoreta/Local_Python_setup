#1
def max_num(num1, num2, num3):
  largest = 0
  if num1 > num2 and num1 > num3:
    largest = num1
    print(largest)
  elif num2 > num1 and num2 > num3:
    largest = num2
    print(largest)
  else:
    largest = num3
    print(largest)
max_num(0,7,2)

def mult_list(numbers):
  multiple = 1
  for i in numbers:
    multiple = multiple*i
  print(multiple)
mult_list([1,2,3,4,5])

def rev_string(a):
  print(a[::-1])
rev_string('My name pablo')

def num_within(num, first, last):
  if num > first and num < last:
    print(True)
  else:
    print(False)
num_within(3, 2, 5)

def pascal(n):
  for i in range(n+1):
      for j in range(n-i):
         print(end='')

      C = 1
      for j in range(1, i+1):
         print(C, '', sep=' ', end=' ')
         C = C * (i - j) // j
      print()

n = 5
pascal(n)