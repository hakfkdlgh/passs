import re
from telegram.ext import Updater, CallbackContext, ConversationHandler, CommandHandler, MessageHandler, Filters, updater
from telegram import Update, replykeyboardmarkup,ReplyKeyboardRemove

import random

token = '1632732324:AAFa2heoBQnNUDigD_5LaViZBEf-L0B7wso'
setting = {'lower_alp': 'True', 'upper_alph': 'True', 'symbols': 'True', 'numbers': 'True', 'lengh':10}
account = {}
test_list = {}
# '''-----------------------------------------------------------------------------------__________________________'''
def start(update: Update, context: CallbackContext):
    update.message.reply_text(reply_to_message_id=update.message.message_id,text='''سلام🤗
        من bitwarden هستم
        میتونم در مدیریت پسورد ها بهت کمک کنم
        با دستور /generate میتونم یه پسورد برات بسازم
        با دستور /setting میتونی تنظیمات تولید پسورد را تغییر دهی
        با دستور /add_account یک اکانت اضافه کن
        با دستور /account هم به حساب هایی که سیو کردی، دسترسی داری''')

def generate_pass(update: Update, context: CallbackContext):
    lower_alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
              'v', 'w', 'x', 'y', 'z']
    upper_alph = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
              'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4','5', '6', '7', '8', '9']
    symbols = ['~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '{', '[', '}', ']', '|', ';',
           '<', '>', '.', '?', '/']
    def settingg():
        if setting['lower_alp'] == 'True' and setting['symbols'] == 'True' and setting['upper_alph'] == 'True' and setting[
        'numbers'] == 'True':
            return lower_alph + upper_alph + numbers + symbols

        if setting['lower_alp'] == 'False' and setting['symbols'] == 'True' and setting['upper_alph'] == 'True' and setting[
        'numbers'] == 'True':
            return upper_alph + numbers + symbols

        if setting['lower_alp'] == 'True' and setting['symbols'] == 'False' and setting['upper_alph'] == 'True' and setting[
        'numbers'] == 'True':
            return lower_alph + upper_alph + numbers

        if setting['lower_alp'] == 'True' and setting['symbols'] == 'True' and setting['upper_alph'] == 'False' and setting[
        'numbers'] == 'True':
            return lower_alph + numbers + symbols

        if setting['lower_alp'] == 'True' and setting['symbols'] == 'True' and setting['upper_alph'] == 'True' and setting[
        'numbers'] == 'False':
            return lower_alph + upper_alph + symbols

        if setting['lower_alp'] == 'False' and setting['symbols'] == 'False' and setting['upper_alph'] == 'True' and setting[
        'numbers'] == 'True':
            return   upper_alph + numbers
        if setting['lower_alp'] == 'False' and setting['symbols'] == 'True' and setting['upper_alph'] == 'False' and setting[
        'numbers'] == 'True':
            return    numbers + symbols
        if setting['lower_alp'] == 'False' and setting['symbols'] == 'True' and setting['upper_alph'] == 'True' and setting[
        'numbers'] == 'False':
            return   upper_alph +  symbols
        if setting['lower_alp'] == 'False' and setting['symbols'] == 'False' and setting['upper_alph'] == 'False' and setting[
        'numbers'] == 'True':
            return numbers 
        if setting['lower_alp'] == 'False' and setting['symbols'] == 'False' and setting['upper_alph'] == 'True' and setting[
        'numbers'] == 'False':
            return upper_alph 
        if setting['lower_alp'] == 'False' and setting['symbols'] == 'True' and setting['upper_alph'] == 'False' and setting[
        'numbers'] == 'False':
            return symbols
        if setting['lower_alp'] == 'True' and setting['symbols'] == 'False' and setting['upper_alph'] == 'False' and setting[
        'numbers'] == 'False':
            return lower_alph 
        if setting['lower_alp'] == 'True' and setting['symbols'] == 'False' and setting['upper_alph'] == 'False' and setting[
        'numbers'] == 'True':
            return lower_alph +  numbers 
        if setting['lower_alp'] == 'True' and setting['symbols'] == 'False' and setting['upper_alph'] == 'True' and setting[
        'numbers'] == 'False':
            return lower_alph + upper_alph  
        if setting['lower_alp'] == 'True' and setting['symbols'] == 'True' and setting['upper_alph'] == 'False' and setting[
        'numbers'] == 'False':
            return lower_alph + symbols
        if setting['lower_alp'] == 'False' and setting['symbols'] == 'False' and setting['upper_alph'] == 'False' and setting[
        'numbers'] == 'False':
            return None 

    def final_dic_and_pass(dict):
        try:
                       
            x = random.choices(dict, k=setting['lengh'])
            return ''.join(x)
        except:
            return 'can not generate pass word\n❌❌change the setting❌❌'
    update.message.reply_text(text=f'your password is ready\n{final_dic_and_pass(settingg())}')

