def main():
    pounds = pounds_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to charge? "))
    charge = pounds * percent
    print(f"Charge £{charge:.2f}")


def pounds_to_float(d):
    z = d.replace ("£", " ")
    x = float(z)
    return(x)

def percent_to_float(p):
    c = p.replace ("%", " ")
    n = float(c)/100
    return(n)

main()
