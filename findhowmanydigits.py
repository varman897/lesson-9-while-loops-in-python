num = int(input("Enter a number to find how many digits are in it: "))

temp = abs(num)
count = 0

if temp == 0:
    count = 1
else:
    while temp > 0:
        temp = temp // 10
        count += 1

print("You have", count, "digits")