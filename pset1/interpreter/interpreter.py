def main():
    """Let's get math-a-magical!"""
    x, y, z = input("Expression: ").strip().split(" ")
    print(f"{calculation(int(x), str(y), int(z)):.1f}")


def calculation(x, y, z):
    """crunch numbers"""
    if y == "+":
        return x + z
    elif y == "-":
        return x - z
    elif y == "*":
        return x * z
    elif y == "/":
        return x / z


main()
