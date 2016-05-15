import sys
import os
import shutil
import splitdoc

def write_to_main():
    '''
    Take the main file from sections and combine back into a 
    single file. 
    ''' 
    shandle = open('combined_main.tex','w')
    try:
        mhandle = open('./sections/main.tex')
    except:
        'section files not found!'

    for line in mhandle:
        if ('\\input' in line) and (line[0]!='%'):
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
    '''
    copy the lines from ihandle to ohandle.
    '''
    for line in ihandle:
        ohandle.write(line)
    return ohandle
            
if __name__ == '__main__':
    write_to_main()
    splitdoc.copy_to_dest('../')
    
