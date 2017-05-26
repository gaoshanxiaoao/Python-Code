import urllib.request
import re
import string
import operator
import os


def cleanText(input):
    # input = re.sub('\n+', " ", input).lower()  # 匹配换行,用空格替换换行符
    input = re.sub('\[[0-9]*\]', "", input)  # 剔除类似[1]这样的引用标记
    input = re.sub(' +', " ", input)  # 把连续多个空格替换成一个空格
    # input = re.sub("\"", "\"\"", input)
    input = bytes(input, 'utf-8')  # .encode('utf-8')  # 把内容转换成utf-8格式以消除转义字符
    input = input.decode("ascii", "ignore")
    #input = input.decode("gbk", "ignore")
    return input


def cleanInput(input):
    input = cleanText(input)
    cleanInput = []
    input = input.split(' ')  # 以空格为分隔符，返回列表

    for item in input:
        item = item.strip(string.punctuation)  # string.punctuation获取所有标点符号

        if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):  # 找出单词，包括i,a等单个单词
            cleanInput.append(item)
    return cleanInput


def getNgrams(input, n):
    input = cleanInput(input)
    # print(input)
    output = {}  # 构造字典
    for i in range(len(input) - n + 1):
        ngramTemp = " ".join(input[i:i + n])  # .encode('utf-8')
        if ngramTemp not in output:  # 词频统计
            output[ngramTemp] = 0  # 典型的字典操作
        output[ngramTemp] += 1
    return output


def getCharacterNgrams(input, n):
    input = cleanText(input)
    output = {}
    for i in range(len(input) - n + 1):
        ngramTemp = input[i:i + n]
        ngramTemp = re.sub("\"", "\"\"", ngramTemp)
        if ngramTemp not in output:
            output[ngramTemp] = 0
        output[ngramTemp] += 1
    return output


def checkNgrams(authorset, output):
    for doc in authorset:
        content = open(dirpath + document, encoding="utf8").read()
        output_ngrams = getCharacterNgrams(content, 3)
        for key, value in output.items():
            if key not in output_ngrams:
                del output[key]
            else:
                value = value + output_ngrams[key]
        return ouput


def articlelist_Author(authorname, dirlist):
    articleset = []
    for templist in dirlist:
        if templist.split("_")[0] == authorname:
            articleset.append(templist)
    return articleset


def output_ngrams_csv(dirlist, dirpath, file_csv):
    for document in dirlist:
        if(document.split(".")[1] == "csv"):
            continue
        content = open(dirpath + document, encoding="utf8").read()
        for i in range(3, 6):
            ngrams = getCharacterNgrams(content, i)
            author_name = document.split("_")[0]
            with open(file_csv, "a") as f:
                for key, value in ngrams.items():
                    f.write("\"" + key + "\"" + "," + document.split(".")[0] + "," +
                            author_name + "," + str(value) + "\n")
            f.close()


def create_Corpus_csv(dirlist, dirpath, file_csv):
    with open(file_csv, "a") as f:
        f.write("content|file_name|author_name" + "\n")
    f.close()
    for document in dirlist:
        if(document.split(".")[1] == "csv"):
            continue
        content = open(dirpath + document, encoding="utf8").read()
        content = cleanText(content)
    # for i in range(3, 6):
    # ngrams = getCharacterNgrams(content, i)
        author_name = document.split("_")[0]
        with open(file_csv, "a") as f:
            f.write(content + "|" + document.split(".")
                    [0] + "|" + author_name + "\n")
        f.close()


def literater_article_author(author_list, dirpath):
    for temp in author_list:
        if(temp == author_list[0]):
            content = open(dirpath + temp, encoding="utf8").read()
            output_ngrams = getCharacterNgrams(content, 3)
        else:
            checkNgrams(author_list[1:len(author_list)], output_ngrams)


def generate_square_matrix(file_1_csv, output):
    with open(file_1_csv, "r") as f:
        file_1_list = f.readlines()
    for ngram_content in file_1_list:
        if (ngram_content == "ngram|author"):
            continue
        else:
            ngramTemp = ngram_content.split("|")[0]
            if(ngramTemp not in output):
                output[ngramTemp] == 0
            output[ngramTemp] += 1
    return output


def create_Corpus_csv_2(dirlist, dirpath, file_csv):
    with open(file_csv, "a") as f:
        f.write("content|author_name|file_name" + "\n")
        for document in dirlist:
            with open(dirpath + document, "r", encoding="utf8") as fr:
                while True:
                    contentTemp = fr.readline()
                    if (contentTemp == "ngram|author\n"):
                        continue
                    elif not contentTemp:
                        break
                    else:
                        contentTemp = re.sub("\n", "", contentTemp)
                        f.write(contentTemp + "|" + document.split("_")
                                [0] + document.split("_")[1] + "\n")

                #content = open(dirpath + document, encoding="utf8").read()
                # f.write(content)

                # main program
                #------------------
file_csv = "G:/R_workplace/project_author_classification/Filtered_texts/finall_text.csv"
dirpath = "G:/R_workplace/project_author_classification/Filtered_texts/"
dirlist = os.listdir(dirpath)
# output_ngrams_csv(dirlist, dirpath, file_csv)
create_Corpus_csv_2(dirlist, dirpath, file_csv)
#--------------------


'''
Austen_list = articlelist_Author("Austen", dirlist)
Chaucer_list = articlelist_Author("Chaucer", dirlist)
Dickens_list = articlelist_Author("Dickens", dirlist)
Paterson_list = articlelist_Author("Paterson", dirlist)
Shelley_list = articlelist_Author("Shelley", dirlist)
'''


# file_name = "Paterson_TheOldBushSongs"

# 方法一：对网页直接进行读取
'''
content = urllib2.urlopen(urllib2.Request(
    "http://pythonscraping.com/files/inaugurationSpeech.txt")).read()
'''

'''
# 方法二：对本地文件的读取，测试时候用，因为无需联网
content = open(
    "G:/R_workplace/project_author_classification/Corpus_1/" + file_name + ".txt").read()
ngrams = getNgrams(content, 5)
'''
'''
sortedNGrams = sorted(ngrams.items(), key=operator.itemgetter(
    1), reverse=True)  # =True 降序排列
'''
# print(ngrams)

'''
author_name = file_name.split("_")[0]
print(author_name)
file_csv = "G:/R_workplace/project_author_classification/Corpus_1/corpus_ngram.csv"
'''
'''
with open(file_csv, "a") as f:
    for key, value in ngrams.items():
        f.write(key + "," + file_name + "," +
                author_name + "," + str(value) + "\n")
f.close()
'''
