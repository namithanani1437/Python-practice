#sum of k powers#
a=input()
length=len(a)
sum=0
for i in a:
    i=int(i)**length
    sum=sum+(i)
print(sum)


#Armsrong number#
a=input()
length=len(a)
sum=0
for i in a:
    i=int(i)**length
    sum=sum+i
if int(a)==sum:
    print("Armstrong Number")
elif int(a)!=sum:
    print("Not an Armstrong Number")


#Factors of a number#
a=int(input())

for i in range(1,a+1):
    if a%i==0:
        print(i)
