"""
test-app
to be used for docker training
- build
- push
- pull
- run
"""

from loguru import logger

entry_message = 'Starting app'
logger.info(entry_message)

body_message = """
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""
logger.info(body_message)

import os
import time

dir_path = '/data'
logger.debug(f"What's inside {dir_path} you asked?")
try:
    logger.debug(os.listdir(dir_path))
except FileNotFoundError as e:
    logger.error(f"{dir_path} does not exist - {e}")

exit_message = 'Exiting app'
logger.info(exit_message)

i = 1

while True:
    logger.info(f'still running #{i}')
    i += 1
    time.sleep(4)