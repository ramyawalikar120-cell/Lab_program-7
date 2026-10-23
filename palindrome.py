s = input("Enter a string: ")
t = s.lower().replace(" ", "")
if t == t[::-1]:
    print(s, "is a palindrome")
else:
    print(s, "is not a palindrome")