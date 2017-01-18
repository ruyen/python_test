#-*- coding: utf-8 -*-
'''
테스트 용도 페이지 web_crawler, scholar_crawler 및 word2vec 관련
'''
import web_crawler
import gword2vec
import scholar_crawler




'''
수집부분 output : temp_list 는 dictionary list 이고, {html(key): title(value)}로 구성 -> 다음 단계에서 html 기반으로 get single article 써써 긁어오기
'''
# dbworld 사이트에서 데이터 수집
dbworld_list = web_crawler.spider() #dbworld에서 하이퍼링크만 가져온다
web_crawler.save_dbworld('dbworld', dbworld_list) # db월드의 하이퍼링크 기반으로 10개의 txt 파일 만듦(대략 2~300메가)

# 위의 파일에 대해 전처리 필요






# 구글 학술검색에서 데이터 수집
gsch_terms = 'reputation' # 구글 학술검색 키워드 입력 (나중에 유저 입력이되는 부분)
scholar_crawler.gscholar_craw(gsch_terms) # gs_data 폴더 안에 키워드.txt로 json 형태로 저장됨



'''
temp_list에서 get_single_article(html)로 text 긁어오기
'''


print("it is done 2")




'''
word2vec part
'''
model = gword2vec.set_input('./gs_data/', './vector_model', 200, 10, 3, 2)
model.similar_by_word('big', topn=20, restrict_vocab=None) # 단어, 유사도 높은거 몇개까지 볼지, 유니크 단어에서 몇개 볼지(None은 제약이 없는거고 1000개면 unique term 중 1000개 보겠다는거... 단어가 무수히 많을때 속도를 위해 사용


'''
Scholar crawler
'''
