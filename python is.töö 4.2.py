def mahlapakkide_arv(ounte_kogus):
    pakkide_arv = (ounte_kogus * 0.4) / 3
    return round(pakkide_arv)

def main():
    ounte_kogus = float(input("Sisestage õunte kogus kilogrammides: "))
    pakkide_arv = mahlapakkide_arv(ounte_kogus)
    print(f"Mahlapakkide arv: {pakkide_arv}")

if __name__ == "__main__":
    main()
