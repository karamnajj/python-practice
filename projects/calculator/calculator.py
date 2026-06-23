print("Calculator")

num = int(input("How many operands: "))
numbers=[]
numbers.append(int(input("Enter First Number: ")))

for i in range(num-1):
    numbers.append(int(input("Enter Next Number: ")))


# a = input("First Number: ")
operator = input("Operator: ")
# b = input("Second Number: ")

if operator == "+":
    total = 0
    for number in numbers:
        total += number
    print(total)

elif operator == "-":
    total = numbers[0]
    for number in numbers:
        total -= number
    print(total)

elif operator == "*":
    total = 1
    for number in numbers:
        total *= number
    print(total)

elif operator == "/":
    total = numbers[0]
    for number in numbers:
        total /= number
    print(total)
else:
    print("Invalid Operator")
