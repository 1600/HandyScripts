import threading
import time

maxs=5
threadLimiter=threading.BoundedSemaphore(maxs)

class encodeThread(threading.Thread):
	def run(self):
		threadLimiter.acquire()
		try:
			for i in range(10):
				print i
				time.sleep(1)
		finally:
			threadLimiter.release()

while 1:
		a=encodeThread()
		a.start()