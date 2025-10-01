#defining a function
def greet():
    name=input("Enter your name: ")
    return "Namaste! " + name
print(greet())

#function with parameters
def greet_parameter(name):
    return "Namaste! " + name
print(greet_parameter(name=input("Enter your name and i will greet you: ")))

#Question: What is the value of spam
spam = print('Hello!')
print(spam)  #None

#function without return , returns None
def hello():
    print("Hello!")
result = hello()
print(result)
