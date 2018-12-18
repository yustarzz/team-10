#-*- coding: utf-8 -*- 
import requests
from bs4 import BeautifulSoup




#수시 버튼을 클릭했을 때

keyword=input("키워드 입력해주세요: ")
for i in range(1,4):
    url = 'http://admission.ewha.ac.kr/enter/doc/rolling/faq.asp?page=%d&s_board_category=BBS0402&s_search_cate=&s_search_type=&s_search_text=&p_board_id=BBS0001&p_site_type=MAM0001' %i
    response= requests.get(url)

    
    source = response.text
    soup = BeautifulSoup(source, 'html.parser')
    
    top_list = soup.findAll('li',{"class":"dep1 on"})

    question=soup.findAll('a',{"class":"tit"})
    answer=soup.findAll('div',{"class":"txt"})

    for i in range(0,len(question)):
        question[i]=str(i)+" "+question[i].text

    for i in range(0,len(answer)):
        answer[i]=answer[i].text
 


        
   
   
    from flashtext import KeywordProcessor
    keyword_processor=KeywordProcessor()
    for i in range(0,len(question)):
  
        
       keyword_processor.add_keyword(keyword)
       keywords_found=keyword_processor.extract_keywords(question[i])
    
       if(keywords_found):
              finalquestion=question[i].split('Q')[1]
              print(finalquestion)
              print(answer[i])
           


	
#정시 버튼을 클릭했을 때
keyword=input("키워드 입력해주세요: ")
for i in range(1,2):
    url = 'http://admission.ewha.ac.kr/enter/doc/regular/faq.asp'
    response= requests.get(url)

    
    source = response.text
    soup = BeautifulSoup(source, 'html.parser')
    
    top_list = soup.findAll('li',{"class":"dep1 on"})

    question=soup.findAll('a',{"class":"tit"})
    answer=soup.findAll('div',{"class":"txt"})

    for i in range(0,len(question)):
        question[i]=str(i)+" "+question[i].text

    for i in range(0,len(answer)):
        answer[i]=answer[i].text
 


        
   
   
    from flashtext import KeywordProcessor
    keyword_processor=KeywordProcessor()
    for i in range(0,len(question)):
  
        
       keyword_processor.add_keyword(keyword)
       keywords_found=keyword_processor.extract_keywords(question[i])
    
       if(keywords_found):
              finalquestion=question[i].split('Q')[1]
              print(finalquestion)
              print(answer[i])



#재외국민과 외국인
keyword=input("키워드 입력해주세요: ")
for i in range(1,2):
    url = 'http://admission.ewha.ac.kr/enter/doc/abroad/faq.asp'
    response= requests.get(url)

    
    source = response.text
    soup = BeautifulSoup(source, 'html.parser')
    
    top_list = soup.findAll('li',{"class":"dep1 on"})

    question=soup.findAll('a',{"class":"tit"})
    answer=soup.findAll('div',{"class":"txt"})

    for i in range(0,len(question)):
        question[i]=str(i)+" "+question[i].text

    for i in range(0,len(answer)):
        answer[i]=answer[i].text
 


        
   
   
    from flashtext import KeywordProcessor
    keyword_processor=KeywordProcessor()
    for i in range(0,len(question)):
  
        
       keyword_processor.add_keyword(keyword)
       keywords_found=keyword_processor.extract_keywords(question[i])
    
       if(keywords_found):
              finalquestion=question[i].split('Q')[1]
              print(finalquestion)
              print(answer[i])


#편입학/의대학사편입학
keyword=input("키워드 입력해주세요: ")
for i in range(1,3):
    url = 'http://admission.ewha.ac.kr/enter/doc/transfer/faq.asp?page=%d&s_board_category=BBS0405&s_search_cate=&s_search_type=&s_search_text=&p_board_id=BBS0001&p_site_type=MAM0001' %i
    response= requests.get(url)

    
    source = response.text
    soup = BeautifulSoup(source, 'html.parser')
    
    top_list = soup.findAll('li',{"class":"dep1 on"})

    question=soup.findAll('a',{"class":"tit"})
    answer=soup.findAll('div',{"class":"txt"})

    for i in range(0,len(question)):
        question[i]=str(i)+" "+question[i].text

    for i in range(0,len(answer)):
        answer[i]=answer[i].text
 


        
   
   
    from flashtext import KeywordProcessor
    keyword_processor=KeywordProcessor()
    for i in range(0,len(question)):
  
        
       keyword_processor.add_keyword(keyword)
       keywords_found=keyword_processor.extract_keywords(question[i])
    
       if(keywords_found):
              finalquestion=question[i].split('Q')[1]
              print(finalquestion)
              print(answer[i])


#약대입학/편입학
keyword=input("키워드 입력해주세요: ")
for i in range(1,3):
    url = 'http://admission.ewha.ac.kr/enter/doc/pharmacy/faq.asp?page=%d&s_board_category=BBS0406&s_search_cate=&s_search_type=&s_search_text=&p_board_id=BBS0001&p_site_type=MAM0001' %i
    response= requests.get(url)

    
    source = response.text
    soup = BeautifulSoup(source, 'html.parser')
    
    top_list = soup.findAll('li',{"class":"dep1 on"})

    question=soup.findAll('a',{"class":"tit"})
    answer=soup.findAll('div',{"class":"txt"})

    for i in range(0,len(question)):
        question[i]=str(i)+" "+question[i].text

    for i in range(0,len(answer)):
        answer[i]=answer[i].text
 


        
   
   
    from flashtext import KeywordProcessor
    keyword_processor=KeywordProcessor()
    for i in range(0,len(question)):
  
        
       keyword_processor.add_keyword(keyword)
       keywords_found=keyword_processor.extract_keywords(question[i])
    
       if(keywords_found):
              finalquestion=question[i].split('Q')[1]
              print(finalquestion)
              print(answer[i])




