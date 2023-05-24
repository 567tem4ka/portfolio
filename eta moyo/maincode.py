import random
#import datetime
import time

a = ('hello','hi','hi human')
hello = ('hi','hello','hello patatos','hello glados','hello potato')
td = ('what time is it','what time','time','time please')
d = ('погоди-ка, у тебя есть мультиметр? не важно.','2','3','4','5','6','7','8','9','0')

#time = datetime.now()

while True:
    main = input()

    if main in hello:
        print(random.choice(a))

    #elif main in td:
        #(time)


    #while True:
        #sleep(5)
        #print(random.choice(d))

