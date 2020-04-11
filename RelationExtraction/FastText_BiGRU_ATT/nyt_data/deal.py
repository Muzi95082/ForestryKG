import fileinput
def del_firstline():
    for line in fileinput.input("vec.txt", inplace = 1):
        if not fileinput.isfirstline():
            print(line.replace("\n", ""))
#del_firstline()
def del_f():
    fin = open('vec.txt',encoding='UTF-8')
    a = fin.readlines()
    fout = open('vec1.txt', 'w',encoding='UTF-8')
    b = ''.join(a[1:])
    fout.write(b)
    fin.close()
    fout.close()
del_f()