from collections import Counter


def areOccurrencesEqual( s: str):
    # Method1
    d = {}
    for ch in s:
        if ch in d:
            d[ch] = d[ch] + 1
        else:
            d[ch] = 1
    print(len(set(d.values()))==1)

    # Method2
    # d=Counter(s)
    # print(d.most_common()[0][1]==d.most_common()[-1][1])

areOccurrencesEqual('abccsas')