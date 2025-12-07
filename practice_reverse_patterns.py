# -----------------------------------------
# 1) Print N Numbers in Reverse
# -----------------------------------------

print("\n=== Print N Numbers in Reverse ===")
n = int(input("Enter a number: "))
for i in range(n, 0, -1):
    print(i)


# -----------------------------------------
# 2) Print from M to N in Reverse
# -----------------------------------------

print("\n=== Print from M to N in Reverse ===")
m = int(input("Enter starting number (M): "))
n = int(input("Enter ending number (N): "))

for i in range(m, n - 1, -1):
    print(i)


# -----------------------------------------
# 3) Print Characters in Reverse
# -----------------------------------------

print("\n=== Print Characters in Reverse ===")
text = input("Enter a word: ")

for char in text[::-1]:
    print(char)


# -----------------------------------------
# 4) Print Odd Numbers from N to M in Reverse
# -----------------------------------------

print("\n=== Print Odd Numbers from N to M ===")
n = int(input("Enter lower limit: "))
m = int(input("Enter upper limit: "))

for i in range(m, n - 1, -1):
    if i % 2 != 0:
        print(i)


# -----------------------------------------
# 5) Inverted Right Angled Triangle
# -----------------------------------------

print("\n=== Inverted Right Angled Triangle ===")
size = int(input("Enter size: "))

for i in range(size, 0, -1):
    print("*" * i)


# -----------------------------------------
# 6) Inverted Right Angled Triangle - Version 2
# -----------------------------------------

print("\n=== Inverted Right Angled Triangle - 2 ===")
size = int(input("Enter size: "))

for i in range(size, 0, -1):
    for j in range(i):
        print("*", end="")
    print()
