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