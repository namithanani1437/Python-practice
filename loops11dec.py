#Question: Multiplication Table
Write a program to print the multiplication table of the given number (N) up to ten multiples in the format "N x i = M".

Input: The first line of input will contain an integer.

Output: The output should be ten lines containing the multiples in the given format.

Example: If the given number is 3, your code should print the multiplication table like:

3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12
3 x 5 = 15
3 x 6 = 18
3 x 7 = 21
3 x 8 = 24
3 x 9 = 27
3 x 10 = 30

a=int(input())

for i in range(1,11):
    print(str(a)+" "+"x "+str(i)+" "+"= "+str(a*i))



#Vowels in a String , write a program to find the vowels in the given  
#Print the resultant string by joining all the vowels in the string  
#Given a string string S .  S  Note  The Vowels are a, e, i, o, and u.

a=input()
word=""
for i in a:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
       word=word+i
print(word)

#Question: Reverse the String
In this coding question, you need to write a program that takes a string as input and prints the reverse of the given string.

a=input()
word=""
for i in a:
    word=i+word
print(word)
