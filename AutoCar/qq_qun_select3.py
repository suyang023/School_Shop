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
        # 司机发单免费群
        b1 = bot.List('group', user)
        # 乘客发单免费群
        b2 = bot.List('group', chengkename)
        # b1 = bot.List('buddy', user)
        if content.find('人找车') != -1:

            # 检测是否含有电话号码
            try:
                matchResult = re.search(r'(\d+)', content)  # 从指定位置开始匹配
                vlaue_phone = matchResult.groups(0)
            except BaseException:
                vlaue_phone = ''
            if vlaue_phone != '':
                content2 = content.replace('人找车', '人-找-车')
                if b1:
                    b = b1[0]
                bot.SendTo(b, content2 + ps)
                # bot.SendTo(contact, '你好，我是QQ机器人')

        elif content.find('车找人') != -1:
            content2 = content.replace('车找人', '车-找-人')
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
        elif i > len(username):
            break
        time.sleep(0.1)

    for i in range(0, len(divername_all)):

        # b1 = bot.List('buddy', user)
        if content.find('人找车') != -1:
            # 检测是否含有电话号码
            try:
                matchResult = re.search(r'(\d+)', content)  # 从指定位置开始匹配
                vlaue_phone = matchResult.groups(0)
            except BaseException:
                vlaue_phone = ''
            if vlaue_phone != '':
                content2 = content.replace('人找车', '人-找-车')
                "重庆-涪陵，重庆-万州，重庆-开州，开州-万州"
                # qun_name_1 = ['重庆永川顺风车群', '重庆永川拼车群', '永川往返重庆顺风车', '永川 江津 重庆 顺风车', '永川到重庆拼车群', '重庆到永川拼车群']
                qun_name_1 = ['重庆涪陵拼车顺风车群', '重庆-涪陵拼车', '重庆←→涪陵拼车群', '涪陵拼车群', '重庆万州拼车群', '万州重庆拼车群', '重庆往返万州拼车群', '重庆～万州拼车专用群', '重庆万州拼车部落', '重庆万州拼车群【➋】', '万州重庆拼车群【➌】', '万州重庆拼车超级群', '万州顺风车总群', '重庆开州拼车群', '重庆开州拼车总群', '重庆至开州往返拼车⑧', '重庆―开州拼车坐车群', '重庆开州州拼车群【➋】', '重庆开州开县拼车交流', '开州重庆拼车群', '开州<->重庆往返拼车', '开州↹重庆↹万州拼车', '开州万州达州重庆拼车']
                qun_name_2 = ['重庆涪陵拼车顺风车群', '重庆-涪陵拼车', '重庆←→涪陵拼车群', '涪陵拼车群', '重庆-长寿-梁平拼车群', '重庆-长寿拼车E族', '长寿拼车到重庆群', '长寿-重庆拼车群', '长寿到重庆拼车群', '长寿重庆拼车群']


                for z in qun_name_1:
                    if z == contact.name:
                        print(contact.name)
                        divername = ['氵', '巴渝山']
                        for a in range(0, len(divername)):
                            username = divername[a]
                            # 司机用户组
                            b1 = bot.List('buddy', username)
                            if b1:
                                b = b1[0]
                            bot.SendTo(b, content2 + ps)
                for z in qun_name_2:
                    if z == contact.name:
                        print(contact.name)
                        divername = ['氵', '巴渝山']
                        for a in range(0, len(divername)):
                            username = divername[a]
                            # 司机用户组
                            b1 = bot.List('buddy', username)
                            if b1:
                                b = b1[0]
                            bot.SendTo(b, content2 + ps)

                        # bot.SendTo(contact, '你好，我是QQ机器人')


if __name__ == '__main__':
    RunBot()
