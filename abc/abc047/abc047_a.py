"""
>>> main(10, 30, 20)
Yes
>>> main(30, 30, 100)
No
>>> main(56, 25, 31)
Yes

"""


def main(a, b, c):
    if a + b == c:
        print("Yes")
        return
    elif a + c == b:
        print("Yes")
        return
    elif b + c == a:
        print("Yes")
        return
    else:
        print("No")
        return


if __name__ == "__main__":
    a, b, c = map(int, input().split())

    main(a, b, c)
