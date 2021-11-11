def get_init_infos():
    amntOFmoney = int(input("Please enter your current money balance: "))
    prcOFapple = int(input("Please enter the price of an apple: "))
    return amntOFmoney, prcOFapple

def showing_Results(amnt_money, Apples_price):
    MaxOFapples = amnt_money // Apples_price
    _Change = amnt_money % Apples_price
    return MaxOFapples, _Change

def Display(MaxOFapples, _Change):
    print(f"You can buy {MaxOFapples} apples and your change is {_Change} pesos")

amnt_money, Apples_price = get_init_infos()

MaxOFapples, _Change = showing_Results(amnt_money, Apples_price)

Display(MaxOFapples, _Change)