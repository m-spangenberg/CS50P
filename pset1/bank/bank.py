def main():
    """Be friendly to our customer"""
    greeting = input("Greeting: ").strip().lower()
    print(f"${penalty(greeting)}")


def penalty(greeting):
    """Check how much we owe the customer"""
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100


main()
