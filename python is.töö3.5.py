from datetime import *

fail = open("nimekiri.txt", encoding="UTF-8")

nimed = 1
for rida in fail:
    if nimed == datetime.now().day:
        print(rida, end="")
    nimed=nimed + 1
    
    fail.close