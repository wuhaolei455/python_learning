from contextlib import contextmanager
import time
import os
import random

# 用于计时with代码块
@contextmanager
def timer(label):
    start = time.time()
    print(f'{label}: start')
    yield 555
    end = time.time()
    print(f'{label}: {end - start} seconds')

with timer('counting') as tag:
    # n = 1000000
    # while n > 0:
    #     n -= 1
    print(f'counting: {tag}')
    time.sleep(0)

# 执行with代码块时，临时更新环境变量
@contextmanager
def set_temp_env(**kwargs):
    cur = "old"
    os.environ['TEST_ENV'] = kwargs['TEST_ENV']
    yield
    # reset
    os.environ['TEST_ENV'] = cur

with set_temp_env(TEST_ENV = 'new'):
    print(f'current env: {os.getenv("TEST_ENV")}')
print(f'current env: {os.getenv("TEST_ENV")}')


@contextmanager
def conditional_manager(condition):
    if condition:
        print("Doing extra setup")
        yield
        print("Doing extra teardown")
    else:
        yield

def get_condition():
    # business logic
    if (random.randint(0, 1) == 1):
        return True
    else:
        return False

with conditional_manager(get_condition()):
    print("BUSINESS LOGIC")