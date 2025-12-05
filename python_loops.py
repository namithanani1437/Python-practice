05-DEC-2025
#Print Numbers Divisible by B#

a=int(input())
b=int(input())

for i in range(1,a+1):
    if i%b==0:
        print(i)


#Sum of Numbers Divisible by A#

a=int(input())
b=int(input())
c=int(input())
sum=0
for i in range(b,c+1):
    if i%a==0:
        sum=sum+i 
print(sum)

#Count of numbers divisible by A#

a=int(input())
b=int(input())
count=0
for i in range(1,a+1):
    if i%b==0:
        count=count+1
print(count)

#Print numbers divisible by 2 and 3#

a=int(input())
for i in range(1,a+1):
    if i%2==0 and i%3==0:
         print(i)


#Print count of numbers divisible by 2 and 3#

a=int(input())
count=0
for i in range(1,a+1):
     if i%2==0 and i%3==0:
         count=count+1
print(count) 

#Print required characters#

a=input()

for i in a:
     if i=="z" or i==a:
       print(i) 

#print vowels#

a=input()
for i in a:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
        print(i) 


#count of vowels#
a=input() 
count=0
for i in a:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
        count=count+1
print(count) 




