#-*- coding: utf-8 -*-
import requests
import pandas


from bs4 import BeautifulSoup
from collections import defaultdict


'''
spider is crawler bot
'''

def spider():
    cfp_dic = defaultdict(lambda: defaultdict(str))
    k = 0
    url = 'https://research.cs.wisc.edu/dbworld/browse.html' #수집하려는 홈페이지 주소
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'lxml') #수집한 html 소스를 태그별로 파싱함

    for link in soup.select('td > a'): #<td><a ~~~>의 태그들만 선택
         href = link.get('href')
         title = link.string
         if title != 'web page': #수집하려는 홈페이지에 td> a중에 필요 없는 것들 제거하는 부분
            cfp_dic[k][href] = title
            k += 1

    return cfp_dic

def get_single_article(item_url): # url의 boby 부분의 text를 가져오기
    source_code = requests.get(item_url) # url 집어 넣기
    source_code.encoding = 'utf-8' # 인코딩설정.. 밑에 from_encoding써서 안써도 될지도...
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'lxml', from_encoding='utf-8') #BeautifulSoup로 html 이쁘게 가져오기(아마 tag 당 1줄씩)
    return_text = ''
    for contents in soup.select('body '):
        return_text += contents.text
        #print(contents.text)
    return return_text

def save_dbworld(file_name,dbworld_list):
    cfp_documents = ''
    for count in range(0,10): # 파일을 10개 만든다 0~9
        with open('./gs_data/' + file_name +str(count)+'.txt', 'w', encoding='UTF-8') as f: #파일이름은 file_name(0~9).txt
            for nlist in range(0+(count*100),100+(count*100)): #dbworld의 url list를 모두 사용하는경우 너무 많음 .... 적당히 끊어 사용하는게 중요 1000으로 바꾸면 하나당 2~3기가 나옴
                for key, value in dbworld_list[nlist].items():
                    cfp_documents += get_single_article(key)
                f.write(cfp_documents)
                f.write('\n')
        f.close()



