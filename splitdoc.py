import sys
import os
import shutil

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
    
    copy_to_dest()    
    return ihandle 

def copy_to_dest(source = './',dest='./sections/'):
    '''
    Copy any non-annoying files to the new directory, 
    Parameters are default for split. 
    '''
    for root, dirs, files in os.walk(source): 
        for item in files:
            if ('.pdf' in item) or ('.eps' in item) or ('makefile' in item) or ('.bib' in item):
                shutil.copy(source+item,dest)
            else:
                pass    

def loop_build(ihandle):
    '''
    Parse the latex file and write into individual 
    documents. 
    '''
    #settings = open('sections/settings.tex','w')
    packages = open('sections/packages.tex','w')
    commands = open('sections/commands.tex','w')
    bibliography = open('sections/bibliography.tex','w')
    title_block = open('title_block.tmp','w')
    section_list = [] 

    while True:
        line = ihandle.readline()
        if not line: break
        if '\usepackage{' in line:
            packages.write(line)
        elif '\documentclass' in line:
            doc_class = line
        elif r'\newcommand' in line:
            commands.write(line)
        elif '\section' in line:
            ihandle,section_list=write_section(ihandle,line,section_list) 
        elif r'\begin{thebibliography' in line:
            ihandle = write_beg_end(ihandle,line,bibliography)
        elif (r'\title' in line) or (r'\author' in line) or (r'\affiliation' in line) or (r'\thanks' in line): 
            title_block.write(line)
        elif (r'\begin{abstract}' in line):
            write_beg_end(ihandle,line,title_block)
        else:
            pass
    title_block.close()
    build_main(section_list,doc_class)

def write_section(ihandle,line,section_list):
    '''
    write a section.
    '''
    pos = 0 
    fname = line[line.find('{')+1:line.find('}')]  
    fname = fname.lower()
    fname = fname.replace(' ','_')
    
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
        elif r'\begin{thebibliography}' in line:
            ihandle.seek(prev)
            return (ihandle,section_list)
        else:
            ohandle.write(line)
    return (ihandle,section_list)

def write_beg_end(ihandle,line,ohandle):
    '''
    write a section.
    '''
    pos = 0
    ohandle.write(line)
    name = line[line.find('{')+1:line.find('}')]  
    name = name.replace(' ','_')
    while True:
        line = ihandle.readline()
        if not line: break
        prev,pos = pos,ihandle.tell()
        if '\end{'+name+'}' in line:
            ohandle.write(line)
            ihandle.seek(prev)
            return ihandle
        else:
            ohandle.write(line)
    print "No end statement found for %s " %name
    return -1 

def build_main(section_list,doc_class):
    '''
    write the main document to be compiled 
    '''
    title_block = open('title_block.tmp')
    main = open('sections/main.tex','w')
    main.write(doc_class+'\n')
    main.write('\input{packages}\n')
    main.write('\input{commands}\n')
    main.write('\\begin{document}\n')
    for line in title_block:
        main.write(line)
    main.write('\\maketitle \n')
    for section in section_list:
        main.write('\input{'+section+'}\n')
    main.write('\input{bibliography}\n')
    main.write(r'\end{document}')
    main.close()
    os.remove('title_block.tmp')

if __name__=='__main__':
    fname = 'test.tex'
    ihandle = load_file(fname)
    loop_build(ihandle)
    

