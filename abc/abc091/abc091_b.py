"""B - Two Colors Card Game
https://atcoder.jp/contests/abc091/tasks/abc091_b
N
s_1
s_2
:
s_N
M
t_1
t_2
:
t_M

>>> main(3, ["apple", "orange", "apple"], 1, ["grape"])
2
>>> main(3, ["apple", "orange", "apple"], 5, ["apple", "apple", "apple", "apple", "apple"])
1
>>> main(1, ["voldemort"], 10, ["voldemort", "voldemort", "voldemort", "voldemort", "voldemort", "voldemort", "voldemort", "voldemort", "voldemort", "voldemort"])
0
>>> main(6, ["red", "red", "blue", "yellow", "yellow", "red"], 5, ["red", "red", "yellow", "green", "blue"])
1
"""


def main(n, s: list, m, t: list):
    choices = set(s + t)

    ans = [0]

    for choice in choices:
        ans_t = 0
        for _s in s:
            if choice == _s:
                ans_t += 1
        for _t in t:
            if choice == _t:
                ans_t -= 1

        ans.append(ans_t)

    print(max(ans))


if __name__ == "__main__":
    n = int(input())
    s = [input() for _ in range(n)]
    m = int(input())
    t = [input() for _ in range(n)]

    main(n, s, m, t)
