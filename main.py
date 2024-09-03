# add_numbers
def add_numbers(num1, num2):
  return num1 + num2

result1 = add_numbers(6, 7)
print(result1)

# is_even
def is_even(number):
  return number % 2 == 0

result2 = is_even(4)
print(result2)

# reverse_string
def reverse_string(text):
  return text[::-1]

result3 = reverse_string('My name is, user!')
print(result3)

# count_vowels
def count_vowels(text):
  vowels = "aeiouAEIOU"
  count = sum(1 for char in text if char in vowels)
  return count

result4 = count_vowels('I am doing an assignment.')
print(result4)

# calculate_factorial
def calculate_factorial(n):
  if n == 0:
     return 1
  else:
    factorial = 1
    for i in range(1, n + 1):
      factorial *= i
      return factorial
    
    result5 = calculate_factorial(7)
    print (result5)
    
    # apply_decorator
    def decorator_func(func):
      def wrapper(*args, **kwargs):
        print("Decorator Applied")
        return func(*args, **kwargs)
      return wrapper
    
    def apply_decorator(func):
      return decorator_func(func)
    
    # Example
    def greet(name):
      return f"Welcome to, {name}!"
    
    # Applying the decorator to the greet function
    decorated_greet = apply_decorator(greet)
    
    # calling the decorated function
    result6 = decorated_greet("Moringa")
    print(result6)
    
    # Sequence
    def sort_by_age(list_of_tuples):
     return sorted(list_of_tuples, key=lambda x: x[1])
  
    people = [("John", 20), ("Mary", 25), ("David", 50)]
    sorted_people = sort_by_age(people)
    print("People sorted by age:", sorted_people)
  
    # Set and Dictionaries
    def merge_dicts(dict1, dict2):
      merged = dict1.copy()
      for key, value in dict2.items():
        if key in merged:
          merged[key] += value
        else:
          merged[key] = value
      return merged
    
    dict1 = {'apple': 20, 'banana': 51, 'orange': 10}
    dict2 = {'banana': 30, 'orange': 80, 'grape': 12} 
    
    merged_dict = merge_dicts(dict1, dict2) 
    print("Merged dictionary:", merged_dict)
    
    # Class_creation
    class Car:
      def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
      def display_info(self):
        # Display car info
        print(f"Car Info: {self.year} {self.make} {self.model}")
        
        my_car = Car("Toyota", "Corolla", 2004)
        my_car.display_info()

  
  


    
    
    
    
    