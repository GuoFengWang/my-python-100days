# -*- coding: utf-8 -*-
#多进程测试脚本
from time import sleep
from multiprocessing import Process
import os

def test(string):
	print(string,  os.getpid())
	sleep(60)
	print('bye%d' %os.getpid())

def main():
	Process(target=test,args=('hello',)).start()
	Process(target=test,args=('world',)).start()


if __name__ == '__main__':
	main() 


