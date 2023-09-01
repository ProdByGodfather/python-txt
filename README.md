# Python-txt
<hr>
Prod By GodFather.<br>
Read, Write, Delete and update the `.TXT` Files with python.

## Working

get file name with url to path variable:
```python
    path = 'file-name.txt'
```
for connect to the files we use 2 arguments: <br>
1. file path
2. actions:

    1. `r` For Read The File
    2. `w` For Write The File
    3. `x` For Create New File
    4. `a` For Add Item To The File
    5. `r+` For Write And Read The File

```python
file = open(path, 'r')
```

now for show the datas from `file-name.txt` :
```python

get_all_lines_as_list = file.readlines()
print("as List: ",get_all_lines_as_list)

# get all lines as list and displaying as str
print("as str ( sorted ): ",end="")
for i in get_all_lines_as_list:
    print(i,end='')

```

For write on `.txt` file we using write method:
```python

file.write(text)

```
