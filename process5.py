def run():
    print('process started running...')


def shut_down():
    print("process is shutting down...")


def start_task_1():
    print('start task 1')


def start_task_2():
    print('start task 2')


def email_admin():
    print('process tasking emailed to admin')


if __name__ == '__main__':
    # code in this block is run in this order
    run()
    start_task_1()
    start_task_2()
    email_admin()
    shut_down()
