import tf_idf4gxs,cut_word

if __name__ == '__main__':
    base_dir = './src/'
    cut_dir = './src_cut/'
    file = '1引言.txt'
    cut_word.cut_w(base_dir+file)
    key_num = 4
    key_word, word_list = tf_idf4gxs.get_key_words(cut_dir + file, key_num)
    print('the %sth key word is:%s'%(key_num,','.join(key_word)))
    print('all word is:%s'%','.join(word_list))