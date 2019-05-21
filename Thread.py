#多线程测试脚本
from time import sleep
from threading import Thread
import os

def test(string):
	print(string,  os.getpid())
	sleep(60)
	print('bye%d' %os.getpid())

def main():
	Thread(target=test,args=('hello',)).start()
	Thread(target=test,args=('world',)).start()


if __name__ == '__main__':
	main() 
	

