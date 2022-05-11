def main():
    """Hit the road, jack!"""
    while True:
        # Make sure the function obeys the rules set out by the pset.
        fraction = input("Fraction: ").strip()
        try:
            numerator, denominator = fraction.split("/", 1)
            if numerator.isdigit() and denominator.isdigit():
                if int(numerator) <= int(denominator) and int(denominator) != 0:
                    fuel_gauge = (int(numerator) / int(denominator)) * 100
                    if fuel_gauge >= 99:
                        print('F')
                        break
                    elif fuel_gauge < 99 and fuel_gauge > 1:
                        print(f"{fuel_gauge:.0f}%")
                        break
                    else:
                        print('E')
                        break
        # Here we catch those sneaky exceptions.
        except (ValueError, ZeroDivisionError):
            pass
        else:
            pass


def convert(fraction):
    """"""


def gauge(percentage):
    """"""


if __name__ == "__main__":
    main()