import  re

file_object = open('staticResult.txt','r',encoding='UTF-8')
file_object1 = open('staticResult1.txt','w',encoding='UTF-8')
for line in file_object:
    lines=re.sub('()', '', line)
    file_object1.write(lines)
file_object1.close()
file_object.close()