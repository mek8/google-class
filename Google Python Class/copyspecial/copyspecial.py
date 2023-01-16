import sys
import re
import os
import shutil
import subprocess

def get_special_paths(dir):

    spec_paths = []
    filenames = os.listdir(dir)
    for f in filenames:
        match = re.search(r'__\w+__', f)
        if match:
            spec_paths.append(os.path.join(dir, f))
    return spec_paths

def copy_to(paths, todir):

    try:
        for p in paths:
            shutil.copy(p, todir)
    except IOError:
        os.mkdir(todir)
        for p in paths:
            shutil.copy(p, todir)

def zip_to(paths, zippath):

    for p in paths:
        cmd = "zip -j " + zippath + " " + p
        print("Command to run:", cmd)
        (status, output) = subprocess.getstatusoutput(cmd)
        if status:
            sys.stderr.write(output)
            sys.exit(status)
        print(output)


def main():
    args = sys.argv[1:]
    if not args:
        print("usage: [--todir dir][--tozip zipfile] dir [dir ...]")
        sys.exit(1)

    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]
        for a in args:
            files_for_copy = get_special_paths(a)
            copy_to(files_for_copy, todir)


    tozip = ''
    if args[0] == '--tozip':
        tozip = args[1]
        del args[0:2]
        for a in args:
            files_for_zip = get_special_paths(a)
            zip_to(files_for_zip, tozip)


    if len(args) == 0:
        print("error: must specify one or more dirs")
        sys.exit(1)

if __name__ == "__main__":
    main()

