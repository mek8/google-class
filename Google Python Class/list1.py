print(__name__)
def match_ends(words):
    count = 0

    for word in words:
        if len(word) >= 2 and word[0] == word[len(word) - 1]:
            count += 1

    return(count)

#match_ends(['olala', 'hello', 'I', 'mom', 'dad'])


def front_x(words):

    xlist = []
    slist = []

    for w in words:
        if w[0] == 'x':
            xlist.append(w)
        else:
            slist.append(w)

    sxlist = sorted(xlist)
    slist = sorted(slist)

    final_list = sxlist + slist

    return(final_list)

#front_x(['bbb', 'ccc', 'axx', 'xzz', 'xxba'])

"""def sort_last_sample(tuples):

    last_list = []
    final_list = []

    for t in tuples:
        last_list.append(t[len(t)-1])
    last_list.sort()

    for i in last_list:
        for t in tuples:
            if i == t[len(t)-1]:
                final_list.append(t)

    return(final_list)"""

def last_el(t):

    return t[-1]

def sort_last(tuples):

    sort_l = sorted(tuples, key=last_el)

    return(sort_l)


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '

    print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))

def main():
    print('match_ends')
    test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
    test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
    test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

    #print
    print('front_x')
    test(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
       ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
    test(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
       ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
    test(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
       ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])


    #print
    print('sort_last')
    test(sort_last([(1, 3), (3, 2), (2, 1)]),
       [(2, 1), (3, 2), (1, 3)])
    test(sort_last([(2, 3), (1, 2), (3, 1)]),
       [(3, 1), (1, 2), (2, 3)])
    test(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]),
       [(2, 2), (1, 3), (3, 4, 5), (1, 7)])


if __name__ == '__main__':
  main()

