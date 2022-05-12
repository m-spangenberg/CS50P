months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


def main():
    """Back to the future?"""
    while True:
        try:
            userinput = input("Date: ").strip()

            # if the userinput contains spaces, do this.
            if " " in userinput:
                month, day, year = userinput.split(" ")
                if month.title() in months:
                    day = int(day.strip(","))
                    month = int(months.index(month)) + 1
                    if month <= 12 and day <= 31:
                        print(f"{year}-{month:02}-{day:02}")
                        break

            # if the userinput does not contain spaces, do this.
            else:
                month, day, year = map(int, userinput.split("/"))
                if month <= 12 and day <= 31:
                    print(f"{year}-{month:02}-{day:02}")
                    break

        # Go back to the top of the loop
        except ValueError:
            continue

        # catch CTRL+D and CTRL+C then end the program
        except (EOFError, KeyboardInterrupt):
            print("", end="\n")
            quit()

        # Go back to the top of the loop
        else:
            continue


main()
