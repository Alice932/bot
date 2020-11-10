from vk_api.longpoll import VkLongPoll, VkEventType
from twilio.rest import Client
import vk_api
import random
import time
import os
from datetime import datetime
import vk


login, password = "логин", "пароль"
vk_session = vk_api.VkApi(login=login, password=password, app_id=2685278)
vk_session.auth(token_only=True)

session = vk.Session()
vk_api = vk.API(session)


session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)
word_list = []
nothing = ''
my_name = 'НедоАлиса'

def send_message(vk_session, message=None ):
   vk_session.method('messages.send',{'user_id': event.user_id, 'message': message, 'random_id': random.randint(-2147483638, +2147483648)})

def send_chat_message(vk_session, message = None ):
   vk_session.method('messages.send',{'chat_id': event.chat_id, 'message': message, 'random_id': 0})

def sleep_thread(sleepWait, sleepTime):
    timeStart = time.time()
    timeElapsed = 0

    while timeElapsed <= sleepWait:
        timeElapsed = time.time() - timeStart
        print('time elapsed = ' + str(timeElapsed))
        time.sleep(10)

    print('going to sleep. zzz....')
    # Sleep for x
    time.sleep(sleepTime)
    print('im awake!')

#def check_status(user_id, fields):
#  vk.users.get(user_id=165118535, fields='online')

own_words = {    "hello":('привет','здравствуй','здравствуйте','дарова','шалом','прив','утро','эй'),

                 "name":('арс','арсений','сеня','сень','сенечка','сенька','юрков','арс,'),

                 "night":('сна','споки','снов','ночи','спа'),

            }



   #USER_ONLINE = 165118535




for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW :
        print('Сообщение пришло в: ' + str(datetime.strftime(datetime.now(), "%H:%M:%S")))
        print('Текст сообщения: ' + str(event.text))
        #print(event.user_id)
        response = event.text.lower()
        new_status = vk_api.users.get(access_token = 'токен', user_id = 165118535, v = 5.126, fields = ["online"])
        online_status = new_status[0]["online"]
        print(online_status)

        if online_status == 1:

            if event.from_user and not (event.from_me):

                full = ''.join(response)
                for word in full.split():
                    if word in (own_words["name"]):
                        vk_session.method('messages.send',{'user_id': event.user_id,'message':my_name+': Действительно, Арсений','random_id':0})
                    elif word in (own_words["hello"]):
                        vk_session.method('messages.send',{'user_id': event.user_id,'message':my_name+': Приветик','random_id':0})
                    elif word in (own_words["night"]):
                        vk_session.method('messages.send',{'user_id': event.user_id,'message':my_name+': Спокойного сна','random_id':0})



            elif event.from_user:
                if response == 'я в тебя верю':
                     vk_session.method('messages.send',{'user_id': event.chat_id,'message':my_name+': И я в тебя тоже верю','random_id':0})

            elif event.from_chat and (event.from_me):

                full = ''.join(response)
                for word in full.split():
                    if word == 'недоалиса' and 'тихо':
                       send_chat_message(vk_session, message=my_name+': Ладно, ухожу' )
                       #sleep_thread(50, 30)


            elif event.from_chat and not (event.from_me):

                full = ''.join(response)
                for word in full.split():
                    if word in (own_words["name"]):
                        send_chat_message(vk_session, message=my_name+': Действительно, Арсений' )


                if response == "шабелян +":
                    vk_session.method('messages.send',{'chat_id': event.chat_id,'message':'Юрков+','random_id':0})
                elif response == "шабелян+":
                    vk_session.method('messages.send',{'chat_id': event.chat_id,'message':'Юрков+','random_id':0})

                #elif response == "арсений":
                 #   vk_session.method('messages.send',{'chat_id': event.chat_id,'message': my_name+': Он ответит вам попозже,если это срочно, напишите "Срочно Арс", я ему передам ','random_id':0})
                elif response == "срочно арс":
                    vk_session.method('messages.send',{'chat_id': event.chat_id,'message':my_name+': Минуточку','random_id':0})

                 # Your Account Sid and Auth Token from twilio.com/console
                 # and set the environment variables. See http://twil.io/secure
                 # account_sid = os.environ['AC3e76b45ac589cae92c7abb7590a986f0']
                 #auth_token = os.environ['d012a129faf064e48d3e20264bd00ff1']
                 #client = Client(account_sid, auth_token)

                 #call = client.calls.create(
                  #      twiml='<Response><Say>Ahoy, World!</Say></Response>',
                   #     to='+79781031932',
                    #    from_='+12058907532'
                    #)

                #print(call.sid)

        else:
            if event.from_user and not (event.from_me):

                send_message(vk_session, message= my_name + ': Приииветик. Это НедоАлиса, помощница Арсения. Его сейчас пока нет. Но он ответит вам позже! ' )
                send_message(vk_session, message= my_name +': Если хотите пообщаться, то напишите мое имя. Если нет, то можете просто не отвечать) ')



            elif event.from_chat and not (event.from_me):

                if response == "шабелян +":
                    vk_session.method('messages.send',{'chat_id': event.chat_id,'message':'Юрков+','random_id':0})
                elif response == "шабелян+":
                    vk_session.method('messages.send',{'chat_id': event.chat_id,'message':'Юрков+','random_id':0})





