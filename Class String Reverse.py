print("\033c")

class StringReverse:
    def __init__(self):
        self.__string = ""
        self.__reversedString = ""
    
    def takeInput(self):
        self.__string = input("Enter a string: ")
    
    def reverseString(self):
        self.__reversedString = self.__string[::-1]
        
        return self.__reversedString

string = StringReverse()
string.takeInput()

reversedString = string.reverseString()
print(f"Reverse of the given string: {reversedString}")