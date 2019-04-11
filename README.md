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
   
