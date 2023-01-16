import os
import sys
import subprocess

## Example pulls filenames from a dir, prints their relative and absolute paths
def printdir(dir):
  filenames = os.listdir(dir)
  for filename in filenames:
    print(filename)  ## foo.txt
    print(os.path.join(dir, filename)) ## dir/foo.txt (relative to current dir)
    print(os.path.abspath(os.path.join(dir, filename))) ## /home/nick/dir/foo.txt

## Given a dir path, run an external 'ls -l' on it --
## shows how to call an external program
def listdir(dir):
    cmd = 'ls ' + dir
    mkdir = 'mkdir testmkdir'
    print("Command to run:", mkdir)   ## good to debug cmd before actually running it
    (status, output) = subprocess.getstatusoutput(mkdir)
    if status:    ## Error case, print the command's output to stderr and exit
        sys.stderr.write(output)
        sys.exit(status)
    print(output)  ## Otherwise do something with the command's output

    (status, output) = subprocess.getstatusoutput(cmd)
    if status:    ## Error case, print the command's output to stderr and exit
        sys.stderr.write(output)
        sys.exit(status)
    print(output)  ## Otherwise do something with the command's output

listdir('/home/EmilMek8/googl')