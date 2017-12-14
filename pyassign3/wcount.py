#!/usr/bin/env python3

"""wcount.py: count words from an Internet file.

__author__ = "Qiuyu Ren"
__pkuid__  = "1700010641"
__email__  = "1700010641@pku.edu.cn"
"""

import sys
from urllib.request import urlopen


def nonletter(s, c):
    """Output the first non-letter character in the string s[c:].
    If no such characher exists, output -1."""

    for t in range(c, len(s)):
        if not (ord(s[t]) in list(range(65, 91))+list(range(97, 123))):
            return t
    return -1


def wcount(lines, topn=10):
    """Count words from lines of text string, then sort by their counts
    in reverse order, output the topn (word count), each in one line.
    """

    dic = {}
    lines += ' '
    c0 = -1
    c = nonletter(lines, 0)
    while c >= 0:
        l1 = lines[c0+1:c].lower()
        c0 = c
        c = nonletter(lines, c+1)
        if l1 == '':
            continue
        if l1 in dic:
            dic[l1] += 1
        else:
            dic[l1] = 1
    for i in range(topn):
        if dic == {}:
            break
        m = 0
        for text in dic.keys():
            if dic[text] > m:
                p = text
                m = dic[p]
        print(p, '\t', m)
        del dic[p]
    pass


if __name__ == '__main__':

    if len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. ' +
              'If not given, will output top 10 words')
        sys.exit(1)

    try:
        topn = 10
        if len(sys.argv) == 3:
            topn = int(sys.argv[2])
    except ValueError:
        print('{} is not a valid topn int number'.format(sys.argv[2]))
        sys.exit(1)

    try:
        with urlopen(sys.argv[1]) as f:
            contents = f.read()
            lines = contents.decode()
            wcount(lines, topn)
    except Exception as err:
        print(err)
        sys.exit(1)
