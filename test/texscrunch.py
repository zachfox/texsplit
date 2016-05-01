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
                tex_list.append('./sections/'+item)
            else:
                pass    
    return tex_list

def write_to_main(tex_list):
    '''
    Take the main file from sections and combine back into a 
    single file. 
    ''' 
    shandle = open('main.tex','w')
    try:
        main_ind = tex_list.index() 
        mhandle = open('./sections/main.tex')
    except:
        'section files not found!'

    for line in mhandle:
        if '\\input' in line:
            start_index = line.find('{')+1
            end_index = line.find('}')
            fname = './sections/'+line[start_index:end_index] +'.tex'
            try: 
                ihandle = open(fname)
                
            except:
                print('Unable to load the input file {0}. \n Exiting.'.format(fname))
            print('....Writing file {0}....'.format(fname))
            load_and_write(ihandle,shandle)    
        else:
            shandle.write(line)
        
def load_and_write(ihandle,ohandle):
    for line in ihandle:
        ohandle.write(line)
    return ohandle
    
            
if __name__ == '__main__':
    tex_list = load_files()
    write_to_main(tex_list)
    
