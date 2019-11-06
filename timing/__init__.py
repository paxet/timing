import atexit
from functools import reduce
import time

separator = '=' * 40
start = -1


def seconds_to_str(seconds: float):
    # Reduce expresion used to convert the seconds variable in a tuple with hours, minutes and seconds splitted.
    h, m, s = reduce(lambda time_tup, interval: divmod(time_tup[0], interval) + time_tup[1:], [(seconds,), 60, 60])
    return '{hours:d}:{minutes:0>2d}:{seconds:0>6.3f}'.format(hours=int(h), minutes=int(m), seconds=s)


def now() -> float:
    # time.clock() was deprecated in Python 3.3
    # return time.process_time()
    return time.perf_counter()


def log(s: str, elapsed=None):
    print(separator)
    print('{} - {}'.format(seconds_to_str(now()), s))
    if elapsed:
        print("Elapsed time: {}".format(elapsed))
    print(separator + '\n')


def start_log():
    global start
    start = now()
    atexit.register(end_log)
    log("Start Program")


def end_log():
    global start
    end = now()
    elapsed = end - start
    log("End Program", seconds_to_str(elapsed))


start_log()
