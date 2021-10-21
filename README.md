# cgo
快捷编译单文件c程序


```

import os

def getFile(p='.'):
    dirFiles = os.listdir(p)
    # print(dirFiles)
    fileList = []
    for i in dirFiles:
        if os.path.isfile(i):
            if i.split('.')[-1] == 'c' or i.split('.')[-1] == 'C':
                fileList.append(i)

    print("当前目录C文件：",fileList)
    print("\n")
    return fileList


def compile(file='test.c'):
    name = file.split('.')[0]
    if os.name == 'nt':
        try:
            os.system("gcc ./"+file+" -o "+name+".exe")
        except:
            print(file+"编译失败\n")
        print("运行结果：\n")
        os.system(name+".exe")
    else:
        try:
            os.system("gcc ./"+file+" -o "+name)
        except:
            print(file+"编译失败")

        print("运行结果：\n")
        os.system("./"+name)



if __name__ == '__main__':
    ls = getFile()
    for i in ls:
        compile(i)


```

