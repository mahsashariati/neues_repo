import random

random_numbers = [random.randint(1, 100) for _ in range(10)]
total = sum(random_numbers)

print("Zufallszahlen:", random_numbers)
print("Summe:", total)