from telegram.ext import Updater, MessageHandler, Filters, CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

my_token = '722762604:AAF29yuhip0j8Pal1yj_TL7iUv5EwuWArQ0'

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
    button_list = build_button(["1", "2", "3"]) # make button list
    show_markup = InlineKeyboardMarkup(build_menu(button_list, len(button_list) - 1)) # make markup
    update.message.reply_text("과학을 어느정도 좋아하시나요", reply_markup=show_markup) # reply text with markup

def callback_get(bot, update):
    data_selected = update.callback_query.data
    print("callback : ", data_selected) 
    
    if len(data_selected.split(",")) == 1 :
        button_list = build_button(["1", "2", "3"], data_selected)
        show_markup = InlineKeyboardMarkup(build_menu(button_list, len(button_list) - 1))
        bot.edit_message_text(text="경영을을 좋아하시나요?",
                              chat_id=update.callback_query.message.chat_id,
                              message_id=update.callback_query.message.message_id,
                              reply_markup=show_markup)       

    elif len(data_selected.split(",")) == 2 :
        bot.edit_message_text(text="{}이(가) 선택되었습니다".format(update.callback_query.data),
                              chat_id=update.callback_query.message.chat_id,
                              message_id=update.callback_query.message.message_id)
        a=update.callback_query.data.split(',')
        computer =10
        print(a)
        for i in a:
            computer+=1
            print(computer)


      



        
get_handler = CommandHandler('start', get_command_1)
updater.dispatcher.add_handler(CallbackQueryHandler(callback_get))
updater.dispatcher.add_handler(get_handler)



updater.start_polling(timeout=1, clean=True)
updater.idle()


