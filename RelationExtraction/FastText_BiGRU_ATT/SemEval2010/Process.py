import codecs
with codecs.open('train.txt','r','utf-8')as fr,codecs.open('train_f1.txt','a','utf-8')as f:

    for line in fr:
        pre=',,'
        line= line.replace(pre,",")
        line = line.replace("<e1>","")
        line = line.replace("</e1>","")
        line = line.replace("<e2>","")
        line = line.replace("</e2>","")
        f.write(line)

    f.close()