# -*-coding:UTF-8-*-
import codecs
import datetime
import glob
import os

import chardet


def formed_files():
    current_date = datetime.datetime.now().strftime('.%Y-%m-%d')
    csvs = (glob.glob(r'../accs/*.csv'))
    txts = (glob.glob(r'../accs/*.txt'))
    news = (glob.glob(r'../accs/*.new'))
    for csv in csvs:
        os.rename(csv, csv[0:-4] + '.txt')
    for txt in txts:
        all_2_utf8(txt, out_enc="UTF-8")
        os.rename(txt, txt[0:-4] + current_date + '.new')
    return news


def all_2_utf8(filename, out_enc="UTF-8"):
    try:
        content = open(filename, 'rb').read()
        source_encoding = chardet.detect(content)
        print(filename)
        print("编码格式: " + source_encoding['encoding'])

        if source_encoding['encoding'] != "utf-8":
            if source_encoding['encoding'] == 'GB2312':
                content = content.decode("GBK", 'ignore')
                content = content.encode(out_enc)
                codecs.open(filename, 'wb').write(content)
            else:
                content = content.decode(source_encoding['encoding'], 'ignore').encode(out_enc)
                codecs.open(filename, 'wb').write(content)
            print("转换完成")
            print("编码格式: " + source_encoding['encoding'])
            print("*************************")
        else:
            print("无需转换")
            print("*************************")

    except IOError as err:
        print("I/O error:{0}".format(err))

