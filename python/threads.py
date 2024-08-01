# import concurrent.futures

# pool = concurrent.futurers.ThreadPoolExecutor(5)
# futures = []
# for task in tasks:
#      futures.append(pool.submit(task))
# future.result()
# try:
#    future.result()
# except ExceptionType:
#    do whatever
# concurrent.futures.as_completed(futures)
# for result in concurrent.futures.as_completed(ftureus):
#     print(result)
# futures = {}
# for task in tasks:
#     futures[executor.submit(task)] = task_metadata 
# for future in concurrent.futures.as_completed(ftureus):
#      print(futures[future] )

# executor.submit(target_function, arg1, arg2)

import time
import threading

def threading_demo():
    flag = True

    def function(thread_id: str, i_s: int) -> None:
        for i in range(i_s, i_s+10):
            if flag:
                print(f"#{thread_id}: {flag}: {i}")
            else:
                print(f"#{thread_id}: {flag}: Error")
            time.sleep(2)

    # function("t1", 200)
    threads_nos = 10
    threads = []
    for i in range(threads_nos):
        thread = threading.Thread(target=function, args=(f"t{i}", i*100))
        thread.start()
        threads.append(thread)

    # wait for completion
    for thread in threads:
        thread.join()

    time.sleep(3)
    flag = False
    print('demo_threading complete')

# threading_demo()


from concurrent.futures import ThreadPoolExecutor, as_completed

def concurrent_futures_demo():
    flag = True
    def target_function(thread_id: str, i_s: int) -> None:
        for i in range(i_s, i_s+5):
            if flag:
                print(f"#{thread_id}: {flag}: {i}")
            else:
                print(f"#{thread_id}: {flag}: Error")
            time.sleep(1)
        return time.time()
    
    # futures = []
    # with ThreadPoolExecutor(max_workers=2) as executor:
    #     for i in range(10):
    #         future = executor.submit(target_function, i, i*100)
    #         futures.append(future)
    # print(futures)
    # executor = ThreadPoolExecutor(max_workers=2)
    # future = executor.submit(target_function, 't1', 100)
    # print(future)
    futures = []
    with ThreadPoolExecutor(max_workers=2) as executor:
        for i in range(5):
            future = executor.submit(target_function, f"t{i}", i*100)
            futures.append(future)
        
        for future in as_completed(futures):
            flag = not flag
            print('completed', future.result())

        print('all tasks submitted, but didnt exit now')

    print('concurrent_futures_demo body completed')
    
# concurrent_futures_demo()
# print('concurrent_futures_demo completed')