Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print("Hello, Python!")
Hello, Python!
print("Emmie")
Emmie
print(Hello, Python!)
SyntaxError: invalid syntax
print"Emmie"
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
print(Emmie)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print(Emmie)
NameError: name 'Emmie' is not defined
print("Emmie")("Hello, Python!")
Emmie
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print("Emmie")("Hello, Python!")
TypeError: 'NoneType' object is not callable
