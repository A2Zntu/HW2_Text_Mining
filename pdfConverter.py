# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 16:36:23 2019

@author: Evan
"""

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO, open
from pdfminer.pdfpage import PDFPage
import os


work_dir = os.getcwd()
pdf_dir = os.path.join(work_dir, 'pdfraw')
txt_dir = os.path.join(work_dir, 'txtDir')

def readPDF(fname, pages=None):
    '''Convert pdf to a list of string'''
    if not pages: 
        pagenums = set();
    else:         
        pagenums = set(pages);      
    manager = PDFResourceManager() 
    codec = 'utf-8'
    caching = True

    output = StringIO()
    converter = TextConverter(manager, output, codec=codec, laparams=LAParams())     

    interpreter = PDFPageInterpreter(manager, converter)   
    infile = open(fname, 'rb')

    for page in PDFPage.get_pages(infile, pagenums,caching=caching, check_extractable=True):
        interpreter.process_page(page)

    convertedPDF = output.getvalue().split('\n')
    while '' in convertedPDF:
        convertedPDF.remove('')
        
    infile.close(); converter.close(); output.close()
    return convertedPDF

def saveTxt(content, txtFile):
    '''Convert a list of string to Txt File'''
    with open(txtFile, "wb+") as f:
        for line in content:
            try:
                f.write(line.encode('big5'))
            except UnicodeEncodeError as e:
                pass
        f.close()
        
def printTxt(txtFile):
    f = open(txtFile,'r')
    print(f)
    f.close()
    
def TxtNamePrecise(name):
    newName = ''
    for word in name:
        if word != ' ':
            newName += word
    
    newName += '.txt'
    return newName




f = open("C:\\Users\\Stella\\Documents\\GitHub\\HW2_Text_Mining\\fund_list3.csv", encoding="utf-8" )
fundlist =[]
for line in f:
      fundlist.append(line.strip('\n'))
print(fundlist)
m =0
for i in fundlist:
    m = m+1
    print(i)
    content = readPDF(os.path.join(pdf_dir, i))     
    name = str(m) # The documnet Name
    pathContent = os.path.join(txt_dir, name)
    saveTxt(content, txtFile = pathContent)
    print(content)
        

