
greet_user = lambda name : print('Hello My Dear, ', name)
user_name = input("What is your name? ")
greet_user(user_name)


data = [(3, 11), (1, 7), (7, 8), (16, 88), (23, 15)]

sorted_data = sorted(data, key=lambda x: x[1])

print(sorted_data)

numbers = [1, 2, 3, 4, 5]

squared_numbers = list(map(lambda x: x**2, numbers))

print(squared_numbers)

def greet():
    print("Hello, world!")

greet() 

def add(a, b):
    return a + b

result = add(5, 3)  

def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()       
greet("Alice") 

def multiply(a, b):
    return a * b

result = multiply(4, 3)  

def print_message(message):
    print(message)

print_message("This is a message.")  

def greet():
    print("Hello, world!")

def add(a, b):
    return a + b

greet()  

result = add(5, 3)
print(result) 
