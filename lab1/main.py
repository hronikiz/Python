
user_name = input("Enter your name:")
print("Hello " + user_name)  #This is a comment

float_number = 203021.123
age = 18
UserDescription = """
lorem ipsum dolor sit amet, 
consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut 
labore et dolore magna aliqua.
"""

print("Type of variable User_Description",type(UserDescription))
print("Type of variable user_name: ",type(user_name))
print("Type of variable age: ",type(age))
print("Type of variable float_number: ",type(float_number))

print("Length of stroke: ", len(user_name))

user_name_upper = user_name.upper()
print("Text in uppercase: ",user_name_upper)

substring = UserDescription[5 : 15]
print("Substring: ", substring)

message1 = f"Your name is: {user_name}"
print(message1)

message2 = "My name is {}. I am {} years old.".format(user_name, age)
print(message2)



txt = "More results from text..."
substr = txt[4:12]
print(substr)
print(substr.strip(""))

txt = "More results from text..."
print(txt.split("e"))

age = 36
txt = "My name is Mary, and I am {}"
print(txt.format(age))
