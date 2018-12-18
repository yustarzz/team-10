# team-10

# 어플 이름 
_ 이화입시정보챗봇 [UNI]
# 어플 설명 
_ 이화대학을 목표로 입시를 준비하는 입시생들에게 입시 관련 정보를 제공해주는 어플입니다. 텔레그램 챗봇을 기반으로 하였습니다.\
_ 어플 초반에 간단한 테스트로 단과대학 적성검사를 하는 부분이 있고, 이후 사용자가 원하는 입시정보를 얻을 수 있도록 구현하였습니다.
# 코드 설명
# 1. 전공 적성 검사
## 1.1. 키보드 버튼 생성
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

```python
def help_handler(bot, update):
    print("start")    
    update.message.reply_text("안녕하세요.이 챗봇은 당신의 적성에 맞추어 학과를 알려드립니다. 자신의 적성을 확인 하고 싶으시다면,/get 을 눌러주세요 ") 
```
help_handler()함수는 이 챗봇을 소개하는 문구를 출력하고 /get을 입력하도록 돕는 역할을 합니다.

## 1.2 질문 시작
get_command_1 함수로부터 질문을 하기 시작합니다.

```python
 button_list = build_button(["매우 그렇다", "그렇다", "아니다","매우 아니다"]) 
``` 
build_button()함수를 호출하여 

"매우 그렇다"  "그렇다"
"아니다"  "매우 아니다" 

형태의 네가지 버튼을 생성합니다.

```python
update.message.reply_text("책을 읽는 것을 좋아합니까?", reply_markup=show_markup)
```
챗봇의 메시지를 업데이트하여 사용자에게 질문을 하는 함수입니다.

### callback_get()함수

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
for i in range(0,2):
 if(a[i]=="매우 그렇다"):
    enginnering+=3
    nature+=2
  elif(a[i]=="그렇다"):
    enginnering+=4
    nature+=2
```
만약 응답이 "매우 그렇다"였다면 engineering(공과대학)의 점수를 3점 올려주고 nature(자연대학)의 점수를 2점 올려줍니다.
만약 응답이 "그렇다"였다면 engineering의 점수를 4점 올려주고 nature의 점수를 2점 올려주는 식으로 전공의 적성을 맞춰갑니다.


```python
if(enginnering>nature):
  bot.edit_message_text(text="당신은 공대에 적성이 맞아요!\n구체적 전공에 대한 정보를 알고 싶으신가요?".format(update.callback_query.data),
```
engineering이 nature보다 점수가 높았다면, 결과를 내보낸 후 









# 2. 이화입학처 사이트를 웹 크롤링하여 사용자가 입력한 키워드에 해당하는 전형별 FAQ 



















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

