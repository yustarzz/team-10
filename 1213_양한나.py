from telegram.ext import Updater, MessageHandler, Filters, CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

my_token = '709534392:AAFdWbMMLsEw79NPKRUfkAp4Pn0TTTTJ5ek'
eltec=0
a=[]
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



def get_command_1(bot, update):
    print("get")
    button_list = build_button(["매우 그렇다", "그렇다", "아니다","매우 아니다"]) # make button list
    show_markup = InlineKeyboardMarkup(build_menu(button_list, len(button_list) - 2)) # make markup
    update.message.reply_text("과학을 좋아하시나요?", reply_markup=show_markup) # reply text with markup

def callback_get(bot, update):
    data_selected = update.callback_query.data
    print("callback : ", data_selected) 
    
    if len(data_selected.split(",")) == 1 :
        button_list = build_button(["매우 그렇다", "그렇다", "아니다","매우 아니다"], data_selected)
        show_markup = InlineKeyboardMarkup(build_menu(button_list, len(button_list) - 2))
        bot.edit_message_text(text="수학을 좋아하시나요?",
                              chat_id=update.callback_query.message.chat_id,
                              message_id=update.callback_query.message.message_id,
                              reply_markup=show_markup)
    if len(data_selected.split(",")) == 2 :
        button_list = build_button(["매우 그렇다", "그렇다", "아니다","매우 아니다"], data_selected)
        show_markup = InlineKeyboardMarkup(build_menu(button_list, len(button_list) - 2))
        bot.edit_message_text(text="영어를 좋아하시나요?",
                              chat_id=update.callback_query.message.chat_id,
                              message_id=update.callback_query.message.message_id,
                              reply_markup=show_markup)
        

    elif len(data_selected.split(",")) == 3 :
       
        a=update.callback_query.data.split(',')
        enginnering=0
        nature=0
        social=0
        literature=0
 
        for i in range(0,2):

            if(a[i]=="매우 그렇다"):
                enginnering+=3
                nature+=2
            elif(a[i]=="그렇다"):
                enginnering+=4
                nature+=2
               
        if(enginnering>nature):
            bot.edit_message_text(text="당신은 공대에 적성이 맞아요!\n구체적 전공에 대한 정보를 알고 싶으신가요?".format(update.callback_query.data),
                              chat_id=update.callback_query.message.chat_id,
                              message_id=update.callback_query.message.message_id)
            eltec=1

        else:
            bot.edit_message_text(text="당신은 자연대학에 적성이 맞아요!".format(update.callback_query.data),
                              chat_id=update.callback_query.message.chat_id,
                              message_id=update.callback_query.message.message_id)

def get_command_more(bot, update):
    print("get")
    button_list = build_button(["매우 그렇다", "그렇다", "아니다","매우 아니다"]) # make button list
    show_markup = InlineKeyboardMarkup(build_menu(button_list, len(button_list) - 2)) # make markup
    update.message.reply_text("과학을 좋아하시나요?", reply_markup=show_markup) # reply text with markup

def callback_get_more(bot, update):
    data_selected = update.callback_query.data
    print("callback : ", data_selected) 
    
    if len(data_selected.split(",")) == 1 :
        button_list = build_button(["매우 그렇다", "그렇다", "아니다","매우 아니다"], data_selected)
        show_markup = InlineKeyboardMarkup(build_menu(button_list, len(button_list) - 2))
        bot.edit_message_text(text="수학을 좋아하시나요?",
                              chat_id=update.callback_query.message.chat_id,
                              message_id=update.callback_query.message.message_id,
                              reply_markup=show_markup)
    if len(data_selected.split(",")) == 2 :
        button_list = build_button(["매우 그렇다", "그렇다", "아니다","매우 아니다"], data_selected)
        show_markup = InlineKeyboardMarkup(build_menu(button_list, len(button_list) - 2))
        bot.edit_message_text(text="영어를 좋아하시나요?",
                              chat_id=update.callback_query.message.chat_id,
                              message_id=update.callback_query.message.message_id,
                              reply_markup=show_markup)
        

    elif len(data_selected.split(",")) == 3 :
       
        a=update.callback_query.data.split(',')
        enginnering=0
        nature=0
        social=0
        literature=0
 
        for i in range(0,2):

            if(a[i]=="매우 그렇다"):
                enginnering+=3
                nature+=2
            elif(a[i]=="그렇다"):
                enginnering+=4
                nature+=2
               
        if(enginnering>nature):
            bot.edit_message_text(text="당신은 공대에 적성이 맞아요!\n구체적 전공에 대한 정보를 알고 싶으신가요?".format(update.callback_query.data),
                              chat_id=update.callback_query.message.chat_id,
                              message_id=update.callback_query.message.message_id)
            

        else:
            bot.edit_message_text(text="당신은 자연대학에 적성이 맞아요!".format(update.callback_query.data),
                              chat_id=update.callback_query.message.chat_id,
                              message_id=update.callback_query.message.message_id)


def get_message(bot, update):
                if update.message.text== "네" :
                    update.message.reply_text("/aboutmore 을 눌러주세요!")
                elif update.message.text== "아니오" :
                    update.message.reply_text('이용해주셔서 감사합니다~다시 시작을 원하시면 /start 를 다시 눌러주세요!')
        
get_handler = CommandHandler('start', get_command_1)
updater.dispatcher.add_handler(CallbackQueryHandler(callback_get))
updater.dispatcher.add_handler(get_handler)

get_handler_1 = CommandHandler('aboutmore', get_command_more)
updater.dispatcher.add_handler(get_handler_1)
updater.dispatcher.add_handler(CallbackQueryHandler(callback_get_more))

message_handler = MessageHandler(Filters.text, get_message)
updater.dispatcher.add_handler(message_handler)



updater.start_polling(timeout=1, clean=True)
updater.idle()












