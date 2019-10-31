# take input from the user
num = input("Enter a number: ")
temp=num=int(num)
# initialize sum
sum = 0
# find the sum of the cube of each digit

while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
