#A poorly written example of a program in Python. It prompts the user for the number of elements to sum, takes those integers as input, and handles some basic error cases

MAX = 100

def calculate_sum(arr):
   result = 0
   for num in arr:
      result += num
   return result

def main():
   try:
      n = int(input("Enter the number of elements (1-100): "))
      if not 1 <= n <= MAX:
         print("Invalid input. Please provide a number between 1 and 100.")
         return

      arr = []
      print(f"Enter {n} integers:")
      for i in range(n):
         val = input(f"Element {i+1}: ")
         try:
            arr.append(int(val))
         except ValueError:
            print("Invalid input. Please enter valid integers.")
            return

      total = calculate_sum(arr)
      print("Sum of the numbers:", total)

   except KeyboardInterrupt:
      print("\nProgram terminated by user.")

if __name__ == "__main__":
   main()
