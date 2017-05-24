import requests
from wxpy import *
import json


#图灵机器人
def talks_robot(info = 'tt'):
    api_url = 'http://www.tuling123.com/openapi/api'
    apikey = '48144a905f564f4e8b3a996072c17d07'
    data = {'key': apikey,
                'info': info}
    req = requests.post(api_url, data=data).text
    replys = json.loads(req)['text']
    return replys

#微信自动回复
robot = Bot()
# 回复来自其他好友、群聊和公众号的消息
@robot.register()
def reply_my_friend(msg):
    message = '{}'.format(msg.text)
    replys = talks_robot(info=message)
    return replys

# 开始监听和自动处理消息
robot.start()
embed()