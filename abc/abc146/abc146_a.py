"""
>>> main('SAT')
1
>>> main('SUN')
7
"""

week = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]


def main(s: str):
    print(7 - week.index(s))


if __name__ == "__main__":
    s = input()

    main(s)
