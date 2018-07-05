from multiprocessing import Process
import os

def f(name):
    
    print('hello', name)

if __name__ == '__main__':
    
    l1 = ['Ahmad', 'Hamdy', 'Abdellatif']
   
    #for i in l1:
    #    p = Process(target=f, args=(i,))
    #    p.start()
    for i in range(3):
        p = Process(target=f, args=(l1.pop(),))
        z = Process
        p.start()
    p.join()
    print('Array',l1)