# team-10

# 어플 이름 
_ 이화입시정보챗봇 [UNI]
# 어플 설명 
_ 이화대학을 목표로 입시를 준비하는 입시생들에게 입시 관련 정보를 제공해주는 어플입니다. 텔레그램 챗봇을 기반으로 하였습니다.\n
_ 어플 초반에 간단한 테스트로 단과대학 적성검사를 하는 부분이 있고, 이후 사용자가 원하는 입시정보를 얻을 수 있도록 구현하였습니다.
# 코드 설명
# 1. 전공 적성 검사
## 1.1. 키보드 버튼 생성
```
def build_menu(buttons, n_cols, header_buttons=None, footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, header_buttons)
    if footer_buttons:
        menu.append(footer_buttons)
    return menu
```
build_menu는 키보드에 선택지 버튼을 생성하는 함수입니다. buttons는 버튼에 들어갈 글자, n_cols는 버튼의 열 개수를 나타냅니다.

```
 def build_button(text_list, callback_header = "") : # make button list
    button_list = []
    text_header = callback_header
    if callback_header != "" :
        text_header += ","

    for text in text_list :
        button_list.append(InlineKeyboardButton(text, callback_data=text_header + text))

    return button_list
``` 
build_button은 키보드에 선택지 글자를 채우는 함수입니다.

## 1.2 질문 시작
get_command_1 함수로부터 질문을 하기 시작합니다.

```
 button_list = build_button(["매우 그렇다", "그렇다", "아니다","매우 아니다"]) 
``` 
build_button()함수를 호출하여 

"매우 그렇다"  "그렇다"
"아니다"  "매우 아니다" 

형태의 네가지 버튼을 생성합니다.


```
def callback_get(bot, update):

```
callback_get()함수는 사용자가 버튼을 선택했을때 응답을 해주는 함수입니다.

```
enginnering=0
nature=0
social=0
literature=0
```
단과대학에 관한 변수값을 초기화해주는 부분입니다.

```
for i in range(0,2):
 if(a[i]=="매우 그렇다"):
    enginnering+=3
    nature+=2
  elif(a[i]=="그렇다"):
    enginnering+=4
    nature+=2
```
만약 응답이 "매우 그렇다"였다면 enginerring(공과대학)의 점수를 3점 올려주고 nature(자연대학)의 점수를 2점 올려줍니다.
만약 응답이 "그렇다"였다면 enginerring의 점수를 4점 올려주고 nature의 점수를 2점 올려주는 식으로 전공의 적성을 맞춰갑니다.


```
if(enginnering>nature):
  bot.edit_message_text(text="당신은 공대에 적성이 맞아요!\n구체적 전공에 대한 정보를 알고 싶으신가요?".format(update.callback_query.data),
```
engineering이 nature보다 점수가 높았다면, 결과를 내보낸 후 









# 2. 이화입학처 사이트를 웹 크롤링하여 사용자가 입력한 키워드에 해당하는 전형별 FAQ 



















# 개발자 정보 
_ 김유진(yustarzz): 팀장, 중간 발표자, 기말 발표자, 웹 크롤링 구현\n
_ 허채령 (gommung): 적성검사 구현, 중간 발표자\n
_ 양한나 (iamhanna): 선택형 키보드 구현, 중간 ppt 제작, 기말 ppt 제작, 적성검사 구현\n
_ 윤혜원 (youuuoruon): 적성검사 질문 구성, 중간 ppt 제작, read me 파일 작성\n

# 라이센스
_ telegram open api:  GNU GPL licences\n
_ flashtext \n
_ beautifulsoup \n
_ requests \n

