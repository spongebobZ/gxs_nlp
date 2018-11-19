import jieba,os

def cut_w(fp):
    fn = os.path.basename(fp)
    tmp_list=[]
    with open(fp,'r',encoding='utf-8') as fr:
        for line in fr.readlines():
            tmp_list.append(' '.join(jieba.cut(line)))
    with open('./src_cut/'+fn,'w',encoding='utf-8') as fw:
        for i in tmp_list:
            fw.write(i)

cut_w('./src/1引言.txt')