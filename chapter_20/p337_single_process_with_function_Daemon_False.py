from multiprocessing import Process
from time import ctime, sleep

def clock(interval):
	while True:
		print("The time is %s" % ctime())
		sleep(interval)

if __name__ == "__main__":
	p = Process(target=clock, args=(2,))
	p.daemon = False
	p.start()
	#print("hello!")
	#p.join()
