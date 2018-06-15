from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
import json
import base64
import urllib
import time
import requests
import chardet

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)
num = 0


def cqzb_gov():
    try:
        # print('测试2！')
        star1_title_dict_1 = []
        star1_title_dict_2 = []
        all = 1

        while (1):
            url = 'http://www.cqzb.gov.cn/class-5-1.aspx'
            print('第%d次循环！！！' % all)
            browser.get(url)

            for i in range(1, 21):
                star1_url = browser.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/ul/li[%s]/a' % i)
                url = star1_url.get_attribute('href')
                star1_title = browser.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/ul/li[%s]/a' % i).text
                star1_time = browser.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/ul/li[%s]/span' % i).text
                # star1_title = browser.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/ul/li[1]/a').text
                # star1_time = browser.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/ul/li[1]/span').text
                # data_title.append(star1_title)
                # data_time.append(star1_time)

                star1_title_dict_2.append(star1_title)

                paper_data = {
                    'num': i,
                    'url': url,
                    '标题': star1_title,
                    '时间': star1_time,
                }
                # print(paper_data)

                with open("cqzb_gov.json", 'a+', encoding='utf-8') as json_file:
                    json.dump(paper_data, json_file, ensure_ascii=False)
                    json_file.write('\n')

                json_file.close()

            # 去重 赋值
            star1_title_dict_1_set = set(star1_title_dict_1)
            star1_title_dict_2_set = set(star1_title_dict_2)

            cha_value = star1_title_dict_2_set.difference(star1_title_dict_1_set)

            for i in range(len(cha_value)):
                cha_value_pop = cha_value.pop()
                print(cha_value_pop)

                masgee_2(cha_value_pop)

            star1_title_dict_1.clear()

            for i in range(len(star1_title_dict_2)):
                a = star1_title_dict_2[i]
                star1_title_dict_1.append(a)

            star1_title_dict_2.clear()

            time.sleep(60)
            all += 1
    except TimeoutException:

        cqzb_gov()


def masegg_3():
    a = '123'
    a_1 = a.encode(encoding="utf-8")
    pwd = base64.b64encode(a_1)
    pwd_1 = pwd.decode()
    print(pwd_1)
    pro_name = cqgp_gov('https://www.cqgp.gov.cn/notices/list')
    print(pro_name)

    content = '【重庆煌能科技】客户编号:30901项目:{},请登录 http://www.cqggzy.com/jyxx/jyxx-page.html请及时查看消息查看回N退订'.format(pro_name)
    content_1 = content.encode('gbk')
    print(content_1)

    content_2 = {'content': content_1}
    content_value = urllib.parse.urlencode(content_2)
    print(content_value)
    # content_2 = content_1.decode('utf-8', 'ignore')
    # print(content_2)
    url = "http://61.147.98.117:9015/servlet/UserServiceAPI?method=sendSMS&username=jiekouceshi&password={0}&smstype=1&mobile=17623892069&{1}".format(
        pwd_1, content_value)
    print(url)
    repsonse = requests.post(url)

    # req = Request('POST', url, headers=header)
    # prepped = req.prepare()
    # resp = s.send(prepped, timeout=5)  # 可添加上述相关信息
    # a = resp.text
    a = repsonse.text
    print(a)


def cqgp_gov(url, star1_title_all):
    try:
        # print('测试2！')
        browser.get(url)
        for paper_num in range(1, 21):
            star1_url = browser.find_element_by_css_selector(
                '#notice > div > div.list-group.ng-scope > div:nth-child(1) > div > div.col-xs-6 > a')
            # a = browser.find_element_by_xpath('//*[@id="notice"]/div/div[1]/div[1]/div/div[1]').text
            url = star1_url.get_attribute('href')
            star1_title = browser.find_element_by_xpath('//*[@id="notice"]/div/div[1]/div[1]/div/div[1]').text
            star1_time = browser.find_element_by_xpath('//*[@id="notice"]/div/div[1]/div[1]/div/div[3]').text
            '//*[@id="notice"]/div/div[1]/div[20]/div/div[1]/a'
            star1_time_value = star1_time[:10]
            print(url, star1_title, star1_time_value)

            if star1_title_all != star1_title:
                i = num + 1
                paper_data = {
                    'num': i,
                    '标题': star1_title,
                    'url': url,
                    '时间': star1_time_value
                }

                print(paper_data)

                with open("cqgp_gov.json", 'a+', encoding='utf-8') as json_file:
                    json.dump(paper_data, json_file, ensure_ascii=False)
                    json_file.write('\n')

                json_file.close()

                return star1_title
        else:
            return 0
        # print(a)
    except TimeoutException:
        cqgp_gov()


