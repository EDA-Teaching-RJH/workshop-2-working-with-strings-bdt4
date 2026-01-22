import math  

def main():
  a = int(input("First number"))
  b = int(input("Second number"))  
  pythag(a, b)

def pythag(a, b):
  c = a**2 + b**2
  number = math.sqrt(c)
  print(number)
    

main()
