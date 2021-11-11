def show_Prices():
    prcAp_ = 20
    prcOr_ = 25
    print(f"The price of an apple is {prcAp_} pesos.")
    print(f"The price of an orange is {prcOr_} pesos.")
    return prcAp_, prcOr_

def getting_qntts():
    ApplesQntty = int(input("How many apples will you buy? "))
    OrangesQntty = int(input("How many oranges will you buy?"))
    return ApplesQntty, OrangesQntty

def Ttl_prc(prcAp, prcOr, ApplesQntty, OrangesQtty):
    Apple_Tp = prcAp * ApplesQntty
    Oranges_Tp = prcOr * OrangesQtty
    Ttl_prc = Apple_Tp + Oranges_Tp
    return Ttl_prc

def display(solve):
    print(f"The total amount of your purchase is {solve} pesos")

# steps:
# 1. Show the price of an apple and an orange.
PrcA, PrcO = show_Prices()
# 2. Ask how many apples and oranges will they buy.
AmntA, AmntO = getting_qntts()
# 3. Solve for the total price.
solve = Ttl_prc(PrcA, PrcO, AmntA, AmntO)
# 4. Display the total price.
display(solve)