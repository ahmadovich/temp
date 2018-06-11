from multiprocessing import Process, Queue
import random

def rand_num(queue,x):
    num = random.random()
    queue.put(num)
    queue.put(x)
    
if __name__ == "__main__":
    queue = Queue()
    
    processes = [Process(target=rand_num, args=(queue,5)) for x in range(4)]
    
    for p in processes:
        p.start()
        
    for p in processes:
        p.join()
    results = []
    while not queue.empty() :
        try :
            results.append(queue.get(block = False))
        except:
            break
        
        
        
    #results = [queue.get() for p in processes]

    print('done')
    print(results)
    print(type(results))