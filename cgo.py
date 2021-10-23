#!/usr/bin/env python3

import os,json
def getFile(p='.'):
    gcc = []
    gjj = []
    files = {}    
    dirFiles = os.listdir(p)
    # print(dirFiles)
    for i in dirFiles:
        if os.path.isfile(i):
            if i.split('.')[-1] == 'c' or  i.split('.')[-1] == 'C':
                gcc.append(i)
            if i.split('.')[-1] == 'cpp' or i.split('.')[-1] == 'CPP':
                gjj.append(i)
              
    files['c'] = gcc
    files['cpp'] = gjj 
    # print("当前目录可编译文件：",json.dumps(files,sort_keys=True,indent=4))
    # print("\n")
    return files


def compile(file='test.c',type='gcc'):
    name = file.split('.')[0]+'_'+type
    if os.name == 'nt':
        try:
            os.system(type+" ./"+file+" -o "+name+".exe")
        except:
            print("\033[1;30m{}\033[5,30m".format(file)+"\033[1;30m没有安装gcc!\033\[0m")
        print('\033[5;47m{}\033[0m'.format(file)+" \033[1;33m运行结果：\033[0m\n")
        os.system(name+".exe")
    else:
        try:
            os.system(type+" ./"+file+" -o "+name)
        except:
            print("\033[1;30m{}\033[5,30m".format(file)+"\033[1;30m没有安装g++!\033\[0m")

        print('\033[5;35m{}\033[0m'.format(file)+" \033[1;33m运行结果：\033[0m\n")
        os.system("./"+name)
        print("\n")



if __name__ == '__main__':
    ls = getFile()
    if ls['c'] != []:
        print("\033[1;34m可编译c文件：\033[0m",'\033[1;37m{}\033[0m'.format(ls['c']))
        for c in ls['c']:
            compile(c)

    if ls['cpp'] != []:
        
        print("\033[1;34m可编译cpp文件：\033[0m",'\033[1;37m{}\033[0m'.format(ls['cpp']))
        for cpp in ls['cpp']:
            compile(cpp,type='g++')
