def kuu_nimi(kuu_number):
    kuud = [
        "jaanuar", "veebruar", "märts", "aprill", "mai", "juuni",
        "juuli", "august", "september", "oktoober", "november", "detsember"
    ]
    
    if 1 <= kuu_number <= 12:
        return kuud[kuu_number - 1]
    else:
        return "tundmatu kuu"

def kuupaev_sõnena(kuupaev):
    päev, kuu, aasta = kuupaev.split(".")
    kuu_num = int(kuu)
    kuu_sõne = kuu_nimi(kuu_num)
    return f"{int(päev)}. {kuu_sõne} {aasta}. a."

def kuupaev_programm():
    kuup = input("Sisesta kuupäev kujul DD.MM.YYYY: ")
    tulemus = kuupaev_sõnena(kuup)
    print(tulemus)

kuupaev_programm()
