#-*- coding: utf-8 -*-

import web_crawler





'''
수집부분 output : temp_list 는 dictionary list 이고, {html(key): title(value)}로 구성 -> 다음 단계에서 html 기반으로 get single article 써써 긁어오기
'''
print("ready to craw the data")

temp_list = web_crawler.spider()
# print(temp_list)
print("it is done 1")


'''
temp_list에서 get_single_article(html)로 text 긁어오기
'''
cfp_documents = ''
for key, value in temp_list[0].items():
    cfp_documents = web_crawler.get_single_article(key)

print(cfp_documents)

print("it is done 2")


'''
word2vec part
'''