def setting_command(update: Update, context: CallbackContext):
    update.message.reply_text(text=f'''the current setting is:
    use  Uppercase letters: A-Z = {setting['upper_alph']}
    use Lowercase letters: a-z = {setting['lower_alp']}
    use Numbers: 0-9 = {setting['numbers']}
    use Symbols: ~`! @#$%^&*()_-+=[]|\:;"'<,>.?/ = {setting['symbols']}
    length of generated password = {setting['lengh']} ''')
    update.message.reply_text(text='to change the setting use these buttoms',reply_markup=replykeyboardmarkup.ReplyKeyboardMarkup(keyboard=[
        ['Uppercase','Lowercase'],
        ['Numbers','Symbols'],
        ['length']
    ],resize_keyboard=True,one_time_keyboard=True))
def lowercase(update: Update, context: CallbackContext):
    if setting['lower_alp']=='True':
        setting['lower_alp']='False'
    if setting['lower_alp']=='False':
        setting['lower_alp']='True'
    update.message.reply_text(text='Done!',reply_markup=ReplyKeyboardRemove())
def uppercase(update: Update, context: CallbackContext):
    if setting['upper_alph']=='True':
        setting['upper_alph']='False'
    if setting['upper_alph']=='False':
        setting['upper_alph']='True'
    update.message.reply_text(text='Done!',reply_markup=ReplyKeyboardRemove())
def symbols(update: Update, context: CallbackContext):
    if setting['symbols']=='True':
        setting['symbols']='False'
    if setting['symbols']=='False':
        setting['symbols']='True'
    update.message.reply_text(text='Done!',reply_markup=ReplyKeyboardRemove())
def numbers(update: Update, context: CallbackContext):
    # global setting
    if setting['numbers']=='True':
        setting.update({'numbers':'False'})
    if setting['numbers']=='False':
        setting.update({'numbers':'True'})

    print(setting['numbers'])
    update.message.reply_text(text='Done!',reply_markup=ReplyKeyboardRemove())

def show_accounts(update: Update, context: CallbackContext):
    for key in account:
        update.message.reply_text(text=f'''account name:{key}
        username: {account[key][-2]}
        password: {account[key][-1]}''')
def add_accounts(update: Update, context: CallbackContext):
    update.message.reply_text(text="add your accont's name",reply_to_message_id=update.message.message_id)
    return 1
     
def user(update: Update, context: CallbackContext):
    name = update.message.text
    test_list.update({'name':name})
    update.message.reply_text(text='add your username')
    return 2

def password(update: Update, context: CallbackContext):
    userr = update.message.text
    test_list.update({'user':userr})
    update.message.reply_text(text='add your password')
    return 3
def done(update: Update, context: CallbackContext):
    passs = update.message.text
    account.update({test_list["name"]:[test_list["user"],passs]})
    
    update.message.reply_text(text=f'''Done! the account {test_list["name"]}
    {test_list['user']}:{passs}
has been added. you can see your saved accounts by using /account
you can add another account by /add_account ''')
    # del test_list[-1]
    # del test_list[-1]
    return -1
def cancel_acc(update: Update, context: CallbackContext) -> int:
    show_accounts(update ,context)
    return -1
# '''------------------------------------------------------------------------------------------------------------------------------------------'''
updater = Updater(token='1632732324:AAFa2heoBQnNUDigD_5LaViZBEf-L0B7wso', request_kwargs={'proxy_url': 'socks5h://127.0.0.1:9150'})

conver =ConversationHandler(
    entry_points=[CommandHandler('add_account',add_accounts)],
    states={
        1:[MessageHandler(Filters.text,user)],
        2:[MessageHandler(Filters.text,password)],
        3:[MessageHandler(Filters.text,done)]
    },
    fallbacks=[CommandHandler('account',cancel_acc)]
)
updater.dispatcher.add_handler(CommandHandler('start',start))
updater.dispatcher.add_handler(CommandHandler('generate',generate_pass))
updater.dispatcher.add_handler(CommandHandler('setting',setting_command))
updater.dispatcher.add_handler(MessageHandler(Filters.regex('^Uppercase$'),uppercase))
updater.dispatcher.add_handler(MessageHandler(Filters.regex('^Lowercase$'),lowercase))
updater.dispatcher.add_handler(MessageHandler(Filters.regex('^Numbers$'),numbers))
updater.dispatcher.add_handler(MessageHandler(Filters.regex('^Symbols$'),symbols))
updater.dispatcher.add_handler(CommandHandler('account',show_accounts))
updater.dispatcher.add_handler(conver)

updater.start_polling()
print('Run')
updater.idle()
