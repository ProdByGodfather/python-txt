'''
    Prod By GodFather.
    CRUD The TXT Files With Python.
    This File Training You About Read & Create & Write & Delete, TXT Files With Python.
'''

# import libraries
import time
import os

# for create the TXT file

# File path ( now in base directory ) with file.txt name
path = 'file.txt'

''' 
    for connect to the files we use 2 arguments: 
    1: file path
    2: actions:
        2.1: `r` For Read The File
        2.2: `w` For Write The File
        2.3: `x` For Create New File
        2.4: `a` For Add Item To The File
        2.5: `r+` For Write And Read The File
'''
try:
    file = open(path, 'r+')
except:
    file = open(path, 'x')
    file = open(path, 'r+')

# Create A Text For Write on Text File
text = ""
for i in range(10):
    text += f"line {i}.\n"

# Write Text to Text file
file.write(text)

# Close `file` Connection, Basically this action is to update the information of the `.txt` file
file.close()
file = open(path,'r')

get_all_lines_as_list = file.readlines()
print("as List: ",get_all_lines_as_list)

# get all lines as list and displaying as str
print("as str ( sorted ): ",end="")
for i in get_all_lines_as_list:
    print(i,end='')



time.sleep(10)
for i in range(5,0,-1):
    os.system("cls")
    print(f"after {i} sec `file.txt` will by deleted ")
    time.sleep(1)

# close file before delete them
file.close()
# delete the file
os.remove('file.txt')
os.system("cls")
os.system('color 02')
print("file.txt deleted")