from qqbot import QQBotSlot as qqbotslot, RunBot


@qqbotslot
def onQQMessage(bot, contact, member, content):

    b1 = bot.List('buddy', 'laoda')


    if content.find('人找车') != -1:
        if b1:
            b = b1[0]
        bot.SendTo(b, content)
        # bot.SendTo(contact, '你好，我是QQ机器人')

    elif content == '在':
        if b1:
            b = b1[0]
        bot.SendTo(b, '我一直在呢，嘻嘻')

    elif content == '-stop':
        if b1:
            b = b1[0]

        bot.SendTo(b, 'QQ机器人已关闭')
        # bot.SendTo(contact, 'QQ机器人已关闭')
        bot.Stop()


if __name__ == '__main__':
    RunBot()

