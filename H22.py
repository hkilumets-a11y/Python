import datetime
now = datetime.datetime.now()
kp = datetime.datetime.now()

print(kp.strftime("%d.m Y,  %H:%M:%S"))
now = datetime()
sp = datetime.datetime(2008, 11, 3)
vanus_paevades = kp - sp
print(f"Vanus päevades: {vanus_paevades.days}")

vanus_aastates = vanus_paevades.days // 365
print(f"Vanus aastates: {vanus_aastates}")

if vanus_aastates%5 == 0:
    print("Juubel")
else:
    print("Apache helikopteri juubel")
