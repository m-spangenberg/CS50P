# meal schedule
schedule = [
    {"meal": "breakfast time", "start hour": 7, "end hour": 8},
    {"meal": "lunch time", "start hour": 12, "end hour": 13},
    {"meal": "dinner time", "start hour": 18, "end hour": 19},
]


def main():
    """Feeling peckish!"""
    time = input("What time is it? ")
    time = float(convert(time))

    for dict in schedule:
        if time >= float(dict["start hour"]) and time <= float(dict["end hour"]):
            print(dict["meal"])
        else:
            continue


def convert(time):
    """check the time and let the user know what meal time it is!"""
    h, m = time.strip().split(":")
    t = float(h) + (float(m) / 60)
    return f"{t:.2f}"


if __name__ == "__main__":
    main()
