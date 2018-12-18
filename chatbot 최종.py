from telegram.ext import Updater, MessageHandler, Filters, CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

my_token =  '709534392:AAFdWbMMLsEw79NPKRUfkAp4Pn0TTTTJ5ek'
eltec=0

print('start telegram chat bot')

updater = Updater(my_token)


def build_menu(buttons, n_cols, header_buttons=None, footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, header_buttons)
    if footer_buttons:
        menu.append(footer_buttons)
    return menu
   

def build_button(text_list, callback_header = "") : # make button list
    button_list = []
    text_header = callback_header
    if callback_header != "" :
        text_header += ","

    for text in text_list :
        button_list.append(InlineKeyboardButton(text, callback_data=text_header + text))

    return button_list

def help_handler(bot, update):
    print("start")    
    update.message.reply_text("안녕하세요.이 챗봇은 당신의 적성에 맞추어 학과를 알려드립니다. 자신의 적성을 확인 하고 싶으시다면,/get 을 눌러주세요 ") # reply text with markup



def get_command_1(bot, update):
    print("get")
    button_list = build_button(["매우 그렇다", "그렇다", "아니다","매우 아니다"]) # make button list
    show_markup = InlineKeyboardMarkup(build_menu(button_list, len(button_list) - 2)) # make markup
    update.message.reply_text("책을 읽는 것을 좋아합니까?", reply_markup=show_markup) # reply text with markup
    global count
    count=0
  

