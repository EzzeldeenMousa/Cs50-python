def main():
    dollars = dollars_to_float(input("how much was the meal? "))
    percent = percent_to_float(input("what percentage would you like to tip? "))
    tip = dollars * (percent/100)
    print(f"leave ${tip:.2f}")


def dollars_to_float(d):
    d = d.strip("$")
    return float(d)


def percent_to_float(p):
    p = p.strip("%")
    return float(p)
main()
