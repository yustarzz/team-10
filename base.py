from telegram.ext import Updater, MessageHandler, Filters, CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

my_token = '709534392:AAFdWbMMLsEw79NPKRUfkAp4Pn0TTTTJ5ek'

print('start telegram chat bot') 

updater = Updater(my_token)

def build_menu(buttons, n_cols, header_buttons=None, footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, header_buttons)
    if footer_buttons:
        menu.append(footer_buttons)
    return menu

def get_command_1(bot, update):
    print("get")
    show_list = []
    show_list.append(InlineKeyboardButton("매우 그렇다", callback_data="4")) # add on button
    show_list.append(InlineKeyboardButton("그렇다", callback_data="3")) # add off button
    show_list.append(InlineKeyboardButton("아니다", callback_data="2")) # add cancel button
    show_list.append(InlineKeyboardButton("매우 아니다", callback_data="1")) # add cancel button
    
    show_markup = InlineKeyboardMarkup(build_menu(show_list, len(show_list) - 2)) # make markup

    update.message.reply_text("수학보다 과학이 좋다.", reply_markup=show_markup)
    
def get_command_2(bot, update):
    print("get")
    show_list = []
    show_list.append(InlineKeyboardButton("매우 그렇다", callback_data="4")) # add on button
    show_list.append(InlineKeyboardButton("그렇다", callback_data="3")) # add off button
    show_list.append(InlineKeyboardButton("아니다", callback_data="2")) # add cancel button
    show_list.append(InlineKeyboardButton("매우 아니다", callback_data="1")) # add cancel button
    
    show_markup = InlineKeyboardMarkup(build_menu(show_list, len(show_list) - 2)) # make markup

    update.message.reply_text("수학보다 과학이 좋다.111", reply_markup=show_markup)
    
def callback_get(bot, update):
    print("callback")
    bot.edit_message_text(text="{}이(가) 선택되었습니다".format(update.callback_query.data),
                              chat_id=update.callback_query.message.chat_id, message_id=update.callback_query.message.message_id)
    
def callback_get_2(bot, update):
    print("callback")
    bot.edit_message_text(text="{}이(가) 선택되었습니다".format(update.callback_query.data),
                              chat_id=update.callback_query.message.chat_id, message_id=update.callback_query.message.message_id)

    
get_handler = CommandHandler('get', get_command_1)
updater.dispatcher.add_handler(CallbackQueryHandler(callback_get))
updater.dispatcher.add_handler(get_handler)
get_handler = CommandHandler('get', get_command_2)
updater.dispatcher.add_handler(CallbackQueryHandler(callback_get_2))

updater.start_polling(timeout=1, clean=True)
updater.idle()


