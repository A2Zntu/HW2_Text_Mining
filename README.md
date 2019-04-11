# HW2_Text_Mining
Members
-------------- 

* R07723037 陳韻竹 財金所碩一
* B05902027 尹慕哲 資工系大三
* R06723051 姜奕帆 財金所碩二

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
   
Testing 
--------------   
  * Do the following test:     
     cd to the work path     
    `$ python pdfConverter.py` 
    
  ![alt text](https://github.com/A2Zntu/HW2_Text_Mining/blob/master/picture/Pdf2txtSample.JPG "Logo Title Text 1")


## Co-occurence
  Install
--------------   
 * Install Package:
    ```
    $ pip install networkx    
     
    ```
 * rewrite the opensource of networkx to let `Chinese` words show on the nodes    
    Reference: [Reference Article](https://knowlab.wordpress.com/2016/05/25/networkx-%E7%B9%AA%E5%9C%96%E9%A1%AF%E7%A4%BA%E4%B8%AD%E6%96%87%E7%9A%84%E8%A7%A3%E6%B1%BA%E6%96%B9%E6%B3%95/?fbclid=IwAR3YM4IvHhNqzS3QMJVoe_vHISOnDczQSQfbRZepLNqImTvVEaQTEQJVUI4)
 
  Visualization  
 -------------- 
  * Co-oocurence matrix:       
    ![matrix](https://github.com/A2Zntu/HW2_Text_Mining/blob/master/picture/matrix1.JPG)
  * Co-oocurence matrix percentage:     
    ![matrix](https://github.com/A2Zntu/HW2_Text_Mining/blob/master/picture/matrix2.JPG)
 
    The size of matrix is 610 X 610. 
 
  * Co-oocurence Plot:              
    
  ![alt text](https://github.com/A2Zntu/HW2_Text_Mining/blob/master/picture/network1.png "Logo Title Text 1")
   
 
## cutword.py
* 讀取文本：讀取各基金公開說明書之txt檔
* 文字清理：去除標點符號與意義不大的詞彙
* 繁體中文分詞 
* 統計詞頻：針對每個基金文本，統計詞頻，以利後續TDM與co-occurrence matrix之製作

## generate_train_data.py
* 製作NER所需使用的train_data：由於助教的NER model只能辨識人、地、組織等詞彙，所以我們希望可以新增自訂類別，標記出跟基金市場較相關的術語，我們稱此類別為MKT(Market)。該檔案可以讀進文本、拆分每一個字、並且標記每一個字，如股(B-MKT)、價(I-MKT)，最後產出NER所需的train_data。
 ![image](https://github.com/A2Zntu/HW2_Text_Mining/blob/master/picture/train_data_mkt.JPG)


## NER 結果
* 嘗試要根據train_data_wmkt來訓練新的NER model，然而不知道哪邊出了錯誤，在訓練時頻頻卡關，因此只能用最原始的助教的model來跑公開說明書的文字。可預見的是，由於這些文字中少有人、地、組織等詞，NER標記效果並不好，標記出來的東西也對投資策略的分析沒有太大幫助。
 ![image](https://github.com/A2Zntu/HW2_Text_Mining/blob/master/ner/ner_result.jpg)
 
 
