# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 10:41:06 2016

@author: dzhang
"""

# Looks through a specified directory and saves all files in target directory 
# to a csv file

# v2 allows for input of specific file types

import os, time
import pandas as pd

# rep_string reformats entered string to accept file endings with and without '.'
def rep_string(string):
    for char in [' ', '.']:
        if char in string:
            string = string.replace(char, '')
    string = string.split(',')
    return string

def get_files(path):
    for dirpath, subdirList, fileList in os.walk(rootDir):
        for fname in fileList:
            if not filetypes_str:
                fullpath = os.path.join(dirpath, fname)
                file_created = time.ctime(os.path.getctime(fullpath))
                file_last_modified = time.ctime(os.path.getmtime(fullpath))
                ftype = ''.join(fname.split('.')[-1:])
                yield fname, fullpath, file_created, file_last_modified, ftype
            else:
                for i in filetypes_f:
                    if fname.endswith(i):
                        fullpath = os.path.join(dirpath, fname)
                        file_created = time.ctime(os.path.getctime(fullpath))
                        file_last_modified = time.ctime(os.path.getmtime(fullpath))
                        ftype = ''.join(fname.split('.')[-1:])
                        yield fname, fullpath, file_created, file_last_modified, ftype   

                        
rootDir = input('Enter root directory: ')
print('Enter file types to search for (if multiple, separate with comma)')
print('Example: txt, pdf, docx, mp3')
filetypes_str = input ('To search all file types, hit [Enter]:')
filetypes_f = rep_string(filetypes_str)

rootfolder = ''.join(rootDir.split('\\')[-1:])

data = []
    

columns = ['File_name', 'File_path', 'Created', 'Last_modified', 'Filetype']

data = get_files(rootDir)

df = pd.DataFrame(data, columns = columns)
df_summary = df.groupby(['Filetype']).size().reset_index(name='Count')

print ('Summary: \n')
print(df_summary)

df.to_csv('dir_map_%s.csv' % rootfolder)

input('Press Enter to exit:')

