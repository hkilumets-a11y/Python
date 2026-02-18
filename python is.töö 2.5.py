import random
poialpoisid  = int(input("Mitu põialpoissi tahab õunu?"))

lumivalgekese_ounad = 14

for i in range(poialpoisid):
    jagatud_ounad = random.choice([1, 2])
    lumivalgekese_ounad -= jagatud_ounad

    print(f"Päkapikk {i+1} sai {jagatud_ounad} õuna(õuna).")

print(f"Lumivalgekesele jäi alles {lumivalgekese_ounad} õuna.")
