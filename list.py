from random import randint, choices
import string
import numpy as np
from datetime import datetime

list1=[]
list2=[]
#main_list=[]
for i in range(0,1000):
    value = "".join(choices(string.ascii_uppercase + string.digits, k=20))
    list2.append(value)
    
for i in range(0,1000):
    value = "".join(choices(string.ascii_uppercase + string.digits, k=20))
    list1.append(value)
    

def time_taken(list1,list2):
    main_list = np.setdiff1d(list2,list1)
    print(main_list)
    

start=datetime.now()
time_taken(list1,list2)
print(datetime.now()-start)
