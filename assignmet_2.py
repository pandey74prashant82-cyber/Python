#Task 1
num=int(input("Enter a number: "))
if num%2==0:
    print(f"{num} is an even number")
else:
    print(f"{num} is an odd number")

#task 2
num2=range(1,51)
for i in num2:
    print(i)
print(f"The sum of the number from 1 to 50 is:{sum(num2)}")
