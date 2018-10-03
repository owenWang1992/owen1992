import sched, time
import datetime
s = sched.scheduler(time.time, time.sleep)
def print_time(a='default'):
    print("Schedule job at ", '{0:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()), a)

def print_some_times():
    print(datetime.datetime.now())
    s.enter(15, 1, print_time,argument=('job3', ))
    s.enter(10, 2, print_time, argument=('job2',))
    s.enter(5, 1, print_time, kwargs={'a': 'job1'})
    s.run()

if __name__ == '__main__':
    print_some_times()
