from math_operations import add_numbers
from text_processing import capitalize_string

if __name__ == "__main__":
  
  try: 
    result1 = add_numbers(5, 7)
    print("Result of adding numbers:", result1)
  except: 
    print("Number addition function not yet implemented correctly")
  try:
    result2 = capitalize_string("hello, world")
    print("Capitalized string:", result2)
  except:
    print("Capitalize function still needed)
