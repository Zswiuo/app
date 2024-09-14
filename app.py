import telebot
from telebot import types

id = 6535731385

bot = telebot.TeleBot("7094592781:AAFJQGcd8SUY4zHszdPzTIWgr5-wbW6fk0Q") 

ch = "-1001589366226" # ايدي قناتك هنا لاتمسح -100
t = ['creator', 'member', 'administrator']
use = "l0_Il0"

@bot.message_handler(commands=["start"])
def start(message):
    if message.chat.type == 'private':
        user_id = str(message.from_user.id)        
        with open("ids.txt", 'a+') as file:
            file.seek(0)          
            if user_id not in file.read():
                file.write(user_id + '\n')

    if bot.get_chat_member(chat_id=ch, user_id=message.from_user.id).status not in t:
        
        bot.reply_to(message, "عذرا عزيزي المستخدم ، \n عليك الاشتراك بقنوات البوت لتتمكن من استخدامة [ {}] \n- - - - - - - - - - \n اشترك من ثم ارسل /start".format(use))
        return            
    idu = message.from_user.id
    tnt = types.InlineKeyboardMarkup(row_width=1)
    s1 = types.InlineKeyboardButton("رفع حظر رقم" , callback_data="rqm")
    s2 = types.InlineKeyboardButton("رفع حظر من الخاص" , callback_data="rav")
    s3 = types.InlineKeyboardButton("رفع حظر من الخاص بالرسائل" , callback_data="msg")
    tnt.add(s1,s2,s3)
    bot.reply_to(message, f"مرحبا صديقي  [{message.from_user.first_name}](tg://user?id={message.from_user.id})\n البوت يحتوي على مجموعة خطوات لفك حظر التليجرام استخدم الي يناسبك من الازرار 👇",parse_mode="markdown",reply_markup=tnt)
    
    if idu == id:
        but = types.InlineKeyboardMarkup(row_width=1)
        a2 = types.InlineKeyboardButton("اذاعة", callback_data="all")
        a3 = types.InlineKeyboardButton("ارسل التخزين", callback_data="send_file")
        but.add(a2)
        but.add(a3)
        bot.reply_to(message, "مرحبا عزيزي المطور \n هذه هي لوحة التحكم الخاصة بك\n اذا تريد تعرف احصائيات البوت ارسل /stats", reply_markup=but)        
        
	
@bot.callback_query_handler(func=lambda call: call.data == "rqm")
def callback_query(call):
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='''▪️كيفية استرجاع حسابك في التيليجرام
1-تدخل على موقع:

https://telegram.org/support 


2-تكتب هذه الرساله في اول سطر


 My Telegram account was deleted by mistake. Please help me retrieve it with all of its data again

3-بالسطر الثاني تكتب بريدك الالكتروني المتوفر على جهازك

4-بالسطر الثالث تكتب رقم هاتفك المحذوف او محضور

ملاحظة : الطريقة مضمونة 90% و لا تحاول اكثر من مرة انتظر لكي يتم الرد عليك من الشركة''')
	
	
	
@bot.callback_query_handler(func=lambda call: call.data == 'rqm')
def callback_query(call):
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='''▪️كيفية استرجاع حسابك في التيليجرام
1-تدخل على موقع:

https://telegram.org/support 


2-تكتب هذه الرساله في اول سطر


 My Telegram account was deleted by mistake. Please help me retrieve it with all of its data again

3-بالسطر الثاني تكتب بريدك الالكتروني المتوفر على جهازك

4-بالسطر الثالث تكتب رقم هاتفك المحذوف او محضور

ملاحظة : الطريقة مضمونة 90% و لا تحاول اكثر من مرة انتظر لكي يتم الرد عليك من الشركة''')

@bot.callback_query_handler(func=lambda call: call.data == 'rav')
def callback_query(call):
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='''اول شي تدخل للبوت - @SpamBot - 
من ثم تضغط  - هذا خطا - 

من ثم تضغط - نعم - 

من ثم - لا لم اقم بهذا قط -  

من ثم ترسل: 

 Hello Telegram Support, a hacker reported on my account for no reason. Please lift the restrictions as soon as possible
وتنتضر . . .''')

@bot.callback_query_handler(func=lambda call: call.data == 'msg')
def callback_query(call):
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='''- اذا تريد البدء ارسل /run''')

@bot.message_handler(commands=["run"])
def run(message):
    w = 0 
    while w < 15:
        w = w + 1
        bot.send_message(message.chat.id, text= "{}".format(w))

        		
@bot.message_handler(commands=["stats"])
def stats(message):
    if message.from_user.id == id:  # تأكد أن معرف المرسل هو معرف المطور المخول
        with open("ids.txt") as file:
            lines = file.readlines()
            # تصفية الأسطر الفارغة والتي تحتوي على مسافات بيضاء
            clean_lines = [line.strip() for line in lines if line.strip()]
            num_users = len(clean_lines)
        bot.reply_to(message, f"عدد أعضاء البوت: {num_users}")


##############################

@bot.callback_query_handler(func=lambda call: True)
def calldata(call):
    if call.data == "send_file":
        with open("ids.txt", "r") as file:
            bot.send_document(call.message.chat.id, file)
    elif call.data == "all":
        bot.send_message(call.message.chat.id, "• ارسل الان ماتريد إذاعته • \n نص - صورة - ملف")
        bot.register_next_step_handler(call.message, send_broadcast_message)

def send_broadcast_message(message):
    with open("ids.txt", "r") as file:
        user_ids = file.readlines()
        for user_id in user_ids:
            if message.text:
                bot.send_message(user_id.strip(), text=message.text)
            elif message.photo:
                bot.send_photo(user_id.strip(), photo=message.photo[-1].file_id, caption=message.caption)
            elif message.document:
                bot.send_document(user_id.strip(), data=message.document.file_id, caption=message.caption, parse_mode='Markdown')
# @world_father
# @world_father
@bot.callback_query_handler(func=lambda call: True)
def calldata(call):
    if call.data == "send_file":
        with open("ids.txt", "r") as file:
            bot.send_document(call.message.chat.id, file)

print("- - this bot done run - -")
bot.polling()
