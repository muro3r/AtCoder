"""A - Weather Prediction
https://atcoder.jp/contests/abc141/tasks/

>>> main('Sunny')
Cloudy
>>> main('Rainy')
Sunny"""


def main(s):
    if s == "Sunny":
        print("Cloudy")
    if s == "Cloudy":
        print("Rainy")
    if s == "Rainy":
        print("Sunny")


if __name__ == "__main__":
    s = input()
    main(s)