def masgee_1(star1_title_all):
    a = '1234'
    a_1 = a.encode(encoding="utf-8")
    pwd = base64.b64encode(a_1)

    # content = '【重庆煌能科技】客户编号:30901项目:自适应滤波器设计,请登录 http://www.cqggzy.com/jyxx/jyxx-page.html 请及时查看消息查看回N退订'.encode('gbk')

    content_add = cqgp_gov('https://www.cqgp.gov.cn/notices/list', star1_title_all)

    if content_add == 0:
        return star1_title_all

    else:
        content_data = '【重庆煌能科技】客户编号:30901项目:{},请登录 http://www.cqggzy.com/jyxx/jyxx-page.html 请及时查看消息查看回N退订'.format(
            content_add)
        content = content_data.encode('gbk')

        encode = chardet.detect(content)
        print(encode['encoding'])
        print(content)
        print(len(content))

        data = {
            'method': 'sendSMS',
            'username': 'jiekouceshi',
            'password': pwd,
            'smstype': '1',
            'mobile': '17623892069,15520099841',
            'content': content
        }

        url = 'http://61.147.98.117:9015/servlet/UserServiceAPI?'

        response = requests.post(url, data=data)
        a = response.text
        print(a)
        print(data)

        return content_add


def cqgp_gov_2(url):
    try:
        # print('测试2！')
        browser.get(url)
        for i in range(1, 21):

            star1_url = browser.find_element_by_css_selector(
                '#notice > div > div.list-group.ng-scope > div:nth-child(%d) > div > div.col-xs-6 > a' % i)
            # a = browser.find_element_by_xpath('//*[@id="notice"]/div/div[1]/div[1]/div/div[1]').text
            url = star1_url.get_attribute('href')
            star1_title = browser.find_element_by_xpath(
                '//*[@id="notice"]/div/div[1]/div[%d]/div/div[1]' % i).text
            star1_time = browser.find_element_by_xpath('//*[@id="notice"]/div/div[1]/div[%d]/div/div[3]' % i).text

            # star1_title = star1_title_value.text
            # star1_time = star1_time_value.text

            star1_time_value = star1_time[:10]
            star1_time_true = star1_time[10:]

            star1_time_true_1 = star1_time_true.find('刚刚')

            if star1_time_true_1 != -1:

                if -1 < star1_title.find('成交'):
                    continue
                elif -1 < star1_title.find('结果'):
                    continue
                else:

                    print(url, star1_title, star1_time_value)

                    paper_data = {
                        'num': i,
                        '标题': star1_title,
                        'url': url,
                        '时间': star1_time_value
                    }

                    print(paper_data)

                    masgee_2(star1_title)

                    with open("cqgp_gov.json", 'a+', encoding='utf-8') as json_file:
                        json.dump(paper_data, json_file, ensure_ascii=False)
                        json_file.write('\n')

                    json_file.close()
            else:
                continue

        # print(a)
    except TimeoutException:
        cqgp_gov()


def masgee_2(star1_title):
    a = 'cqcmgzs20181'
    a_1 = a.encode(encoding="utf-8")
    pwd = base64.b64encode(a_1)

    # content = '【重庆煌能科技】客户编号:30901项目:自适应滤波器设计,请登录 http://www.cqggzy.com/jyxx/jyxx-page.html 请及时查看消息查看回N退订'.encode('gbk')

    # content_add = cqgp_gov('https://www.cqgp.gov.cn/notices/list')

    # content_add = star1_title
    content_add = '苏阳是个大美女'

    content_data = '【重庆科技】客户编号:30901项目:{},请登录 http://www.zy.com/ge.html 请及时查看消息查看回N退订'.format(
        content_add)
    content = content_data.encode('gbk')

    # 系统编码
    # encode = chardet.detect(content)
    # print(encode['encoding'])
    # print(content)
    print('获取项目名称长度：%s' % len(content))

    data = {
        'method': 'sendSMS',
        'username': '17338635758',
        'password': pwd,
        'smstype': '0',
        'mobile': '17338635758',
        'content': content
    }

    url = 'http://61.147.98.117:9015/servlet/UserServiceAPI?'

    response = requests.post(url, data=data)
    a = response.text
    print(a)

    # print(data)
    # with open("masgge.json", 'a+', encoding='utf-8') as json_file:
    #     json.dump(data, json_file, ensure_ascii=False)
    #     json_file.write('\n')
    # json_file.close()

    print('短信发送成功！！！')


def main_1():
    star1_title_all = ''
    while (1):
        star1_title_all = masgee_1(star1_title_all)
        # cqgp_gov()
        time.sleep(60)


def main_2():
    i = 1
    while (1):
        print('第%d次获取数据' % i)
        cqgp_gov_2('https://www.cqgp.gov.cn/notices/list')
        i += 1
        time.sleep(160)


if __name__ == '__main__':
    cqzb_gov()
    # main_2()
