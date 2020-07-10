myfile = open('/Users/macbook/Downloads/PythonCourse-master/Section_06/project_files/file_01.txt')

content = myfile.read() # note file can be read one time only by default

myfile.seek(0) # to reset cursor to start of the file

data = myfile.read()
print(data)

myfile.seek(0)
content_list = myfile.readlines()
myfile.close() # do this to make it so you can write to file
print(content_list)

with open('/Users/macbook/Downloads/PythonCourse-master/Section_06/project_files/file_01.txt', mode='w+') as myfile:
    # new_content = myfile.read()
    myfile.write('\nAppend this sentence to the file4')
    myfile.read()


myfile_appended = open('/Users/macbook/Downloads/PythonCourse-master/Section_06/project_files/file_01.txt')
print(myfile_appended)


