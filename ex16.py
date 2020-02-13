from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C.")
print("To continue, hit return.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating file. RIP.")
target.truncate()

print("Time to write a new file.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("Writing input to new file")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("Closing file")
target.close()