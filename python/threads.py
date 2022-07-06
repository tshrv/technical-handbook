"""
Threading pseudo code by ash2shukla@gmail.com
"""

import concurrent.futures
pool = concurrent.futurers.ThreadPoolExecutor(5)
futures = []
for task in tasks:
     futures.append(pool.submit(task))
future.result()
try:
   future.result()
except ExceptionType:
   do whatever
concurrent.futures.as_completed(futures)
for result in concurrent.futures.as_completed(ftureus):
    print(result)
futures = {}
for task in tasks:
    futures[executor.submit(task)] = task_metadata 
for future in concurrent.futures.as_completed(ftureus):
     print(futures[future] )

executor.submit(target_function, arg1, arg2)
