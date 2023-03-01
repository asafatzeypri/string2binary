message = input("Enter the message: ")
binary = " ".join(format(ord(c), "b") for c in message)
print(binary)

binary_text = input("Enter the binary message: ")

normal =  "".join(chr(int(c, 2)) for c in binary_text.split(" "))

print(normal)