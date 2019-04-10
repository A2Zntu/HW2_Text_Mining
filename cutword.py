import jieba
import os

jieba.set_dictionary('dict.txt.big')

f = open("C:\\Users\\Stella\\Documents\\GitHub\\HW2_Text_Mining\\txtDir\\filtered\\test.txt", encoding="utf-8")
text = []
for line in f:
    text.append(line)
print(text)

seg_list = jieba.lcut(text[0])

print("|".join(seg_list))


