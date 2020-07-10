import os

print(os.getcwd())

# Change directory
os.chdir('/Users/macbook/Desktop')

# Get current working directory
print(os.getcwd())

print(os.listdir())

if 'myfolder-pythontest7.9.20' not in os.listdir():
    os.mkdir('myfolder-pythontest7.9.20')
    os.makedirs('myfolder-pythontest7.9.20/subfolder/datafolder')

# delete last directory
os.rmdir('myfolder-pythontest7.9.20/subfolder/datafolder')

# os.rename('stuff.txt', 'renamed.txt')
# walking directories is used to traverse directories

import os

# a is the directory path dirpath, b is direcoty names dirnames, c is files filenames
for dirpath, dirnames, filenames in os.walk('/Users/macbook/Desktop/myfolder-pythontest7.9.20'):
    # print(4,dirpath)
    # print(5,dirnames)
    # print(6,filenames)
    # print('---------')
    pass

# we get the environment variable below
print(os.environ.get('HOME'))
print(os.path.join(os.environ.get('HOME'), "myfile.txt"))
# base name
print(os.path.basename('/bin/tools/myfile.txt'))
# dirname only
print(os.path.dirname('/bin/tools/myfile.txt'))
# see if the path exists
print(os.path.exists('/bin/tools/myfile.txt'))
# split, exists, isfile, isdir, splitext

import sys

# to accept input on command line, $python application1.2.py dan #prints-dan
# print(sys.argv[1:])

argument_list = sys.argv[1:]

for arg in argument_list:
    print(arg)
