
import threading
#import random
import turtle
from multiprocessing import Process

if __name__ == '__main__':

    data = [[(1101, 754), (948, 107), (1487, 578), (890, 80)], 
        [(1187, 580), (750, 19), (724, 289), (105, 559)],
        [(1121, 758), (1652, 299), (957, 896), (11, 208)]
        ]

    def turtle_dot(atuple):
        x, y, tmpturtle = atuple
        tmpturtle.setpos(x, y)
        tmpturtle.dot()

    quakeWindow = turtle.Screen()
    quakeWindow.screensize(1800, 900)

    
    class test(threading.Thread):
        def __init__(self, data, tmpturtle):
            threading.Thread.__init__(self)
            self.data = data
            self.tmpturtle = tmpturtle

        def turtle_dot(self):
            self.tmpturtle.speed(0)
            print('Im doing jobs')
            x, y = self.data
            print('x:',x, 'y', y)
            self.tmpturtle.setpos(x, y)
            self.tmpturtle.dot()

        def run(self):
            print('Im %s' % threading.current_thread())
            self.turtle_dot()
    
    def main(alist, aturtle):
        for point in alist:
            tmp_thread = test(point, aturtle)
            tmp_thread.start()

    main_turtles = [turtle.Turtle() for i in range(3)]
    count = 0
    for sub_list in data:
        print(sub_list)
        tmp_p = Process(target=main, args=(sub_list, main_turtles[count]))
        count += 1
        tmp_p.start()
        tmp_p.join()
        
    print('Iteration ended')

    quakeWindow.exitonclick()
