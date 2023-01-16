#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib.request
import subprocess

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def read_urls(filename):
    adress = re.match(r'(\S+)_(\S+)', str(filename))
    adr = adress.group(2)
    f = open(filename, 'rU')
    unsort_urls = re.findall(r'\S*/puzzle/\S*', f.read())
    f.close()
    sort_urls = []
    for u in unsort_urls:
        u = adr + u
        if u not in sort_urls:
            sort_urls.append(u)
    sort_urls = sorted(sort_urls)
    return sort_urls


def download_images(img_urls, dest_dir):

    count = 0
    try:
        for i in img_urls:
            urllib.request.urlretrieve('http://' + i, dest_dir + "/img" + str(count))
            count += 1
    except IOError:
        os.mkdir(dest_dir)
        for i in img_urls:
            urllib.request.urlretrieve('http://' + i, dest_dir + "/img" + str(count))
            count += 1

    subprocess.getoutput('echo > ' + dest_dir + '/index.html')
    htmlfile = open('./animal/index.html', 'w')
    htmlfile.write('<verbatim>\n<html>\n<body>\n')
    img_f = os.listdir(dest_dir)

    for f in img_f:
        if re.match(r'img', f):
            htmlfile.write('<img src=' + os.path.abspath(os.path.join(dest_dir, f)) +'>')
    htmlfile.write('\n</body>\n</html>')
    htmlfile.close()

def main():
    args = sys.argv[1:]

    if not args:
        print('usage: [--todir dir] logfile ')
        sys.exit(1)

    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    img_urls = read_urls(args[0])

    if todir:
        download_images(img_urls, todir)
    else:
        for i in img_urls:
            print(i)

if __name__ == '__main__':
    main()
