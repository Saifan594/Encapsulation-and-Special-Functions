class MyClass:
    __privateVar = 27
    
    def __privateMeth(self):
        print("I'm inside class MyClass")
    
    def hello(self):
        print(f"Private Variable value: {MyClass.__privateVar}")

foo = MyClass()

print(foo.__privateVar)
foo.hello()
foo.__privateMeth()