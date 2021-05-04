import csv
import os
import os.path

directories = os.listdir('.')
print(directories)

for file_name in directories:
    if file_name[0] == '.' or file_name[0] == '_' or file_name == 'README.md':
        pass
    else:
        for i, character in enumerate(file_name):
            if character == '.':
                file_name_jpg = file_name[:i] + '.jpg'
                print(file_name_jpg)
                # Line below changes all python files to jpg
                # os.rename(file_name, file_name_jpg)
print(directories)
