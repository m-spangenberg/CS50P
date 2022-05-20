import os
import sys
from PIL import Image


def main():
    """Dress a puppet in a Harvard CS50 Shirt."""
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)
    elif not os.path.isfile(sys.argv[1]):
        print(f"Could not read {sys.argv[1]}")
        sys.exit(1)
    elif not sys.argv[1].lower().endswith(".jpg") or not sys.argv[1].lower().endswith(".jpeg") or not sys.argv[1].lower().endswith(".png"):
        print("Not a JPG file")
        sys.exit(1)
    else:
        # Do the thing!
        fit_check(sys.argv[1], sys.argv[2])


def fit_check():
    """"""
    pass


if __name__ == "__main__":
    main()
