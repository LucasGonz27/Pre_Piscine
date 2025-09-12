import random
import time

start = time.time()
for i in range(random.randint(1,100)):
    print(i)
    print(time.time()-start)