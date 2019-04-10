# -*- coding: utf-8 -*-
import jieba
import os
import pandas as pd
from collections import Counter

jieba.set_dictionary('dict.txt.big')

df = pd.read_csv("C:\\Users\\Stella\\Documents\\GitHub\\HW2_Text_Mining\\text.csv")
stopwords = []
with open('C:\\Users\\Stella\\Documents\\GitHub\\HW2_Text_Mining\\stopwords.txt', 'r', encoding='UTF-8') as file:
    for each in file.readlines():
        stopwords.append(each.strip())
    stopwords.append(' ')


def remove_punctuation(content_string, user_pc=False):
    if(user_pc):
        punctuation = user_pc
    else:
        punctuation=list("!@#$%^&*()_+=-[]`~'\"|/\\abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ,.;{}\r\xa0\u3000、，。「」！？；：<>")
        
    for p in punctuation:
        content_string = content_string.replace(p, " ")
    return(content_string)
    
def lcut_to_dict(lcut):
    word_dict = dict(Counter(lcut))
#     word_dict.pop(' ')
    return(remove_stopwords_from_dict(word_dict, stopwords))

def remove_stopwords_from_dict(word_dict, stopwords):
    for w in stopwords:
        word_dict.pop(w, word_dict)
    return word_dict

data =[]
for j in range(len(df)):
    betadic = {}
    betadic['id'] = df.iloc[j,0]
    betadic['fund'] = df.iloc[j,1]
    betadic['content']= df.iloc[j,2]
    data.append(betadic)

for i in range(len(df)):
    current_content =data[i]['content']
    current_cutted = jieba.lcut(remove_punctuation(current_content))
    data[i]['cutted_dict'] = lcut_to_dict(current_cutted)
    print(data[i]['cutted_dict'])




