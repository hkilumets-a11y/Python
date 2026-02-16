õpilaste_arv = int(input("Sisesta õpilaste arv"))

tais_laudade_arv = õpilaste_arv // 2
opilased_ilma_partnerita = õpilaste_arv % 2

print(f"Täis laudade arv: {tais_laudade_arv}")
print(f"Õpilasi, kes jäävad ilma lauapartnerita: {opilased_ilma_partnerita}")