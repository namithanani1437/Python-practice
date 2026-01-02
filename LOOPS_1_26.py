# ============================================================
#                 Loops Practice — 2026-01-02
# ============================================================
# Language: Python
#
# Problems Covered Today:
#
# 1. Divisible by 9 in a Range
# 2. 2 Series
# 3. Sum of N Terms — 2 Series
# 4. Sum of N Terms — 1 Series
# 5. Sum of N Terms — X Series
# 6. Number of Digits from M to N
# 7. Divisible by 6
# 8. Vowels of a String — 2
# 9. Indivisible Number
# 10. Smallest Among N Numbers
#
# Practice Date: 2026-01-02
# ============================================================


print("------ 1. Divisible by 9 in a Range ------")
m = int(input("Enter start: "))
n = int(input("Enter end: "))
for i in range(m, n + 1):
    if i % 9 == 0:
        print(i)


print("------ 2. 2 Series ------")
terms = int(input("Enter number of terms: "))
for i in range(1, terms + 1):
    print("2" * i)


print("------ 3. Sum of N Terms — 2 Series ------")
n = int(input("Enter n: "))
total = 0
for i in range(1, n + 1):
    total += int("2" * i)
print("Sum =", total)


print("------ 4. Sum of N Terms — 1 Series ------")
n = int(input("Enter n: "))
total = 0
for i in range(1, n + 1):
    total += int("1" * i)
print("Sum =", total)


print("------ 5. Sum of N Terms — X Series ------")
x = input("Enter digit X: ")
n = int(input("Enter n: "))
total = 0
for i in range(1, n + 1):
    total += int(x * i)
print("Sum =", total)


print("------ 6. Number of Digits from M to N ------")
m = int(input("Enter start: "))
n = int(input("Enter end: "))
count = 0
for i in range(m, n + 1):
    count += len(str(i))
print("Total digits =", count)


print("------ 7. Divisible by 6 ------")
num = int(input("Enter a number: "))
if num % 6 == 0:
    print("Divisible by 6")
else:
    print("Not divisible by 6")


print("------ 8. Vowels of a String — 2 ------")
s = input("Enter a string: ")
vowels = "aeiouAEIOU"
for ch in s:
    if ch in vowels:
        print(ch)


print("------ 9. Indivisible Number (Prime Check) ------")
num = int(input("Enter a number: "))
if num <= 1:
    print("Not prime")
else:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print("Prime / Indivisible")
    else:
        print("Not prime")


print("------ 10. Smallest Among N Numbers ------")
n = int(input("Enter count: "))
smallest = None
for i in range(n):
    x = int(input())
    if smallest is None or x < smallest:
        smallest = x
print("Smallest number is:", smallest)

# ============================================================
# End of Loops Practice — 2026-01-02
# ============================================================

