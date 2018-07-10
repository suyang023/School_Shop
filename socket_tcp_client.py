# -*- coding:utf-8 -*-
import socket

s = socket.socket()

s.connect(('120.79.87.139',9011))

while 1:
	cmd = raw_input('please input cmd:')
	if cmd == 'exit':break
	elif cmd == '':continue
	s.sendall(cmd)
	data = s.recv(2048)
	print data
s.close()
