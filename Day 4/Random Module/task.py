import random

#random_integer = random.randint(a: 1, b: 5)
#print(random_integer)
random_number_0_to_1 = random.random() * 10
print(random_number_0_to_1)

random_float = random.uniform(a:1,b:10)
print(random_float)

random_heads_or_tails = random.randint(a:0, b:1)
if random_heads_or_tails == 0:
    print("Heads")
else:
    print("Tails")