def callback_get(bot, update):
    data_selected = update.callback_query.data
    print("callback : ", data_selected) 
    if(count==0):
        if len(data_selected.split(",")) == 1 :
            button_list = build_button(["매우 그렇다", "그렇다", "아니다","매우 아니다"], data_selected)
            show_markup = InlineKeyboardMarkup(build_menu(button_list, len(button_list) - 2))
            bot.edit_message_text(text="무언가 탐구 하는 것을 좋아합니까?",
                                  chat_id=update.callback_query.message.chat_id,
                                  message_id=update.callback_query.message.message_id,
                                  reply_markup=show_markup)
        if len(data_selected.split(",")) == 2 :
            button_list = build_button(["매우 그렇다", "그렇다", "아니다","매우 아니다"], data_selected)
            show_markup = InlineKeyboardMarkup(build_menu(button_list, len(button_list) - 2))
            bot.edit_message_text(text="새로운 언어를 배우는 것에 흥미를 느낍니까?",
                                  chat_id=update.callback_query.message.chat_id,
                                  message_id=update.callback_query.message.message_id,
                                  reply_markup=show_markup)
        if len(data_selected.split(",")) == 3 :
            button_list = build_button(["매우 그렇다", "그렇다", "아니다","매우 아니다"], data_selected)
            show_markup = InlineKeyboardMarkup(build_menu(button_list, len(button_list) - 2))
            bot.edit_message_text(text="기계의 작동 원리에 대해 흥미를 느낍니까?",
                                  chat_id=update.callback_query.message.chat_id,
                                  message_id=update.callback_query.message.message_id,
                                  reply_markup=show_markup)   
        if len(data_selected.split(",")) == 4:
            button_list = build_button(["매우 그렇다", "그렇다", "아니다","매우 아니다"], data_selected)
            show_markup = InlineKeyboardMarkup(build_menu(button_list, len(button_list) - 2))
            bot.edit_message_text(text="답이 딱 정해져 나오는 문제를 좋아합니까?",
                                  chat_id=update.callback_query.message.chat_id,
                                  message_id=update.callback_query.message.message_id,
                                  reply_markup=show_markup)

        elif len(data_selected.split(",")) == 5 :
            a=[]
            a=update.callback_query.data.split(',')
            enginnering=0        
            literature=0

            if (a[0]=="매우 그렇다"):               
                literature+=3
            elif (a[0]=="그렇다"):
                literature+=1
            elif (a[0]=="아니다"):
                enginnering+=1
            else:
                enginnering+=3
                
            if (a[1]=="매우 그렇다"):               
                literature+=1
                enginnering+=3
            elif (a[1]=="그렇다"):            
                enginnering+=1
            elif (a[1]=="아니다"):
                literature+=1
            else:
                literature+=3
                
            if (a[2]=="매우 그렇다"):               
                literature+=3
                enginnering+=1
            elif (a[2]=="그렇다"):
                literature+=1
            elif (a[2]=="아니다"):
                enginnering+=1
            else:
                enginnering+=3
                   
            if (a[3]=="매우 그렇다"):
                enginnering+=3
            elif (a[3]=="그렇다"):
                enginnering+=2
            elif (a[3]=="아니다"):
                literature+=1
            else:
                literature+=3

            if (a[4]=="매우 그렇다"):
                enginnering+=3
            elif (a[4]=="그렇다"):
                enginnering+=1
            elif (a[4]=="아니다"):
                literature+=1
            else:
                literature+=3
                
            if(enginnering>literature):
                bot.edit_message_text(text="당신은 공대에 적성이 맞아요!\n구체적 전공에 대한 정보를 알고 싶으신가요?".format(update.callback_query.data),
                                  chat_id=update.callback_query.message.chat_id,
                                  message_id=update.callback_query.message.message_id)
                eltec=1

            else:
                bot.edit_message_text(text="당신은  인문대학에 적성이 맞아요!구체적 전공에 대한 정보를 알고 싶으신가요?".format(update.callback_query.data),
                                  chat_id=update.callback_query.message.chat_id,
                                  message_id=update.callback_query.message.message_id)
    else:
        data_selected = update.callback_query.data
        print("callback : ", data_selected)     
        if len(data_selected.split(",")) == 1 :
            button_list  = build_button(["매우 그렇다", "그렇다", "아니다","매우 아니다"], data_selected)
            show_markup = InlineKeyboardMarkup(build_menu(button_list, len(button_list) - 2))
            bot.edit_message_text(text="생명을 다루는 것에 관심이 있나요?",
                                              chat_id=update.callback_query.message.chat_id,
                                              message_id=update.callback_query.message.message_id,
                                              reply_markup=show_markup)
        if len(data_selected.split(",")) == 2 :
            button_list = build_button(["매우 그렇다", "그렇다", "아니다","매우 아니다"], data_selected)
            show_markup = InlineKeyboardMarkup(build_menu(button_list, len(button_list) - 2))
            bot.edit_message_text(text="외우는 것보다 이해하는 것이 좋은가요?",
                                              chat_id=update.callback_query.message.chat_id,
                                              message_id=update.callback_query.message.message_id,
                                              reply_markup=show_markup)
        if len(data_selected.split(",")) == 3 :
            button_list = build_button(["매우 그렇다", "그렇다", "아니다","매우 아니다"], data_selected)
            show_markup = InlineKeyboardMarkup(build_menu(button_list, len(button_list) - 2))
            bot.edit_message_text(text="기계의 작동 원리에 대해 흥미를 느끼나요?",
                                              chat_id=update.callback_query.message.chat_id,
                                              message_id=update.callback_query.message.message_id,
                                              reply_markup=show_markup)
                        

        elif len(data_selected.split(",")) == 4 :
                       
             b=update.callback_query.data.split(',')
             chemical=0       
             engine=0
             if (b[0]=="매우 그렇다"):
                chemical+=3
                
             elif (b[0]=="그렇다"):
                chemical+=1
             elif (b[0]=="아니다"):
                engine+=1
             else:
                engine+=3
                            
             if (b[1]=="매우 그렇다"):               
                           chemical+=1
                           
             elif (b[1]=="그렇다"):            
                            chemical+=1
             elif (b[1]=="아니다"):
                            engine+=1
             else:
                            engine+=3
                            
             if (b[2]=="매우 그렇다"):               
                            engine+=3
                            chemical+=1
             elif (b[2]=="그렇다"):
                            engine+=1
             elif (b[2]=="아니다"):
                                chemical+=1
             else:
                                chemical+=3
                                   
             if (b[3]=="매우 그렇다"):
                                engine+=3
             elif (b[3]=="그렇다"):
                                engine+=2
                                chemical+=1
             elif (b[3]=="아니다"):
                                chemical+=1
             else:
                                chemical+=0
                             

             if(engine>chemical):
                                bot.edit_message_text(text="당신은 기계공학과에 적성이 맞아요!".format(update.callback_query.data),
                                                  chat_id=update.callback_query.message.chat_id,
                                                  message_id=update.callback_query2.message.message_id)           

             else:
                                bot.edit_message_text(text="당신은 화학공학과에 적성이 맞아요!".format(update.callback_query.data),
                                                  chat_id=update.callback_query.message.chat_id,
                                                  message_id=update.callback_query.message.message_id)
                    

            

def get_command_more(bot, update):
    
    print("aboutmore")
    button_list = build_button(["매우 그렇다", "그렇다", "아니다","매우 아니다"]) # make button list
    show_markup = InlineKeyboardMarkup(build_menu(button_list, len(button_list) - 2)) # make markup
    update.message.reply_text("화학을 좋아하시나요?", reply_markup=show_markup) # reply text with markup
    global count
    count=1



def get_message(bot, update):
                if update.message.text== "네" :
                    update.message.reply_text("/aboutmore 을 눌러주세요!")
                elif update.message.text== "아니오" :
                    update.message.reply_text('이용해주셔서 감사합니다~다시 시작을 원하시면 /start 를 다시 눌러주세요!')


help_handler = CommandHandler('start',help_handler)
updater.dispatcher.add_handler(help_handler)

get_handler = CommandHandler('get', get_command_1)
updater.dispatcher.add_handler(CallbackQueryHandler(callback_get))
updater.dispatcher.add_handler(get_handler)



get_handler_1 = CommandHandler('aboutmore', get_command_more)
updater.dispatcher.add_handler(CallbackQueryHandler(callback_get))
updater.dispatcher.add_handler(get_handler_1)


message_handler = MessageHandler(Filters.text, get_message)
updater.dispatcher.add_handler(message_handler)



updater.start_polling(timeout=1, clean=True)
updater.idle()

