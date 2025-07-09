# Python String Slicing Syntax
# string[start:stop:step]
# start: index to begin (inclusive). Defaults to 0 if omitted.
# stop: index to end (exclusive). Defaults to end of string if omitted.
# step: how many characters to skip. Defaults to 1.

text = "Hello, World!"


print(text[0:5:2])    # 'Hello'    (characters at indexes 0,1,2,3,4)
print(text[7:12])   # 'World'    (indexes 7 to 11)
print(text[7:])     # 'World!'   (from index 7 to end)
print(text[:5])     # 'Hello'    (from start to index 4)
print(text[::2])    # 'Hlo ol!'  (every 2nd character)
print(text[::-1])   # '!dlroW ,olleH' (reversed string)


filename = "document.pdf"
dot_index = filename.index(".")   # Finds position of '.' → 8
extension = filename[dot_index + 1:]  # Slices from 9 to end → 'pdf'
print(extension)  # Output: pdf