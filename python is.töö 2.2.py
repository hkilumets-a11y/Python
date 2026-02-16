ringide_arv = int(input("Sisesta ringide arv:"))
porgandite_koguarv = 0
praegune_ring = 2
while praegune_ring <= ringide_arv:
    porgandite_koguarv += praegune_ring
    praegune_ring += 2

print(f"porgandite koguarv on: {porgandite_koguarv} ")