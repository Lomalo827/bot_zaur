import vk_api, vk
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.longpoll import VkLongPoll, VkEventType
from datetime import datetime
from vk_api import VkUpload
import json
import requests
vk_session = vk_api.VkApi(token='vk1.a.GPEZR7_9v0QuPFn7V6zp-Q9S_ZN9t2hwJApn9Q2WopSeOdFD7DZlKWU6nU6co0ByF-Vkit1oTSVZc5ZogxhALkSqsW29vy2WPDLRdkw12ili4uNYoGrbYg4tI1uRC-jXKVEJDOWz47D6hDxJelyLBWPfKQKoDCP5S8JIOlNvaaRosfykCcM2UcfiB-P0RmcsAw1WhiY4qPpZqoprEuhGIA')
longpoll = VkBotLongPoll(vk_session,217290481)
vk = vk_session.get_api()
pic_dir = "C:\\Users\lo297rd\Desktop\гифка\\"
pic_path = pic_dir + '3x.gif'


def Time():
    now = datetime(2023, 11, 20, 5, 46, 00)
    then = datetime.now()
    duration = now - then 
    return str(duration)

def Gif():
    result = json.loads(requests.post(vk.docs.getMessagesUploadServer(type='doc', peer_id=event.object.message['peer_id'])['upload_url'], files={'file': open(pic_path, 'rb')}).text)
    jsonAnswer = vk.docs.save(file=result['file'], title='title', tags=[])
    vk.messages.send(peer_id=event.object.message['peer_id'], random_id=0, attachment=f"doc{jsonAnswer['doc']['owner_id']}_{jsonAnswer['doc']['id']}")


def sender(id,text):
    vk_session.method('messages.send',{'chat_id':id,'message':text,'random_id':0})

for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        if event.from_chat:
            id=event.chat_id
            print(id)
            msg=event.object.message['text'].lower()
            print(msg)
            uids = event.object.message['from_id']
            print(uids)


            if msg=='привет':
                sender(id,'чел выйди в окно')
            elif msg=='пойдешь в валик?':
                sender(id,'Пошёл нахуй')
            elif msg=='календарь':
                text=Time()
                print(text)
                sender(id,text)
            elif msg=='[id525320357|@butcherheadd]':
                sender(id,'нахуй ты меня тегаешь сын бляди')
                sender(id,')')
            #if uids==571968157:
                #Gif()
#245394383 
