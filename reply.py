#__anthor: Administrator
#data:

import itchat
import requests

# 登录微信
itchat.auto_login(hotReload=True)
# 获取微信好友发的消息  根据发的消息回复
apiUrl = 'http://www.tuling123.com/openapi/api'

def get_info(message):
    data = {
        'key':'7236768c25d0452f9f6af189236c9b1d',
        'info':message,
        'userid':'robot'
    }
    try:
        r = requests.post(apiUrl,data=data).json()
        info = r['text']
        print("robot reply:%s"%info)
        return info
        #print(r)
    except:
        return

# get_info("吹")
#回复给微信好友
@itchat.msg_register(itchat.content.TEXT)
def auto_reply(msg):
    defaultReply = "我知道了"
    # 搜索微信好友
    realFriend = itchat.search_friends(name='陌生人')
    reallyFriendName = realFriend[0]['UserName']
    # print(reallyFriendName)
    # 打印好友回复的信息
    print("message:%s"%msg['Text'])
    #调用图灵接口
    reply = get_info(msg['Text'])
    if msg['FromUserName'] == reallyFriendName:
        itchat.send(reply,toUserName=reallyFriendName)

itchat.run()
