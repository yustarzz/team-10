# team-10

# 어플 이름 
_ 이화입시정보챗봇 [UNI]
# 어플 설명 
_ 이화대학을 목표로 입시를 준비하는 입시생들에게 입시 관련 정보를 제공해주는 어플입니다. 텔레그램 챗봇을 기반으로 하였습니다.\
_ 어플 초반에 간단한 테스트로 단과대학 적성검사를 하는 부분이 있고, 이후 사용자가 원하는 입시정보를 얻을 수 있도록 구현하였습니다.

# 사용법
## 전공 적성 평가
![uni3](https://user-images.githubusercontent.com/43199383/50168269-6044a080-032e-11e9-933a-0e12331d6115.png)
![uni4](https://user-images.githubusercontent.com/43199383/50168640-36d84480-032f-11e9-949a-2590867824c4.png)  
Telegram에서 EwhaInfo를 검색해서 클릭합니다.  
Start버튼을 누르면  


![image](https://user-images.githubusercontent.com/43199383/50168418-bd405680-032e-11e9-88fb-135a6c188166.png)  
챗봇에 관한 설명이 나온 후 /test를 눌러달라는 메시지가 나옵니다. 


![uni5](https://user-images.githubusercontent.com/43199383/50168837-ae0dd880-032f-11e9-9e8a-930cdf32b14c.png)  
/test를 누르면 이런식으로 적성 검사를 위한 질문과 선택지가 표시되고 선택을 하면 다른 질문으로 바뀝니다.  
단과대학에 관한 질문은 총 5개입니다. 이 질문을 전부 마친다면  

![image](https://user-images.githubusercontent.com/43199383/50168988-004ef980-0330-11e9-8ee9-93777e72beac.png)  
자신의 적성에 맞는 단과대를 출력해줍니다.  
/aboutliberal을 눌러준다면 나에게 맞는 전공을 검사해볼 수 있습니다.  

![image](https://user-images.githubusercontent.com/43199383/50169313-b31f5780-0330-11e9-9b77-dca3b3ddec20.png)  
그 단과대학에 해당하는 세부적인 질문에 답을 할 수 있게 됩니다.  
전공검사에 관한 질문은 총 5개입니다. 이 질문도 전부 마치면  
  
![image](https://user-images.githubusercontent.com/43199383/50169526-190bdf00-0331-11e9-9e71-3a60b790fcc2.png)   
최종 결과를 보여줍니다.  
해당 전공에 대해 더 많은 정보를 알고싶은 사람을 위해 링크를 제공합니다.  

## FAQ
사용자가 원하는 정보를 입학처 FAQ에서 크롤링하여 제공합니다.  
사용자가 "자기소개서"를 입력했다면  
![image](https://user-images.githubusercontent.com/43199383/50169901-ef06ec80-0331-11e9-8e65-1c6196f4f489.png)  
입학처 FAQ 사이트에서 "자기소개서"가 있는 질문을 크롤링하여 표시해줍니다.

# 코드 설명
# 1. 전공 적성 평가
## 1.1. 키보드 버튼 생성

### build_menu()
```python
def build_menu(buttons, n_cols, header_buttons=None, footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, header_buttons)
    if footer_buttons:
        menu.append(footer_buttons)
    return menu
```
build_menu는 키보드에 선택지 버튼을 생성하는 함수입니다. buttons는 버튼에 들어갈 글자, n_cols는 버튼의 열 개수를 나타냅니다.  


### build_button()
```python
 def build_button(text_list, callback_header = "") : # make button list
    button_list = []
    text_header = callback_header
    if callback_header != "" :
        text_header += ","

    for text in text_list :
        button_list.append(InlineKeyboardButton(text, callback_data=text_header + text))

    return button_list
``` 
build_button()은 키보드에 선택지 글자를 채우는 함수입니다.  

### help_handler()
```python
def help_handler(bot, update):
    print("start")    
    update.message.reply_text("안녕하세요.이 챗봇은 당신의 적성에 맞추어 학과를 알려드립니다. 자신의 적성을 확인 하고 싶으시다면, /test 을 눌러주세요 ")
```
help_handler()함수는 이 챗봇을 소개하는 문구를 출력하고 /test를 누르도록 돕는 역할을 합니다.
![uni1](https://user-images.githubusercontent.com/43199383/50166273-0fcb4400-032a-11e9-9f91-82f13a8a77a6.PNG)

  
## 1.2. 질문 시작
### get_command_1()
사용자가 /test를 눌렀다면
get_command_1 함수로부터 질문을 하기 시작합니다.

```python
 button_list = build_button(["매우 그렇다", "그렇다", "아니다","매우 아니다"]) 
``` 
build_button()함수를 호출하여  

![uni2](https://user-images.githubusercontent.com/43199383/50166377-4c973b00-032a-11e9-890b-afddda6f96f3.PNG)

이 형태의 네가지 버튼을 생성합니다.  

```python
update.message.reply_text("책을 읽는 것을 좋아합니까?", reply_markup=show_markup)
```
사용자에게 질문을 하는 메시지를 출력하도록 bot의 message를 업데이트(변경)합니다.  

### callback_get()
```python
def callback_get(bot, update):
```
callback_get()함수는 사용자가 버튼을 선택했을때 응답을 해주는 함수입니다.  
또한 사용자로부터 응답이 온 후의 질문도 이 함수 안에 들어있습니다.  
  
```python
if len(data_selected.split(",")) == 1 :
            button_list = build_button(["매우 그렇다", "그렇다", "아니다","매우 아니다"], data_selected)
            show_markup = InlineKeyboardMarkup(build_menu(button_list, len(button_list) - 2))
            bot.edit_message_text(text="무언가 탐구 하는 것을 좋아합니까?",
            chat_id=update.callback_query.message.chat_id,
            message_id=update.callback_query.message.message_id,
            reply_markup=show_markup)
```
build_menu()함수로 사용자에게 선택지 키보드를 띄우고, edit_message_text()함수로 질문을 변경해 줍니다.  

```python
a=[]
a=update.callback_query.data.split(',')
enginnering=0        
literature=0
```
단과대학에 관한 변수값을 초기화해주는 부분입니다.  
a[]는 받아온 응답을 저장하는 배열입니다.  

```python
if (a[0]=="매우 그렇다"):               
                literature+=3
            elif (a[0]=="그렇다"):
                literature+=1
            elif (a[0]=="아니다"):
                enginnering+=1
            else:
                enginnering+=3
```
만약 응답이 "매우 그렇다"였다면 literature(인문대학)의 점수를 3점 올려주고  
"그렇다"였다면 literature의 점수를 1점 올려주고  
"아니다"였다면 engineering(공과대학)의 점수를 1점 올려주고  
그 외 "매우 아니다" 였다면 engineering의 점수를 3점 올려줍니다.  

이런 식으로 응답에 따라 점수를 누적하여 어느 단과대학과 더 맞는지 찾아갈 수 있도록 합니다.  

```python
if(enginnering>literature):
                bot.edit_message_text(text="당신은 공대에 적성이 맞아요!\n구체적 전공에 대한 정보를 알고 싶으신가요? 그렇다면 /aboutengine 를                  눌러주세요!".format(update.callback_query.data),
                 chat_id=update.callback_query.message.chat_id,
                 message_id=update.callback_query.message.message_id)
                eltec=1
else:
                bot.edit_message_text(text="당신은  인문대학에 적성이 맞아요!구체적 전공에 대한 정보를 알고 싶으신가요? 그렇다면 /aboutliberal                  를 눌러주세요!".format(update.callback_query.data),
                 chat_id=update.callback_query.message.chat_id,
                 message_id=update.callback_query.message.message_id)

```
engineering이 literature보다 점수가 높았다면 bot의 메시지를 "당신은 공대에 적성이 맞아요!"로 변경해줍니다.   
그 후 /aboutengine을 누르도록 도움말을 줍니다.  

만약 literature이 engineering보다 점수가 높았다면 bot의 메시지를 "당신은  인문대학에 적성이 맞아요!"로 변경해줍니다.  
그 후 /aboutliberal을 누르도록 도움말을 줍니다.  
  

같은 형식으로 단과대학선택에 관한 5개의 질문과 선택지를 출력 합니다.  
  

### 단과대학이 공대가 되었다면  
```python
elif count==1:
```  
```python
if len(data_selected.split(",")) == 1 :
            button_list  = build_button(["매우 그렇다", "그렇다", "아니다","매우 아니다"], data_selected)
            show_markup = InlineKeyboardMarkup(build_menu(button_list, len(button_list) - 2))
            bot.edit_message_text(text="물리를 좋아하시나요?",
            chat_id=update.callback_query.message.chat_id,
            message_id=update.callback_query.message.message_id,
            reply_markup=show_markup)
```
위와 같은 형식으로 전공파악을 하는 구체적인 질문을 하도록 합니다.  

```python
b=update.callback_query.data.split(',')
chemical=0       
engine=0
```
전공 점수를 초기화하는 부분입니다.  
b[]는 받아온 응답을 저장하는 배열입니다.  

```python
if (b[0]=="매우 그렇다"):
    chemical+=3
elif (b[0]=="그렇다"):
    chemical+=1
elif (b[0]=="아니다"):
    engine+=1
else:
    engine+=3
```
마찬가지로 1번 응답에대해 선택지별로 전공점수를 따로 주는 조건문입니다.  

## 1.3. 적성검사 최종 결과 출력
```python
if (engine>chemical):
                bot.edit_message_text(text="당신은 컴퓨터 공학과에 적성이 맞아요!\n 
                컴퓨터 공학과는 이해와 원리에 대한 공부를 좋아하는 당신에게 적합한 전공입니다.\n
                자세한 정보는 http://cse.ewha.ac.kr/ 를 참고해주세요!".format(update.callback_query.data),
                chat_id=update.callback_query.message.chat_id,message_id=update.callback_query.message.message_id)          

else:
                bot.edit_message_text(text="당신은 화학공학과에 적성이 맞아요!".format(update.callback_query.data),
                chat_id=update.callback_query.message.chat_id,
                message_id=update.callback_query.message.message_id)
```
engine이 chemical보다 높았다면 bot의 메시지를 "당신은 컴퓨터 공학과에 적성이 맞아요!"로 출력한 후  
사용자가 전공에 대한 자세한 정보를 빠르게 접하기 쉽도록 링크를 추가합니다.  
chemical이 engine보다 높은 경우도 같습니다.  
  
## 1.4. 전공에 관한 추가 정보

# 2. 이화입학처 사이트를 웹 크롤링하여 사용자가 입력한 키워드에 해당하는 전형별 FAQ 
## 2.1. 사용자로부터 키워드 입력받기
```python
keyword=input("키워드를 입력해주세요: ")
```
input()함수로 사용자로부터 입학 정보에 대해 알고싶은 키워드를 입력받도록 합니다.  
  
## 2.2. 질문, 답변 크롤링
```python
url = 'http://admission.ewha.ac.kr/enter/doc/rolling/faq.asp?page=%d&s_board_category=BBS0402&s_search_cate=&s_search_type=&s_search_text=&p_board_id=BBS0001&p_site_type=MAM0001'
```
이화여자대학교 입학처 FAQ사이트 url입니다. 이 사이트에서 keyword를 기반으로 원하는 정보를 크롤링합니다.  
(keyword가 포함되어있는 질문과 질문에 대한 답변)\
  

```python
question=soup.findAll('a',{"class":"tit"})
answer=soup.findAll('div',{"class":"txt"})
```
FAQ부분 html에서 'a'에서 <tit>클래스를 크롤링한 결과를 qusetion에 저장합니다.  
똑같이 'div'에서 <txt>클래스를 크롤링한 결과를 answer에 저장합니다.  
  

```python
for i in range(0,len(question)):
    question[i]=str(i)+" "+question[i].text
```
question배열에 크롤링한 question을 차례대로 정리하여 저장하는 부분입니다.  
  

```python
for i in range(0,len(answer)):
    answer[i]=answer[i].text
```
answer배열에 크롤링한 answer을 차례대로 정리하여 저장하는 부분입니다.  
  






# 개발자 정보 
_ 김유진(yustarzz): 팀장, 중간 발표자, 기말 발표자, 웹 크롤링 구현\
_ 허채령 (gommung): 적성검사 구현, 중간 발표자\
_ 양한나 (iamhanna): 선택형 키보드 구현, 중간 ppt 제작, 기말 ppt 제작, 적성검사 구현\
_ 윤혜원 (youuuoruon): 적성검사 질문 구성, 중간 ppt 제작, read me 파일 작성

# 라이센스
_ telegram open api:  GNU GPL licences\
_ flashtext \
_ beautifulsoup \
_ requests

