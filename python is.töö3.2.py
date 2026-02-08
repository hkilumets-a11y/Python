ring = 6
carrots = 0
for i in range(ring):
    r= i+1
    if r % 2 == 0:
        carrots= r+carrots
    print(carrots)