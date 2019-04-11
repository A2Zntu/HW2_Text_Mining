# -*- coding: utf-8 -*-
import jieba
import os
import pandas as pd
from collections import Counter





work_dir = os.getcwd()
read_data_dir = os.path.join(work_dir, 'read_data')

df = pd.read_csv(os.path.join(read_data_dir, 'text.csv'))
# read jeiba dictionary
jieba.set_dictionary(os.path.join(read_data_dir,'dict.txt.big'))


stopwords = []
with open(os.path.join(read_data_dir, 'stopwords.txt'), 'r', encoding='UTF-8') as file:
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

belly = []
for m in range(len(data)):
    lb = data[m]['cutted_dict']
    belly.append(list(lb.keys()))
    
bigbelly =[]
for k in range(len(belly)):
    for l in range(len(belly[k])):
        chunk = belly[k]
        bigbelly.append(chunk[l])
        
        
    

smallbelly = list(set(bigbelly))

# 開啟檔案
fp = open(os.path.join(os.getcwd(), 'smallbelly5.txt'), "a")
 
# 寫入 This is a testing! 到檔案
fp.write(str(smallbelly))
 
# 關閉檔案
fp.close()


# %% train_data generate
textpool = []
for m in range(len(data)):
    lb = data[m]['content']
    textpool.append(lb)

allstring=""
for x in range(len(textpool)):
    allstring = allstring + textpool[x]

seg_list = jieba.lcut(remove_punctuation(allstring))
print(seg_list)


    
    
tagtable = pd.DataFrame()
tagtable['character']=seg_list

tagtable_2 = pd.DataFrame()
tagtable_2['A']=[1,2,3]
tagtable_2['B']=[1,2,3]

mktvocab = []
with open(os.path.join(read_data_dir, 'mktword.txt'), 'r', encoding='UTF-8') as file:
    for each in file.readlines():
        mktvocab.append(each.strip())




for g in range(len(tagtable)):
    if tagtable.iloc[g, 0] in mktvocab:
        seperateword =list(tagtable.iloc[g,0])
        
        for i in range(len(seperateword)):
            if i==0:
                pocket = []
                pocket.append(seperateword[i])
                pocket.append("B-MKT")
                betadf = pd.DataFrame([pocket],columns=list('AB'))
                tagtable_2= tagtable_2.append(betadf)
            else:
                pocket = []
                pocket.append(seperateword[i])
                pocket.append("I-MKT")
                betadf = pd.DataFrame([pocket],columns=list('AB'))
                tagtable_2= tagtable_2.append(betadf)
    
    elif tagtable.iloc[g, 0]==" ":
        continue
    
    elif type(tagtable.iloc[g, 0])==int:
        continue
           
    else:
        seperateword =list(tagtable.iloc[g,0])
        for i in range(len(seperateword)):
            pocket =[]
            pocket.append(seperateword[i])
            pocket.append("O")
            betadf = pd.DataFrame([pocket],columns=list('AB'))
            tagtable_2= tagtable_2.append(betadf)


with open(os.path.join(os.getcwd(), 'train_data.csv'),'a') as f:
    f.write(tagtable_2.to_csv())
            
