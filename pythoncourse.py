print("Hello world")

x = 1
y = 2
count = 0
for number in range(1,10):
    if (number % 2) == 0:
        print(number)
        count += 1

print(f"we have {count} even numbers")      

numbers = [1,6,3,8,3,88]
max_num = numbers[0]
for number in numbers:
    if (number > max_num):
        max_num = number

print(max_num)

class Person:
    def __init__(self, name):
        self.name = name
    
    def talk(self):
        print(f"{self.name} is talking")

person1 = Person("Karam")
person1.talk()