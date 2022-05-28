import re
import sys


def main():
    """Convert time."""
    print(convert(input("Hours: ").strip()))


def convert(s):
    """Convert a time string from 12H to 24H format.
    eg. 9:00 AM to 5:00 PM or 9 AM to 5 PM -> 09:00 to 17:00"""

    # Insensitively find all time strings using AM and PM

    

if __name__ == "__main__":
    main()