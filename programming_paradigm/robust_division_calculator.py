def safe_divide(numerator, denominator):
   try:
      numerator = float(numerator)
      denominator = float(denominator)
      if denominator == 0:
        return "Error: Cannot divide by zero."
      else:
        return f"The result of the division is {numerator / denominator}."
   except ValueError:
      return "Error: Please enter numeric values only."
import sys
from robust_division_calculator import safe_divide
def main():
   if len(sys.argv)!= 3:
      print("Usage: python main.py ")
      sys.exit(1)
   numerator = sys.argv
   denominator = sys.argv
   result = safe_divide(numerator, denominator)
   print(result)
if __name__ == "__main__":
   main()
