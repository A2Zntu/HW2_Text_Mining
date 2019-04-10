# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 15:47:32 2019

@author: Stella
"""
from pdfConverter import *


content = readPDF(os.path.join(pdf_dir, '景順潛力基金-基金公開說明書.pdf'))     
name = TxtNamePrecise(content[0]) # The documnet Name
pathContent = os.path.join(txt_dir, name)
saveTxt(content, txtFile = pathContent)
print(content)