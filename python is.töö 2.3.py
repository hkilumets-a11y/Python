import random
täringute_arv = int(input("vajalike tärnigute arv:"))
print("täringute arv")

for _ in range(täringute_arv):
    täringu_arv = random.randint(1, 6)
    print(täringu_arv)