# """Number from 1 to 10"""--->
for i in range(1,11):
    print(i,end=" ")
# """print even number from 1 to 100"""--->
for i in range(0,101,2):
    print(i,end=" ")
# """print odd number from 1 to 100"""---->
for i in range(1,101,2):
    print(i,end=" ")
'''print the table of n'''
num=int(input("Enter the number:"))
i=1
while(i<=10):
    product=num*i
    print(product,end=" ")
    i+=1
# """sum of the number"""----->
num=int(input("Enter the number:"))
sum=0
for i in range(1,num+1):
    sum+=i
print("sum = ",sum)
# """print your name 10 times"""------>
for i in range(1,11):
    print("Nitin Singh")
# """Factorial of a number"""------>
num=int(input("Enter the number:"))
i=1
fact=1
while(i<=num):
    fact*=i
    i+=1
print(fact,"%")
# """count digit of a number"""---------->
num=int(input("Enter an number:"))
count=0
while(num != 0):
    # num=num%10
    count+=1
    num=num//10
print("count =",count)
# """Reverse of a number"""------------>
num=int(input("Enter an number:"))
original=num
rev=0
while(num != 0):
    digit=num%10
    rev=rev*10+digit
    num=num//10
print("Reverse =",rev)
if(original==rev):
    print("polindrome number")
else:
    print("Not polindrome number")
# """Armstrong of a number"""----------->
num=int(input("Enter an number:"))
original=num
sum=0
while(num != 0):
    digit=num%10
    sum=sum+digit*digit*digit
    num=num//10
print("Armstrong = ",sum)
if(original==sum):
    print("Armstrong number")
else:
    print("Not Armstrong number")
# """Prime or not"""------------->
num=int(input("Enter an number:"))
flag=False
if(num<0):
    print("Not prime Number.")
for i in range(2,num-1,1):
    if(num%i==0):
        flag=True
        break;
if(num==1):
    print("number nither prime nor composite.")
elif(flag==False):
    print("Prime number")
else:
    print("composite number")
# """print the number from num to 1"""------->
num=int(input("Enter an number:"))
for i in range(num,1,-1):
    print(i,end=" ")
# """Display this series AP 2,5,8,11---upto n term"""-->
num=int(input("Enter an number:"))
for i in range(2,(3*num-1),3):
    print(i,end=" ")
# """Display this series GP 1,2,4,8,----upto n term"""--->
num=int(input("Enter an number:"))
a=1
for i in range(1,num):
    print(a)
    a*=2
# """Display this series 99 95 91 87 ----
# # upto all terms which are positive"""------>
num=99
while(num>0):
        print(num,end=" ")
        num=num-4
            
        

    
