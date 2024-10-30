# Printing Patterns

# Square Pattern
size = 5

for i in range(size):
    for j in range(size):
        print("*", end="")
    print()

print("Triangle Pattern")

# Triangle Pattern
for i in range(size):
    for j in range(i+1):
        print("*", end="")
    print()