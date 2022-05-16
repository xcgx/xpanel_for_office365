# coding:utf-8
import codecs
import glob
import os

import chardet


def form_files():
    csvs = (glob.glob(r'../accs/*.csv'))
    for csv in csvs:
        print(csv)
        file_name = csv[0:-4]
        print(file_name)
        os.rename(csv, file_name + '.txt')
    txts = (glob.glob(r'../accs/*.txt'))
    for txt in txts:
        gbk_2_utf8(txt, out_enc="UTF-8")


def gbk_2_utf8(filename, out_enc="UTF-8"):
    try:
        content = open(filename, 'rb').read()
        source_encoding = chardet.detect(content)
        print(filename)
        print("编码格式: " + source_encoding['encoding'])

        if (source_encoding['encoding'] != "utf-8"):
            if (source_encoding['encoding'] == 'GB2312'):
                content = content.decode("GBK")
                content = content.encode(out_enc)
                codecs.open(filename, 'wb').write(content)
            else:
                content = content.decode(source_encoding['encoding']).encode(out_enc)
                codecs.open(filename, 'wb').write(content)
            print("转换完成")
            print("*************************")
        else:
            print("无需转换")
            print("*************************")

    except IOError as err:
        print("I/O error:{0}".format(err))


form_files()
