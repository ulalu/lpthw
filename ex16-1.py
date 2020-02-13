from sys import argv

script, filename = argv

print(f"We're going to read {filename}.")
print("If you don't want that, hit CTRL-C.")
print("To continue, hit return.")

input("?")

print("Opening the file...")
print('')
target = open(filename, 'r')

print(target.read())

print("Closing file")
target.close()