import re
import sys


def main():
    """Convert time."""
    print(convert(input("Hours: ").strip()))


def convert(s):
    """Convert a time string in 12H format into a 24H format."""
    try:
        if re.search('.*?(?= AM)', s):
            x = re.search('.*?(?= AM)', s)
            if re.match(':',x.group(0)):
                pass
            else:
                pass
        elif re.search('.*?(?= PM)', s):
            x = re.search('.*?(?= PM)', s)
            if re.match(':',x.group(0)):
                pass
            else:
                pass
        else:
            raise ValueError
    
    except ValueError:
        pass

if __name__ == "__main__":
    main()