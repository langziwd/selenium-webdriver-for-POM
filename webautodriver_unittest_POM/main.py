import os
from time import sleep

def run_test():
    os.system("python -m test_runner.test_runner_login_01")
    sleep(10)
    # os.system():意思在于window中打开了cmd命令窗口
    # os.system("python -m test_case.test_case_002_register")

if __name__ == '__main__':


    run_test()
    # 10S后关机
    sleep(10)
    # os.system('shutdown -s -f')
