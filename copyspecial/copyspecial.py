#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them

def get_special_paths(dir):
  filenames = os.listdir(dir)
  special_names = [name for name in filenames if re.search(r'__\w+__', name)]
  return [os.path.basename(name) for name in special_names]

def copy_to(to_path, dirs):
  if not os.path.exists(to_path):
    os.mkdir(to_path)
  to_path = os.path.abspath(to_path)
  for dir in dirs:
    for special_path in get_special_paths(dir):
      shutil.copy(special_path, os.path.join(to_path, special_path))

def zip_to(paths, zip_path):
  path_list = [zip_path]
  for path in paths:
    path_list += get_special_paths(path)
  cmd = "zip -j " + " ".join(path_list)
  print cmd
  (status, output) = commands.getstatusoutput(cmd)

  if status != 0:
    print output
    sys.exit(status)

def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  if todir != '':
    copy_to(todir, args)
  elif tozip != '':
    zip_to(args, tozip)
  else:
    for dir in args:
      print "\n".join(get_special_paths(dir)) + "\n"

if __name__ == "__main__":
  main()
