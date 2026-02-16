tulemus = float(input("Sisesta oma eksamitulemus protsentides: "))
if tulemus >= 90:
    hinne = 5
elif tulemus >= 75:
    hinne = 4
elif tulemus >= 50:
    hinne = 3
else:
    hinne = 2
print(f"Sinu hinne on: {hinne}")