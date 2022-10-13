import random

x = random.randrange(0,30)
s_poskusov = 5

while s_poskusov > 0:
    poskus = input("Vnesi število: ")
    poskus = int(poskus)
    if x == poskus:
        print("Zmaga")
        break
    elif poskus < x:
        print("Vnesli ste premajhno število")
    else:
        print("Vnesli ste preveliko število")
    s_poskusov = s_poskusov - 1


