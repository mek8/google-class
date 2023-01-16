import sys
script, option, filename = sys.argv

def parse(filename):
    file = open(str(filename), 'r')
    s = file.read()
    split = s.split()
    file.close()
    word_dict = {}

    for w in split:
        if w.lower() not in word_dict:
            word_dict[w.lower()] = 1
        else:
            word_dict[w.lower()] += 1

    sort_dict = sorted(word_dict)
    return sort_dict, word_dict

def second_e(t):
    return t[-1]

def print_words(filename):
    sort_dict, word_dict = parse(filename)

    for k in sort_dict:
        print(k, word_dict[k])

def print_top(filename):
    sort_dict, word_dict = parse(filename)

    tup = word_dict.items()
    tup = sorted(tup, key=second_e, reverse=True)

    count = 0
    for i in tup:
        if count <= 20:
            print(i[0], i[1])
            count += 1

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
    if len(sys.argv) != 3:
        print('usage: ./wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print('unknown option: ' + option)
        sys.exit(1)

if __name__ == '__main__':
  main()