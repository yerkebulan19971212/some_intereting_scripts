import time


def the_wrong_way():
    start_time = time.time()

    time.sleep(7)

    print(f'{time.time() - start_time} minut have passed')


the_wrong_way()


def the_right_way():
    start_time = time.monotonic()

    time.sleep(7)

    print(f'{time.monotonic() - start_time} minut have passed')


the_right_way()
