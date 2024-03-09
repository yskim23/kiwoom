def my_decorator(func):
    def wppr():
        print("something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wppr

@my_decorator
def say_hello():
    print("Hello!")

say_hello()