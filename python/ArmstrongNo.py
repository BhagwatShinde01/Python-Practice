n = int(input("Enter number: "))
temp = n
sum = 0

while temp > 0:
    digit = temp % 10
    sum += digit ** len(str(n))
    temp //= 10

if sum == n:
    print("Armstrong")
else:
    print("Not Armstrong")