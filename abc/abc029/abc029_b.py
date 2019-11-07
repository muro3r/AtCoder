'''
>>> main(['january','february','march','april','may','june','july','august',\
    'september','october','november','december'])
8
>>> main(['rrrrrrrrrr',\
      'srrrrrrrrr',\
      'rsr',\
      'ssr',\
      'rrs',\
      'srsrrrrrr',\
      'rssrrrrrr',\
      'sss',\
      'rrr',\
      'srr',\
      'rsrrrrrrrr',\
      'ssrrrrrrrr']\
     )
11
'''


def main(s):
    ans = 0

    for _s in s:
        if 'r' in _s:
            ans += 1

    print(ans)


if __name__ == "__main__":
    s = [input() for _ in range(12)]

    main(s)
