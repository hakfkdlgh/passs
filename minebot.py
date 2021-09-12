from telegram.ext import Updater, CallbackContext, ConversationHandler, CommandHandler, MessageHandler, Filters
from telegram import Update, replykeyboardmarkup,ReplyKeyboardRemove
from telegram.ext.dispatcher import run_async
from selenium import webdriver
from time import sleep
import os
import re
FIRST, SECOND, THIRD, FOURTH, FIFTH = range(5)
list_user = [1151302009,1441899112,602932056,227757126, 1058301966, 1016599904, 1499075612, 936009070, 299179006, 400790755, 1041239919, 1031703091, 179719213, 731574428, 99457546, 207710021, 102128530, 107940984,
             1371442978, 1329582518, 13496107881490389033, 564522674, 295805339, 1152520531, 171487373, 1257014953, 1427068010, 1275793537, 1325003318, 1361607478, 1391326237, 220933247, 98605327]
token = '1632732324:AAFa2heoBQnNUDigD_5LaViZBEf-L0B7wso'
namee = {}
timee = {}
msg = {}
url = {}


@run_async
def start(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    global namee, timee, msg, url
    namee[chat_id] = ''
    timee[chat_id] = ''
    msg[chat_id] = ''
    url[chat_id] = ''
    if chat_id in list_user:
        context.bot.sendMessage(
            chat_id, 'سلام به ربات خوش امدید\nاین ربات توسط @mmn_jvt  ساخته شده است')
        buttons = [
            ['رفتن سر کلاس']]

        update.message.reply_text(text="سرویس مورد نظر خود را انتخاب کنید", reply_markup=replykeyboardmarkup.ReplyKeyboardMarkup(
            buttons, one_time_keyboard=True, resize_keyboard=True))
    else:
        context.bot.sendMessage(
            chat_id, 'شما اجازه استفاده از ربات را ندارید')


@run_async
def namm(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    if chat_id in list_user:
        update.message.reply_text(text="نام نمایشی خود را جهت نمایش در کلاس را وارد کنید", reply_markup=ReplyKeyboardRemove())
        return FIRST
    else:
        context.bot.sendMessage(
            chat_id, 'شما اجازه استفاده از ربات را ندارید')

@run_async

def time(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    context.bot.sendMessage(
        chat_id, 'زمان بسته شدن کلاس بعد از ورود را اعلام کنید\nبر حسب دقیقه \n از اعداد انگیلسی استفاده کنید\nحداکثر زمان 90 دقیقه میباشد\nجهت برگشت به منوی اصلی /menu را ارسال کنید')
    nam = update.message.text
    global namee
    namee[chat_id] = nam

    return SECOND

@run_async
def service(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    x = update.message.text
    try:
        x = int(x)
        if x > 90:
            update.message.reply_text(
                text='زمان وارده بیشتر 90 دقیقه می باشد\n\nدوباره وارد کنید\nجهت برگشت به منوی اصلی /menu را ارسال کنید')
        elif x <= 90:
            global timee

            timm = x
            timee[chat_id] = timm
            update.message.reply_text(
                text='پیام خود را جهت ارسال در چت باکس وارد کنید\nمیتوانید با ارسال /skip از این مرحله رد شوید\n\nجهت برگشت به منوی اصلی /menu را ارسال کنید')

            return THIRD
    except:
        update.message.reply_text(text='لطفا یک عدد بین 1 تا 90 ارسال کنید')

@run_async
def mesage(update: Update, context: CallbackContext):
    msgg = update.message.text
    chat_id = update.message.chat_id
    global msg
    msg[chat_id] = msgg


    update.message.reply_text(text='لینک کلاس مورد نظر خود را وارد کنید:\nتوجه: لینک به صورت کامل باشد(باhttps شروع شود)\nجهت برگشت به منوی اصلی /menu را ارسال کنید')
    return FOURTH
@run_async
def skip_mesage(update: Update, context: CallbackContext):
    
    chat_id = update.message.chat_id
    global msg
    msg[chat_id] = ''
    

    update.message.reply_text(text='لینک کلاس مورد نظر خود را وارد کنید:\nتوجه: لینک به صورت کامل باشد(باhttps شروع شود)\nجهت برگشت به منوی اصلی /menu را ارسال کنید')
        
    return FOURTH
@run_async
def urll(update: Update, context: CallbackContext):
    chat_id=update.message.chat_id
    text=update.message.text
    if re.search('^https://www..*',text):
        global url
        url[chat_id]=text
        update.message.reply_text(text='تایید نهایی و رفتن به کلاس\nجهت برگشت به منوی اصلی /menu را ارسال کنید', reply_markup=replykeyboardmarkup.ReplyKeyboardMarkup(
        [['تایید']], one_time_keyboard=True, resize_keyboard=True))
        return FIFTH
    else:
        update.message.reply_text(text='لینک ارسالی شما معتبر یا کامل نمیباشد\nدوباره ارسال کنید\n\nجهت برگشت به منوی اصلی /menu را ارسال کنید')

        

@run_async
def seleniom(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    message_id = update.message.message_id
    global timee, msg, namee ,url
    path = os.path.dirname(os.path.abspath(__file__ )) 
    address = os.path.join(path , 'geckodriver.exe')
    context.bot.sendMessage(chat_id=chat_id,text='در حال باز کردن مرورگر')
    driver = webdriver.Firefox(executable_path=address)
    context.bot.editMessageText('رفتن به ادرس مورد نظر', chat_id, message_id+1)
    driver.get(url[chat_id])
    sleep(1)
    driver.find_element_by_xpath('//*[@id="btn_guest"]').click()
    sleep(1)
    try:
        driver.find_element_by_xpath(
            '/html/body/div[5]/div[2]/div/input').send_keys(namee[chat_id])
        context.bot.editMessageText('رفتن به داخل کلاس', chat_id, message_id+1)
        sleep(1)
        driver.find_element_by_xpath(
            '/html/body/div[5]/div[3]/div[2]/button').click()
        context.bot.editMessageText('حاضر در کلاس', chat_id, message_id+1)
        sleep(1)
        driver.find_element_by_xpath(
            '//*[@id="sidebar"]/div[4]/div[2]/div/div[2]/div[3]/div[1]').send_keys(msg[chat_id])
        sleep(1)
        context.bot.editMessageText(
            'ارسال پیام در چت باکس', chat_id, message_id+1)
        driver.find_element_by_xpath('//*[@id="shape_send"]/path').click()
        
        for i in range(timee[chat_id]):
            x = timee[chat_id] - i
            context.bot.editMessageText(
                'کلاس در {}دقیقه بسته میشود'.format(x), chat_id, message_id+1)
            sleep(60)
    except:
        context.bot.editMessageText(
        'کلاس هنوز شروع نشده است', chat_id, message_id+1)
        sleep(10)        
        
    driver.close()
    context.bot.editMessageText(
        'از کلاس خارج شد\nجهت برگشت به منوی اصلی /menu را ارسال کنید', chat_id, message_id+1)
    timee[chat_id] = ''
    msg[chat_id] = ''
    namee[chat_id] = ''


@run_async
def close(update: Update, context: CallbackContext):

    chat_id = update.effective_chat.id

    buttons = [
        ['رفتن سر کلاس']]

    update.message.reply_text(text="سرویس مورد نظر خود را انتخاب کنید", reply_markup=replykeyboardmarkup.ReplyKeyboardMarkup(
        buttons, one_time_keyboard=True, resize_keyboard=True))
    return ConversationHandler.END

def main() -> None:
    updater = Updater(token, request_kwargs={'proxy_url': 'socks5h://127.0.0.1:9150'})

    
    conver_service = ConversationHandler(
        entry_points=[MessageHandler(Filters.regex('رفتن سر کلاس'), namm)],
        states={
            FIRST: [MessageHandler(Filters.text, time)],
            SECOND: [MessageHandler(Filters.text, service)],
            THIRD: [MessageHandler(Filters.text, mesage),CommandHandler('skip',skip_mesage)],
            FOURTH: [MessageHandler(Filters.text, urll)],
            FIFTH: [MessageHandler(Filters.regex('^تایید$'),seleniom)]


        }, fallbacks=[CommandHandler('menu',  close)]
    )
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(conver_service)

    updater.start_polling()
    updater.idle()
if __name__ == '__main__':
    main()