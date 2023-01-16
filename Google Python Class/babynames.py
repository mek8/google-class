import sys
import re

def extract_names(filename):

    extract_year = re.search(r'\w+', filename)
    year = extract_year.group()[-4:]
    names_dict = {}

    baby_file = open(str(filename), 'r')
    baby_names = re.findall(r'(<tr align="right"><td>)(\d+)(</td><td>)(\w+)(</td><td>)(\w+)(</td>)', baby_file.read())
    for t in baby_names:
        names_dict[t[3]] = t[1]
        names_dict[t[5]] = t[1]
    baby_file.close()

    sorted_names = sorted(names_dict)
    sorted_dict = {}

    for n in sorted_names:
        sorted_dict[n] = names_dict[n]

    final = []
    final.append(year)
    for key in sorted_dict.keys():
        final.append(key + " " + sorted_dict[key])

    return final

def main():
    args = sys.argv[1:]

    if not args:
        print('usage: [--summaryfile] file [file ...]')
        sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
    summary = False
    if args[0] == '--summaryfile':
        summary = True
        del args[0]

    for filename in args:
        names = extract_names(filename)

    # Make text out of the whole list
        text = '\n'.join(names)

        if summary:
            outf = open(filename + '.summary.txt', 'w')
            outf.write(text + '\n')
            outf.close()
        else:
            print(text)


if __name__ == '__main__':
  main()