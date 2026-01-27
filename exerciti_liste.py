import random

person = ['Ion', 'Maria','Jora', 'Mihai', 'Vasile']

length = len(person)

number = random.randint(0, length-1)

print(person[number])

print(random.choice(person))