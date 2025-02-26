x = input("Enter your name:")
print("Hello " + x)  #This is a comment

float_number = 203021.123
intNumber = 18
user_name = "Name"
UserDescription = """
lorem ipsum dolor sit amet, 
consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut 
labore et dolore magna aliqua.
"""

print(type(UserDescription, user_name))

print(len(user_name))

txt = user_name.upper()
print(txt)

print(UserDescription[0:18])

f_user_name = f"Your name is: {x}"
print(f_user_name)

format_user_name = "Your name is: {name}"
print(format_user_name.format(name = x))



