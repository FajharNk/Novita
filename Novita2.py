import random
import sys
import time
def mengetik(s):
   for c in s + '/n':
	sys.stdout.write(c)
	sys.stdout.flush()

	time.sleep(random.random() * 0.3)

mengetik('aku sayang Novita \n aku inginkan dia \n bisakah dia jadi milikku \n andaikan bisa \n aku pasti bahagia')
