Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
name = "Rayna Faulkner"
address = "42 Wallaby Way"=
phonenumber = "918-444-4444"
print("Hi there my name is,", name\n "My address is: ", address\n "and my phone number is", number\n)
SyntaxError: unexpected character after line continuation character
print("Hi there my name is,", name "My address is: ", address "and my phone number is", number)
SyntaxError: invalid syntax
print("Hi there my name is,", name, "My address is: ", address, "and my phone number is", number)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print("Hi there my name is,", name, "My address is: ", address, "and my phone number is", number)
NameError: name 'number' is not defined
print("Hi there my name is,", name, "My address is: ", address, "and my phone number is", phonenumber)
