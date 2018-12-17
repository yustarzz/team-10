#-*- coding: utf-8 -*- 
import requests
from bs4 import BeautifulSoup
for i in range(1,4):
    url = 'http://admission.ewha.ac.kr/enter/doc/rolling/faq.asp?page=%d&s_board_category=BBS0402&s_search_cate=&s_search_type=&s_search_text=&p_board_id=BBS0001&p_site_type=MAM0001' %i
    response= requests.get(url)

    source = response.text
    soup = BeautifulSoup(source, 'html.parser')
    
    #top_list = soup.findAll('li[class=dep1 on]') 
    top_list = soup.findAll('a',{"class":"tit"})
    
    from flashtext import KeywordProcessor
    keyword_processor=KeywordProcessor()
    for i in range(0,len(top_list)):
        a=top_list[i].text
       
        
        keyword_processor.add_keyword('자기소개서')
        keywords_found=keyword_processor.extract_keywords(a)
    
        if(keywords_found):
         print(a)
    #answer=input(무엇이 궁금하신가요)
    #if answer
    #print(span[])

