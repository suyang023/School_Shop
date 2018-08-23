#coding=utf-8
from appium import webdriver
# from selenium.webdriver.support import WebDriverWait
# from selenium.webdriver.support expected_conditions as EC
import time
def get_driver():
	config = {
	                'platformName':'Android',
	                'deviceName':'127.0.0.1:21503',
	                'app':'C:\\Python33\\快手.apk',
	                'appPackage':'com.smile.gifmaker',
	                'appActivity':'com.yxcorp.gifshow.HomeActivity'
	                # 'appWaitActivity':'com.yxcorp.gifshow.HomeActivity'

	            }

	driver = webdriver.Remote('http://localhost:4723/wd/hub',config)
	return driver
#滑动函数
# driver.swipe()
#向左滑动
def swipe_r():
	x = get_size()[0]/10
	x1 = get_size()[1]/10*9
	y = get_size()[1]/2
	driver.swipe(x,y,x1,y)
#向右滑动
def swipe_l():
	x = get_size()[0]/10*9
	x1 = get_size()[1]/10
	y = get_size()[1]/2
	driver.swipe(x,y,x1,y)
#向上滑动
def swipe_up():
	x1 = get_size()[0]/2
	y1 = get_size()[1]/10*9
	y = get_size()[1]/10
	driver.swipe(x1,y1,x1,y)
#向下滑动
def swipe_down():
	x1 = get_size()[0]/2
	y1 = get_size()[1]/10
	y = get_size()[1]/10*9
	driver.swipe(x1,y1,x1,y)
#获取屏幕宽高值
def get_size():
	size = driver.get_window_size()
	size_w = size['width']
	size_h = size['height']
	# print(size_w,size_h)
	return size_w,size_h

driver = get_driver()
time.sleep(20)
driver.find_element_by_id('android:id/button2').click()
# num = driver.find_elements_by_id('com.smile.gifmaker:id/subject')[1].text
num = driver.find_elements_by_id('com.smile.gifmaker:id/subject')[1].click()
time.sleep(2)

a = 0
while (1):
	a+=1
	if a == 4:
		time.sleep(5)
		# driver.find_element_by_class_name('android.widget.ImageView').click()
		driver.find_element_by_id('com.smile.gifmaker:id/forward_button_extra').click()
		break
	else:
		print("向下滑动！")
		time.sleep(5)
		swipe_up()
		swipe_down()
		swipe_up()
		
		#参与评论的用户
		user_num = driver.find_elements_by_id('com.smile.gifmaker:id/name')
		user_null = len(user_num)
		print(len(user_num))
		for i in range(len(user_num)):
			print(i)
			if i == 0:
				continue
			user_num_data = user_num[i].click()
			print("正在点击用户头像！")
			time.sleep(5)
			#获取用户名
			try:
				user_name = driver.find_element_by_id('com.smile.gifmaker:id/title_tv_mirror').text
				print(user_name)
			except:
				continue
			#获取签名信息
			try:
				user_name_data = driver.find_element_by_id('com.smile.gifmaker:id/user_text').text
				print(user_name_data)
			except:
				user_name_data = 0
			print("正在退回！")
			
			#个人主页后退按钮
			driver.find_element_by_id('com.smile.gifmaker:id/left_btn').click()
			if i == len(user_num)-2:
				break
			

# for i in range(len(num)):
# 	num_data = num[i].text
# 	print(num_data)

#第一次测试
def demo_1():
	time.sleep(20)
	driver.find_element_by_id('android:id/button2').click()
	num = driver.find_element_by_id('com.smile.gifmaker:id/subject').text
	print(num)
	time.sleep(5)
	driver.find_element_by_id('com.smile.gifmaker:id/player_cover').click()
	swipe_up()
	swipe_up()
	txt = driver.find_element_by_id('com.smile.gifmaker:id/player_cover').click()
	print(txt)


