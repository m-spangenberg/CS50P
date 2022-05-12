def main():
    """Let's get on the case!"""
    case = input("camelCase: ").strip()
    print(f"snake_case: {snekCase(case)}")


def snekCase(input):
    """ "This function converts input to snake_case"""
    snek = ""
    for letter in input:
        if letter.isupper():
            snek += "_"
            snek += letter.lower()
        else:
            snek += letter

    return snek


main()
