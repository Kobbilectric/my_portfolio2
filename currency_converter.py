def usd_eur():
    return amount  *  0.92315

def eur_usd():
    return amount /  0.92315

def gbp_usd():
    return amount * 0.789076

def usd_gbp():
    return amount / 0.789076
    
def usd_ngn():
    return amount * 1607
    
def ngn_usd():
    return amount / 1607

def menu():
    print("Welcome to currency converter")
    print("Press 1 to convert USD TO EUR")
    print("Press 2 to convert EUR TO USD")
    print("Press 3 to convert USD TO GBP")
    print("Press 4 to convert GBP TO USD")
    print("Press 5 to convert USD TO NGN")
    print("Press 6 to convert NGN TO USD")
    
if __name__ == "__main__":
    menu()
    
choice = int(input('Enter choice: '))
if choice < 1 or choice > 6:
        print('incorrect choice, pls try again')  

else:        
    amount = float(input('Pls enter amount: ')) 

    
if choice == 1:
    print(f'USD{amount} is EUR{usd_eur()}')

elif choice == 2:
    print(f'EUR{amount} is USD{eur_usd()}')

elif choice == 3:
    print(f'GBP{amount} is USD{gbp_usd()}')

elif choice == 4:
    print(f'USD{amount} is GBP{usd_gbp()}')

elif choice == 5:
    print(f'USD{amount} is NGN{usd_ngn()}')

elif choice == 6:
    print(f'NGN{amount} is USD{ngn_usd()}')