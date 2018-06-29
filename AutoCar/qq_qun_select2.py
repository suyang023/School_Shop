from qqbot import QQBotSlot as qqbotslot, RunBot
import re
import time

@qqbotslot
def onQQMessage(bot, contact, member, content):
    username = ['重庆顺风车发单1群']
    chengkename = '重庆顺风车拼车1群'
    divername_all = ['双体科技']
    # username = ['laoda']
    ps = '\nPS:需要长期固定区域接单的司机请私聊群主接单！'

    for i in range(0, len(username)):
        user = username[i]
        #司机发单免费群
        b1 = bot.List('group', user)
        #乘客发单免费群
        b2 = bot.List('group', chengkename)
        # b1 = bot.List('buddy', user)
        if content.find('人找车') != -1:

            #检测是否含有电话号码
            try:
                matchResult = re.search(r'(\d+)',content)  # 从指定位置开始匹配
                vlaue_phone = matchResult.groups(0)
            except BaseException :
                vlaue_phone = ''
            if vlaue_phone != '':
                content2 = content.replace('人找车','人-找-车')
                if b1:
                    b = b1[0]
                bot.SendTo(b, content2+ps)
            # bot.SendTo(contact, '你好，我是QQ机器人')

        elif content.find('车找人') != -1:
            content2 = content.replace('车找人','车-找-人')
            if b2:
                b = b2[0]
            bot.SendTo(b, content2)
                 
        elif content == '-测试-':
            if b1:
                b = b1[0]
            bot.SendTo(b, '你是不是傻！')

        elif content == '-stop':
            b1 = bot.List('buddy', "巴渝山")
            if b1:
                b = b1[0]
            bot.SendTo(b, '网页QQ机器人已关闭')
            # bot.SendTo(contact, 'QQ机器人已关闭')
            bot.Stop()
        elif i>len(username):
            break
        time.sleep(0.1)

    for i in range(0, len(divername_all)):
          
        # b1 = bot.List('buddy', user)
        if content.find('人找车') != -1:
            #检测是否含有电话号码
            try:
                matchResult = re.search(r'(\d+)',content)  # 从指定位置开始匹配
                vlaue_phone = matchResult.groups(0)
            except BaseException :
                vlaue_phone = ''
            if vlaue_phone != '':
                content2 = content.replace('人找车','人-找-车')
                
                if 'test' == contact.name:
                    divername = ['氵','巴渝山']
                    for a in range(0, len(divername)):
                        username = divername[a]
                        #司机用户组
                        b1 = bot.List('buddy', username)
                        if b1:
                            b = b1[0]
                        bot.SendTo(b, content2+ps)
              
            # bot.SendTo(contact, '你好，我是QQ机器人')



if __name__ == '__main__':
    RunBot()
