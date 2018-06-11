
from multiprocessing import Process

def f(name):
	print(name)
	
pa = []

for i in range(1):
	pa = [Process(target = f,args = (i,))]
	for x in pa:
		x.start()
		x.join()
	