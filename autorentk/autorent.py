import csv


faili_nimi= 'autorentk/rentals.csv'
rentide_arv = 0
ideed =[]

with open(faili_nimi, mode='r', encoding='utf-8') as fail:
    csv_lugeja = csv.reader(fail)
    
    pais = next(csv_lugeja) 
    
    for rida in csv_lugeja:
        rentide_arv += 1
        
        if rida[7] not in ideed:
            ideed.append(rida[7])

print(f"Rentide arv: {rentide_arv}")