# Compound interest calculator

def compound_interest(principal, rate, time):
    amount = principal * (1 + rate / 100) ** time
    return round(amount, 2)

if __name__ == "__main__":
    p = float(input("Enter initial amount: "))
    r = float(input("Enter interest rate (%): "))
    t = int(input("Enter number of periods: "))
    print(f"Final amount after {t} periods: {compound_interest(p, r, t)}")
