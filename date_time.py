''' Write a program to add two times given in 24 hours format

(example:  19 10 
                + 02 50
    new time 22 10) '''
 
import datetime
from datetime import timedelta

gd=datetime.timedelta(hours=19,minutes=10) 
time=gd+datetime.timedelta(hours=2,minutes=50) 
print(time)