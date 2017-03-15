
import threading
from multiprocessing import cpu_count
import random
import turtle

'''
try:
    for i in range(1000):
        threading.Thread(
            target=print_who_and_delay_time,
            args=('Thread-%d'%i,)
            ).start()
except:
    print('Error')
print('Itreration ended')
'''

if __name__ == '__main__':
    def turtle_dot(atuple):
        x, y, tmpturtle = atuple
        tmpturtle.setpos(x, y)
        tmpturtle.dot()

    quakeWindow = turtle.Screen()
    quakeWindow.screensize(1800, 900)

    class test(threading.Thread):
        def __init__(self):
            threading.Thread.__init__(self)

        def turtle_dot(self):
            num_of_jobs = 1300 // cpu_count()
            data = [(random.randrange(0, 1800), random.randrange(0, 900))
                    for i in range(num_of_jobs)]
            tmpturtle = turtle.Turtle()
            tmpturtle.speed(0)
            for item in data:
                x, y = item
                tmpturtle.setpos(x, y)
                tmpturtle.dot()

        def run(self):
            print('Im %s' % threading.current_thread())
            self.turtle_dot()
    
    for i in range(cpu_count()):
        test().start()
    '''
    for arg in args:
        print_who_and_delay_time(arg)
    '''

    quakeWindow.exitonclick()
