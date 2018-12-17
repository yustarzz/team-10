# team-10

# 어플 이름 
_ 이화입시정보챗봇 [UNI]
# 어플 설명 
_ 이화대학을 목표로 입시를 준비하는 입시생들에게 입시 관련 정보를 제공해주는 어플입니다. 텔레그램 챗봇을 기반으로 하였습니다.
  어플 초반에 간단한 테스트로 단과대학 적성검사를 하는 부분이 있고, 이후 사용자가 원하는 입시정보를 얻을 수 있도록 구현하였습니다.
# 코드 설명
# 1. 전공 적성 검사
# 1.1. 키보드 버튼 생성
def build_menu(buttons, n_cols, header_buttons=None, footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, header_buttons)
    if footer_buttons:
        menu.append(footer_buttons)
    return menu

    
- build_menu는 키보드에 선택지 버튼을 생성하는 함수입니다. buttons는 버튼에 들어갈 글자이고, n_cols는 버튼의 열 개수를 나타냅니다.

# 개발자 정보 
_ 김유진(yustarzz): 팀장, 중간 발표자, 입시정보 웹사이트에서 불러오기 구현
  허채령 (gommung): 적성검사 개발, 중간 발표자
  양한나 (iamhanna): 선택형 키보드 구현, 중간 ppt 제작
  윤혜원 (youuuoruon): 적성검사 질문 구성, 중간 ppt 제작

# 라이센스
_ telegram open api:  GNU GPL licences
