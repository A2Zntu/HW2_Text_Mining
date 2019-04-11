# train_data_wmkt
將公開說明書的文字標記完新的分類後(B-MKT, I-MKT)，新增至原本NER的train_data中。以便之後訓練model用。

# ner_result
嘗試要根據train_data_wmkt來訓練新的NER model，然而不知道哪邊出了錯誤，在訓練時頻頻卡關，因此只能用最原始的助教的model來跑公開說明書的文字。可預見的是，由於這些文字中少有人、地、組織等詞，NER標記效果並不好，標記出來的東西也對投資策略的分析沒有太大幫助。
