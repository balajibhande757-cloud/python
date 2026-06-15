print(ord('A'))  # Output: 65
print(chr(65))   # Output: 'A'
# strings are imuutable (not chamgable)
# name="maHesh"
# name[0]="l"   # we cannot do this with strings (immutable)
# a=len(name)
# print(a)
# print(name.upper(),name)
# print(name.lower())
# print(name.capitalize())


# text = "  hello world  "
# print(text.strip())  # Output: "hello world"
# print(text.lstrip()) # Output: "hello world  "
# print(text.rstrip()) # Output: "  hello world"

# text = "Python is fun"
# print(text.find("is"))   # Output: 7
# print(text.replace("fun", "awesome"))  # Output: "Python is awesome"

# text = "apple,banana,orange"
# l=text.split(",")
# print(l)
# new_text="-".join(l)
# print(new_text)


text = "Python123"
print(text.isalpha())  # Output: False
print(text.isdigit())  # Output: False
print(text.isalnum())  # Output: True
print(text.isspace())  # Output: False