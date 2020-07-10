try:
    with open('/Users/macbook/Downloads/PythonCourse-master/Section_06/project_files/file_01.1.txt', mode='r') as my_file:
        print(my_file.read())

except FileNotFoundError:
    print('error file does not exist')

except:
    print('general error')

finally:
    print('run the finally statement at the end no matter what')
