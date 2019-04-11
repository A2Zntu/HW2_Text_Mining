# HW2_Text_Mining


## pdfConverter

Install
--------------
 * Install Package:
    ```
    $ pip install pdfminer     
    $ pip install pdfminer3k     
    $ pip install pdfminer.six     
    ```
 * check the version:    
     `pdfminer.__version__ `
     
   if it is `'20181108'`, then we are on the same page. 
   
  * Do the following test:     
     cd to the work path     
    `$ python pdfConverter.py` 
    
  ![alt text](https://github.com/A2Zntu/HW2_Text_Mining/blob/master/picture/Pdf2txtSample.JPG "Logo Title Text 1")
   

## cutword.py
* 讀取文本：讀取各基金公開說明書之txt檔
* 文字清理：去除標點符號與意義不大的詞彙
* 繁體中文分詞 
* 統計詞頻：針對每個基金文本，統計詞頻，以利後續TDM與co-occurrence matrix之製作

## generate_train_data.py
* 製作NER所需使用的train_data：由於助教的NER model只能辨識人、地、組織等詞彙，所以我們希望可以新增自訂類別，標記出跟基金市場較相關的術語，我們稱此類別為MKT(Market)。該檔案可以讀進文本、拆分每一個字、並且標記每一個字，如股(B-MKT)、價(I-MKT)，最後產出NER所需的train_data。
