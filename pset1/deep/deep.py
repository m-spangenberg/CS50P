answers = ["42", "forty two", "forty-two"]


def main():
    """Let's find the meaning of all of this... stuff."""
    question = str(input("What is the meaning of life?: ").strip().lower())
    thinking(question)


def thinking(question):
    """Compute!"""
    if question not in answers:
        print("No")
    else:
        print("Yes")


main()
