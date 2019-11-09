from operator import itemgetter


def main(list_, list_sortByScore):
    list_sortByScore = sorted(list_, key=itemgetter(1), reverse=True)
    list_sortByCity = sorted(list_sortByScore, key=itemgetter(0))

    [print(x[2]) for x in list_sortByCity]


if __name__ == "__main__":
    input_ = input().split('\n')
    N = int(input_[0])
    list_ = list()

    for i in range(1, N + 1):
        city, score = input().split(' ')

        list_.append([city, int(score), i])
