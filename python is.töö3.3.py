fail = open("konto.txt", encoding="UTF-8")
rida=[]
for rida in fail:
    if float(rida)<0:
        print(float(rida))




fail.close()