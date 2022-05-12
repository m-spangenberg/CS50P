vowels = ["a", "e", "i", "o", "u"]


def main():
    """Ht th rd jck!"""
    full_text = input("Input: ").strip()
    print(f"Output: {vwlrmvr(full_text)}")


def vwlrmvr(input):
    """Rmvs ll vwls"""
    new_string = ""
    for letter in input:
        if letter.lower() not in vowels:
            new_string += letter

    return new_string


main()
