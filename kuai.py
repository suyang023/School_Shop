#coding=utf-8
from appium import webdriver
# from selenium.webdriver.support import WebDriverWait
# from selenium.webdriver.support expected_conditions as EC
import time
import re
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
while(1):

	for z in range(0,3):
		# com.smile.gifmaker:id/container
		# com.smile.gifmaker:id/player_cover
		# num = driver.find_elements_by_id('com.smile.gifmaker:id/subject')[z].click()
		num = driver.find_elements_by_id('com.smile.gifmaker:id/player_cover')[z].click()
		time.sleep(2)
		a = 0
		while (1):
			a+=1
			if a == 2:
				time.sleep(5)
				# driver.find_element_by_class_name('android.widget.ImageView').click()
				driver.find_element_by_id('com.smile.gifmaker:id/forward_button_extra').click()
				break
			else:
				print("向下滑动！")
				time.sleep(3)
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
					time.sleep(3)
					#获取用户名
					try:
						user_name = driver.find_element_by_id('com.smile.gifmaker:id/title_tv_mirror').text
						print(user_name)
					except:
						continue
					#获取签名信息
					try:
						user_name_data = driver.find_element_by_id('com.smile.gifmaker:id/user_text').text
						data_ = user_name_data.replace("\n", ",")
						reg = '.*?([A-Za-z0-9]{5,12})'
						data = re.match(reg, data_)
						# print(data)
						if data:
							message1 = data.group(0)
							print('数据获取成功！')
							print(data.group(0))
							with open("user_data.txt","a+") as f:
								f.write("用户名：%s,用户信息：%s"%(user_name,message1))
		        			# f.write("用户名:{0},用户信息：{1})".format(user_name,mes))
					except:
						user_name_data = 0
					print("正在退回！")
					
					#个人主页后退按钮
					try:
						driver.find_element_by_id('com.smile.gifmaker:id/left_btn').click()
						if i == len(user_num)-2:
							break
					except:
						pass
		try:
			time.sleep(2)
			driver.find_element_by_id('com.smile.gifmaker:id/dialog_cancel_image_button').click()
		except:
			pass
		try:
			driver.find_element_by_id('com.smile.gifmaker:id/alert_dialog_cancle_tv').click()
		except:
			pass
			
	#向下滑动
	swipe_up()			

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


