import os
#os.system("date")
#os.mkdir("path")
#os.getcwd()

#path='Moving_File/backupFiles.py'
#isExist=os.path.exists(path)
#print(isExist)

# path='Moving_File/backupFiles.py'
# root_ext = os.path.splitext(path)
# print("root part ",root_ext[0])
# print("ext part ",root_ext[1],"\n")

# os.listdir()

import shutil
path='Moving_File'

print("before moving file")
print(os.listdir(path))

source = 'Moving_File/LICENSE'
destination = 'Moving_File/folder'

dest =shutil.move(source,destination)

print("after moving file")
print(os.listdir(path))
