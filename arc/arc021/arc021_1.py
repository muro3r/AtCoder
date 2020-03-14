"""A - DEAD END
https://atcoder.jp/contests/arc021/tasks/arc021_1

A_{1,1} A_{1,2} A_{1,3} A_{1,4}
A_{2,1} A_{2,2} A_{2,3} A_{2,4}
A_{3,1} A_{3,2} A_{3,3} A_{3,4}
A_{4,1} A_{4,2} A_{4,3} A_{4,4}

>>> main([[2, 8, 2, 2], [32, 2, 8, 8], [4, 64, 2, 128], [2, 8, 4, 2]])
CONTINUE
>>> main([[2, 4, 16, 4],[8, 32, 128, 8],[2, 64, 16, 2],[32, 4, 32, 4]])
GAMEOVER
>>> main([[2, 4, 2, 4],[4, 2, 4, 2],[2, 4, 2, 4],[4, 2, 4, 2]])
GAMEOVER

"""


def main(a: list):
    for i in range(3):
        for j in range(3):
            if a[i][j] == a[i][j + 1] or a[j][i] == a[j + 1][i]:
                print("CONTINUE")
                return

    print("GAMEOVER")


if __name__ == "__main__":
    a = [list(map(int, input().split())) for _ in range(4)]

    main(a)
