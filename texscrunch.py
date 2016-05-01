import sys
import os
import shutil

def load_files():
    '''
    Load all of the files in the sections folder
    '''
    tex_list = []
    for root, dirs, files in os.walk('./sections/'): 
        for item in files:
            if ('.tex' in item): 
                tex_list.append(item)
            else:
                pass    
    print(fname)

if __name__ == '__main__':
    load_files()

