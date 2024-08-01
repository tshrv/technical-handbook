import asyncio
import time

flag = True
async def tgt_function(task_id: str, i_s: int) -> None:
    for i in range(i_s, i_s+5):
        if flag:
            print(f"#{task_id}: {flag}: {i}")
        else:
            print(f"#{task_id}: {flag}: Error")
        # time.sleep(1)
        await asyncio.sleep(1)
    return f"#{task_id} - {time.time()}"

# asyncio.run(tgt_function('t1', 100))

async def exit_function():
    print("exit_function")

async def main():
    # parallel - using asyncio.create_task
    """
    Offers more flexibility as it allows you to start tasks and manage them individually.
    You can choose when to wait for each task, cancel tasks, etc.
    """
    t1 = asyncio.create_task(tgt_function('t1', 100))
    t2 = asyncio.create_task(tgt_function('t2', 100))
    await t1
    await t2
    
    # parallel - using asyncio.gather
    """
    Simplifies running multiple tasks together and waiting for all of them to complete.
    It's useful when you want to wait for the results of all tasks at once.
    """
    # await asyncio.gather(tgt_function('t1', 100), tgt_function('t2', 200))

    # # sequential
    # await tgt_function('t1', 100)
    # await tgt_function('t2', 200)

    print("exiting main")

asyncio.run(main())
