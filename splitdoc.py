import sys
import os


def load_file(fname):
    try:    
        ihandle = open(fname)
    except:
        print("File not found. Exiting...")
        return -1
    try:
        os.mkdir('sections')
    except:
        pass 

    return ihandle 

def get_num_lines(ihandle):
    count=0
    for line in ihandle:
        count+=1
    ihandle.seek(0)
    return count 

def loop_build(ihandle):
    settings = open('sections/settings.tex','w')
    packages = open('sections/packages.tex','w')
    commands = open('sections/commands.tex','w')
    section_list = [] 
    while True:
        line = ihandle.readline()
        if not line: break
        if '\usepackage{' in line:
            packages.write(line)
        elif r'\newcommand' in line:
            commands.write(line)
        elif '\section' in line:
            ihandle,section_list=write_section(ihandle,line,section_list) 
        else:
            pass
    build_main(section_list)

def write_section(ihandle,line,section_list):
    '''
    write a section.
    '''
    pos = 0 
    fname = line[line.find('{')+1:line.find('}')]  
    section_list.append(fname)
    ohandle = open('sections/'+fname+'.tex','w') 
    ohandle.write(line)
    while True:
        line = ihandle.readline()
        if not line: break
        prev,pos = pos,ihandle.tell()
        if ('\section' in line):
            ihandle.seek(prev)
            return (ihandle,section_list)
        elif '\end{document}' in line:
            ihandle.seek(prev)
            return (ihandle,section_list)
        else:
            ohandle.write(line)
    return (ihandle,section_list)

def build_main(section_list):
    main = open('sections/main.tex','w')
    main.write('\input{settings}\n')
    main.write('\input{packages}\n')
    main.write('\input{commands}\n')
    main.write('\\begin{document}\n')
    for section in section_list:
        main.write('\input{'+section+'}\n')
    main.write(r'\end{document}')
    main.close()

            
if __name__=='__main__':
    fname = 'test.tex'
    ihandle = load_file(fname)
    loop_build(ihandle)
    

