import sys

args = sys.argv

if len(args) == 1:
    print()
elif len(args) > 2:
    print(AssertionError("more than one argument is provided"))
elif not set(args[1]) - set("0123456789") == set():
    print(AssertionError("argument is not an integer"))
else:
    x = int(args[1])
    print("I'm Even." if x % 2 == 0 else "I'm Odd.")