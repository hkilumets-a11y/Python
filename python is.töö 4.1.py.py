
def banner(reklaamlause):
    return reklaamlause.upper()
    
def main():
    kordade_arv = int(input("mitu reklaamlauset kuvada?"))
    reklaam = input("sisestage reklaamlause")
    
    for _ in range(kordade_arv):
        print(banner(reklaam))

if __name__ == "__main__":
    main()