import sys
from io import StringIO
import unittest


def resolve():
    N, L = map(int, input().split(' '))

    S = []

    for x in range(0, N):
        S.append(input())

    S.sort()

    [print(S, end='') for S in S]


if __name__ == '__main__':
    resolve()


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_case_1(self):
        input = """3 3
dxx
axx
cxx"""
        output = """axxcxxdxx"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()