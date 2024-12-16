file = open('text.txt', 'r')  
# Read the entire file
content = file.read()

print(content)
file = open('example.txt', 'w')  # Opens the file in write mode
file.write("Hello, World!\n") 
file.writelines(["Line 1\n", "Line 2\n"])  
file.close()

file = open('example.txt', 'r')  # Open the file in read mode
print("Content of the file after writing:")
content1 = file.read() 
print(content1)
file.close()