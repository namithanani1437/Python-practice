# -------------------------------
# Program 1: Print digits of a word/number
# -------------------------------

word = input()
res = ""
for seq in word:
    res = res + seq + " "
print(res)


# -------------------------------
# Program 2: Sum of digits
# -------------------------------

a = input()
b = len(a)
sum = 0
for digi in a:
    sum = sum + int(digi)
print(sum)


# -------------------------------
# Program 3: Factorial
# -------------------------------

a = int(input())
mul = 1
for i in range(1, a + 1):
    mul = mul * i
print(mul)


# -------------------------------
# Program 4: Sum of Cubes
# -------------------------------

a = int(input())
sum = 0
for i in range(1, a + 1):
    cube = i ** 3
    sum = sum + cube
print(sum)


# -------------------------------
# Program 5: Sum and Average of 10 Inputs
# -------------------------------

sum = 0
for i in range(10):
    b = int(input())
    sum = sum + b
avg = sum / 10
print(sum)
print(avg)


# -------------------------------
# Program 6: Sum of Squares from M to N
# -------------------------------

a = int(input())
b = int(input())
sum = 0
for i in range(a, b + 1):
    squ = i ** 2
    sum = sum + squ
print(sum)


# -------------------------------
# Program 7: Print Even Numbers up to N
# -------------------------------

a = int(input())
for i in range(1, a + 1):
    if i % 2 == 0:
        print(i)


# -------------------------------
# Program 8: Print Odd Numbers from M to N
# -------------------------------

a = int(input())
b = int(input())
odd = ""
for i in range(a, b + 1):
    if i % 2 == 1:
       odd = odd + str(i) + " "
print(odd)


# -------------------------------
# Program 9: Sum of Odd Numbers up to N
# -------------------------------

a = int(input())
sum = 0
for i in range(a + 1):
    if i % 2 == 1:
        sum = sum + i
print(sum)


# -------------------------------
# Program 10: Sum of Even Numbers from M to N
# -------------------------------

a = int(input())
b = int(input())
sum = 0
for i in range(a, b + 1):
    if i % 2 == 0:
        sum = sum + i
print(sum)


# -------------------------------
# Program 11: Product of Odd Numbers from M to N
# -------------------------------

a = int(input())
b = int(input())
pro = 1
for i in range(a, b + 1):
    if i % 2 == 1:
        pro = pro * i
print(pro)


# -------------------------------
# Program 12: Sum of Odd Numbers from M to N
# -------------------------------

a = int(input())
b = int(input())
sum = 0
for i in range(a, b + 1):
    if i % 2 == 1:
        sum = sum + i
print(sum)
