import os 
import time
dollar = """
||====================================================================||
   ||//$\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\//$\\||
   ||(100)==================| FEDERAL RESERVE NOTE |================(100)||
   ||\\$//        ~         '------========--------'                \\$//||
   ||<< /        /$\              // ____ \\                         \ >>||
   ||>>|  12    //L\\            // ///..) \\         L38036133B   12 |<<||
   ||<<|        \\ //           || <||  >\  ||                        |>>||
   ||>>|         \$/            ||  $$ --/  ||        One Hundred     |<<||
||====================================================================||>||
||//$\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\//$\\||<||
||(100)==================| FEDERAL RESERVE NOTE |================(100)||>||
||\\$//        ~         '------========--------'                \\$//||\||
||<< /        /$\              // ____ \\                         \ >>||)||
||>>|  12    //L\\            // ///..) \\         L38036133B   12 |<<||/||
||<<|        \\ //           || <||  >\  ||                        |>>||=||
||>>|         \$/            ||  $$ --/  ||        One Hundred     |<<||
||<<|      L38036133B        *\\  |\_/  //* series                 |>>||
||>>|  12                     *\\/___\_//*   1989                  |<<||
||<<\      Treasurer     ______/Franklin\________     Secretary 12 />>||
||//$\                 ~|UNITED STATES OF AMERICA|~               /$\\||
||(100)===================  ONE HUNDRED DOLLARS =================(100)||
||\\$//\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\$//||
||====================================================================||

"""
exchange_rates = {
    "":dollar,
    "USD": 1.0,
    "EUR": 0.85,
    "EGP": 30.9,
    "RMB": 6.5,
}


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_rates():
    print("Welcome to Currency 'Converter':\n")
    for currency in exchange_rates:
        print (f"{currency}: {exchange_rates[currency]}")
         
def currency_converter():
    clear_screen()
    display_rates()

    from_currency = input("\nChoose a currency to convert from: ").upper()
    while True:
        amount = float(input("Enter the amount: "))

        confirmation = input(
            f"\nYou entered {amount} {from_currency}. Confirm? (Y/N): ").upper()
        
        if confirmation == 'Y':
            break
    clear_screen()
    display_rates()

    to_currency = input("\nChoose a currency to convert to: ").upper()

    print ("Analyzing your request... Please wait.")
    time.sleep(2)
    print (
        f"Checking from{to_currency}'s best rates available .....Please wait")
    time.sleep(3)
    print (f"Getting a discount price for {from_currency}.....Please wait")
    time.sleep(2)

    
    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        print("Invalid currency. Conversion canceled")
        time.sleep(2)
        currency_converter()

    new_rate = exchange_rates[to_currency] /exchange_rates[from_currency]

    converted_amount = amount * new_rate

    clear_screen()
    print(
        f"Preparing the deal from {from_currency} to {to_currency}....Please wait\n")
    time.sleep(2)
    print (
        f"Exchang Rate: 1 {from_currency} = {to_currency}\n \n")
    time.sleep(2)
    print (f"{amount} {from_currency} is equal to {round(converted_amount, 2)}{to_currency}")
    time.sleep(1)

    accept_transaction = input(
        f"\nDo you accept this transaction? (Y/N): ").upper()
    
    if accept_transaction == 'Y':
        print ("Transaction Successful!")
    else:
        print("Transaction Canceled.")

    another_conversion = input(
        "\nDo you want to perform another conversion? (Y/N): ")
    
    if another_conversion == 'Y':
        currency_converter()
    else:
        print ("Thanks for using currency converter!")

currency_converter()
